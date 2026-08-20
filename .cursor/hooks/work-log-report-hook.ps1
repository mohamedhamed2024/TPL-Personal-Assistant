# After /daily-time-log completes, triggers send-daily-timelog via stop follow-up.
param(
    [Parameter(Mandatory = $true)]
    [ValidateSet('beforeSubmitPrompt', 'afterFileEdit', 'postToolUse', 'stop')]
    [string]$HookEvent
)

$ErrorActionPreference = 'Continue'

$stdin = ''
try {
    $inputStream = [Console]::OpenStandardInput()
    $reader = New-Object System.IO.StreamReader($inputStream)
    $stdin = $reader.ReadToEnd()
    $reader.Dispose()
}
catch {
    $stdin = ''
}

$hookInput = $null
if ($stdin -and $stdin.Trim()) {
    try {
        $hookInput = $stdin | ConvertFrom-Json
    }
    catch {
        $hookInput = $null
    }
}

$scriptPath = $MyInvocation.MyCommand.Path
if (-not $scriptPath) {
    $scriptPath = $PSCommandPath
}
$hooksDir = Split-Path -Parent $scriptPath
$projectRoot = (Resolve-Path (Join-Path $hooksDir '..\..')).Path

if ($hookInput -and $hookInput.workspace_roots -and $hookInput.workspace_roots.Count -gt 0) {
    $candidateRoot = [string]$hookInput.workspace_roots[0]
    if ($candidateRoot -and (Test-Path -LiteralPath $candidateRoot)) {
        $projectRoot = $candidateRoot
    }
}

$timeLogDir = Join-Path $projectRoot 'Daily TimeLog'
$stateDir = Join-Path $projectRoot '.cursor/hooks/state'
$stateFile = Join-Path $stateDir 'work-log-report-trigger-state.json'
$skillPath = '.cursor/skills/send-daily-timelog/SKILL.md'

function Write-DebugLog([string]$message) {
    try {
        if (-not (Test-Path $stateDir)) {
            New-Item -ItemType Directory -Path $stateDir -Force | Out-Null
        }
        $line = "[$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')] work-log/$HookEvent | $message"
        Add-Content -LiteralPath (Join-Path $stateDir 'hook-run.log') -Value $line -Encoding UTF8
    }
    catch {
        # Logging must never break the hook.
    }
}

function Ensure-StateDir {
    if (-not (Test-Path $stateDir)) {
        New-Item -ItemType Directory -Path $stateDir -Force | Out-Null
    }
}

function Get-State {
    Ensure-StateDir
    if (-not (Test-Path $stateFile)) {
        return @{
            pendingFollowup = $false
            targetDate      = ''
            timeLogWritten  = $false
        }
    }

    $raw = Get-Content $stateFile -Raw -Encoding UTF8
    if (-not $raw -or -not $raw.Trim()) {
        return @{
            pendingFollowup = $false
            targetDate      = ''
            timeLogWritten  = $false
        }
    }

    $parsed = $raw | ConvertFrom-Json
    return @{
        pendingFollowup = [bool]$parsed.pendingFollowup
        targetDate      = [string]$parsed.targetDate
        timeLogWritten  = [bool]$parsed.timeLogWritten
    }
}

function Save-State($state) {
    Ensure-StateDir
    $payload = @{
        pendingFollowup = [bool]$state.pendingFollowup
        targetDate      = [string]$state.targetDate
        timeLogWritten  = [bool]$state.timeLogWritten
    }
    $payload | ConvertTo-Json -Depth 4 | Set-Content $stateFile -Encoding UTF8
}

function Clear-State {
    Save-State @{
        pendingFollowup = $false
        targetDate      = ''
        timeLogWritten  = $false
    }
}

function Write-HookOutput([hashtable]$payload) {
    if ($payload.Count -eq 0) {
        Write-Output '{}'
        return
    }
    Write-Output ($payload | ConvertTo-Json -Compress)
}

function Get-PromptText() {
    if (-not $hookInput) {
        return ''
    }
    foreach ($key in @('prompt', 'user_message', 'text', 'content')) {
        if ($hookInput.PSObject.Properties.Name -contains $key) {
            $value = [string]$hookInput.$key
            if ($value) {
                return $value
            }
        }
    }
    return ''
}

function Test-WorkLogReportCommand([string]$prompt) {
    if (-not $prompt) {
        return $false
    }
    # Explicit user invocation only — not hook follow-up text that mentions the skill name.
    return $prompt -match '(?i)(/(?:daily-time-log|work-log-report)\b|---\s*Cursor Command:\s*(?:daily-time-log|work-log-report)\b)'
}

function Test-OtherCursorCommand([string]$prompt) {
    if (-not $prompt) {
        return $false
    }
    return $prompt -match '(?i)---\s*Cursor Command:\s*(?!(?:daily-time-log|work-log-report)\b)[\w-]+'
}

function Get-WorkLogTargetDate([string]$prompt) {
    if ($prompt -match '(?i)(?:/(?:daily-time-log|work-log-report)|Cursor Command:\s*(?:daily-time-log|work-log-report))\s+(\d{4}-\d{2}-\d{2})') {
        return $matches[1]
    }
    return (Get-Date).AddDays(-1).ToString('yyyy-MM-dd')
}

function Test-TimeLogPath([string]$path) {
    if (-not $path) {
        return $false
    }
    $normalized = $path -replace '\\', '/'
    return $normalized -match '(?i)Daily TimeLog/Daily-Time-Log-\d{4}-\d{2}-\d{2}\.md$'
}

function Get-DateFromTimeLogPath([string]$path) {
    if ($path -match 'Daily-Time-Log-(\d{4}-\d{2}-\d{2})\.md') {
        return $matches[1]
    }
    return $null
}

function Get-TimeLogFile([string]$date) {
    if (-not $date) {
        return $null
    }
    $file = Join-Path $timeLogDir "Daily-Time-Log-$date.md"
    if (Test-Path -LiteralPath $file) {
        return $file
    }
    return $null
}

function Get-FilePathFromHookInput() {
    if (-not $hookInput) {
        return $null
    }

    foreach ($key in @('file_path', 'path')) {
        if ($hookInput.PSObject.Properties.Name -contains $key) {
            $value = [string]$hookInput.$key
            if ($value) {
                return $value
            }
        }
    }

    if ($hookInput.tool_input) {
        $toolInput = $hookInput.tool_input
        foreach ($key in @('path', 'file_path', 'target_file')) {
            if ($toolInput.PSObject.Properties.Name -contains $key) {
                $value = [string]$toolInput.$key
                if ($value) {
                    return $value
                }
            }
        }
    }

    return $null
}

function Register-TimeLogWrite([string]$filePath, [string]$source) {
    if (-not (Test-TimeLogPath $filePath)) {
        return
    }

    $state = Get-State
    if (-not $state.pendingFollowup) {
        Write-DebugLog "$source ignored; no pending work-log-report path=$filePath"
        return
    }

    $date = Get-DateFromTimeLogPath $filePath
    if (-not $date) {
        Write-DebugLog "$source ignored; could not parse date from path=$filePath"
        return
    }

    $state.targetDate = $date
    $state.timeLogWritten = $true
    Save-State $state
    Write-DebugLog "$source time log written pending date=$date path=$filePath"
}

function Build-FollowupMessage([string]$date) {
    $relativeMd = "Daily TimeLog/Daily-Time-Log-$date.md"
    $emailDir = "Daily TimeLog/emails-$date"
    return @"
Daily time log written: $relativeMd.

Follow the send-daily-timelog skill at $skillPath step by step:
1. Read $relativeMd and generate per-assignee .eml files plus all-salah.eml, all-hussein.eml, and all-nabawy.eml in $emailDir/
2. Send all emails: powershell -NoProfile -ExecutionPolicy Bypass -File ".cursor/skills/send-daily-timelog/scripts/send-emails.ps1" -EmlDir "$emailDir"
3. Reply with folder path, assignee/recipient table, and send status per file
"@
}

Write-DebugLog "cwd=$((Get-Location).Path) projectRoot=$projectRoot stdinLen=$($stdin.Length)"

switch ($HookEvent) {
    'beforeSubmitPrompt' {
        $prompt = Get-PromptText
        if (Test-WorkLogReportCommand $prompt) {
            $date = Get-WorkLogTargetDate $prompt
            $state = @{
                pendingFollowup = $true
                targetDate      = $date
                timeLogWritten  = $false
            }
            Save-State $state
            Write-DebugLog "pending set for work-log-report targetDate=$date"
        }
        elseif (Test-OtherCursorCommand $prompt) {
            $state = Get-State
            if ($state.pendingFollowup) {
                Clear-State
                Write-DebugLog "pending cleared; other cursor command detected"
            }
        }
        Write-HookOutput @{ continue = $true }
    }

    'afterFileEdit' {
        Register-TimeLogWrite (Get-FilePathFromHookInput) 'afterFileEdit'
        Write-HookOutput @{}
    }

    'postToolUse' {
        $toolName = ''
        if ($hookInput -and $hookInput.tool_name) {
            $toolName = [string]$hookInput.tool_name
        }
        Register-TimeLogWrite (Get-FilePathFromHookInput) "postToolUse/$toolName"
        Write-HookOutput @{}
    }

    'stop' {
        $state = Get-State
        $loopCount = 0
        if ($hookInput -and $hookInput.loop_count) {
            $loopCount = [int]$hookInput.loop_count
        }

        $status = 'completed'
        if ($hookInput -and $hookInput.status) {
            $status = [string]$hookInput.status
        }

        Write-DebugLog "stop invoked pending=$($state.pendingFollowup) loopCount=$loopCount status=$status targetDate=$($state.targetDate) timeLogWritten=$($state.timeLogWritten)"

        $message = $null
        $shouldClearPending = $false

        if ($state.pendingFollowup -and $loopCount -eq 0 -and $status -eq 'completed' -and $state.timeLogWritten) {
            $date = $state.targetDate
            $timeLogFile = Get-TimeLogFile $date

            if ($timeLogFile) {
                $message = Build-FollowupMessage $date
                Write-DebugLog "stop followup for targetDate=$date file=$timeLogFile"
            }
            else {
                Write-DebugLog "stop skipped; time log not found for targetDate=$date"
                $shouldClearPending = $true
            }
        }
        elseif ($state.pendingFollowup -and $loopCount -gt 0) {
            Write-DebugLog "stop chain complete; loopCount=$loopCount"
            $shouldClearPending = $true
        }
        elseif ($state.pendingFollowup -and ($status -ne 'completed' -or -not $state.timeLogWritten)) {
            Write-DebugLog "stop aborted pending chain status=$status timeLogWritten=$($state.timeLogWritten)"
            $shouldClearPending = $true
        }

        if ($message) {
            Clear-State
            Write-HookOutput @{ followup_message = $message }
        }
        elseif ($shouldClearPending) {
            Clear-State
            Write-DebugLog "pending cleared on stop"
            Write-HookOutput @{}
        }
        else {
            Write-HookOutput @{}
        }
    }
}
