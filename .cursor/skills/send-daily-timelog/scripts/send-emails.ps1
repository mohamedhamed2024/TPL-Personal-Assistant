param(
    [Parameter(Mandatory = $false)]
    [string]$EmlDir,

    [Parameter(Mandatory = $false)]
    [string]$File
)

$ErrorActionPreference = 'Stop'

function Send-EmlFile {
    param(
        [string]$Path,
        [object]$Outlook
    )

    $raw = Get-Content -LiteralPath $Path -Raw -Encoding UTF8
    $name = Split-Path -Leaf $Path

    if ($raw -match '(?m)^To:\s*(.+)$') { $to = $Matches[1].Trim() }
    else { throw "Missing To header in $name" }

    if ($raw -match '(?m)^Subject:\s*(.+)$') { $subject = $Matches[1].Trim() }
    else { throw "Missing Subject header in $name" }

    $htmlStart = $raw.IndexOf('<html>')
    if ($htmlStart -lt 0) { throw "Missing HTML body in $name" }
    $htmlBody = $raw.Substring($htmlStart)

    $mail = $Outlook.CreateItem(0)
    $mail.To = $to
    $mail.Subject = $subject
    $mail.HTMLBody = $htmlBody
    $mail.Send()

    return [PSCustomObject]@{
        File    = $name
        To      = $to
        Subject = $subject
        Status  = 'Sent'
    }
}

try {
    $outlook = [Runtime.InteropServices.Marshal]::GetActiveObject('Outlook.Application')
}
catch {
    $outlook = New-Object -ComObject Outlook.Application
}

$results = @()

if ($File) {
    if (-not (Test-Path -LiteralPath $File)) {
        throw "File not found: $File"
    }
    try {
        $results += Send-EmlFile -Path $File -Outlook $outlook
    }
    catch {
        $results += [PSCustomObject]@{
            File    = (Split-Path -Leaf $File)
            To      = ''
            Subject = ''
            Status  = "Failed: $($_.Exception.Message)"
        }
    }
}
elseif ($EmlDir) {
    if (-not (Test-Path -LiteralPath $EmlDir)) {
        throw "Directory not found: $EmlDir"
    }
    $emlFiles = Get-ChildItem -LiteralPath $EmlDir -Filter '*.eml' | Sort-Object Name
    if ($emlFiles.Count -eq 0) {
        throw "No .eml files found in $EmlDir"
    }
    foreach ($item in $emlFiles) {
        try {
            $results += Send-EmlFile -Path $item.FullName -Outlook $outlook
        }
        catch {
            $results += [PSCustomObject]@{
                File    = $item.Name
                To      = ''
                Subject = ''
                Status  = "Failed: $($_.Exception.Message)"
            }
        }
    }
}
else {
    throw 'Specify -EmlDir or -File'
}

$results | Format-Table -AutoSize | Out-String | Write-Output
