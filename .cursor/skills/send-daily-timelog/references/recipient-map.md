# Recipient map — Daily Time Log emails

Resolve **To** and greeting **FirstName** before generating `.eml` files. Update this file when addresses are confirmed or corrected.

## Confirmed addresses

| Jira / report displayName | Email | Greeting | Notes |
|---------------------------|-------|----------|-------|
| Islam Fathy | islam.fathy@integrant.com | Islam | |
| Michael Girgis | michael.girgis@integrant.com | Michael | |
| Sara Hassan | sarah.hassaan@integrant.com | Sara | Jira may show "Sara Hassan"; standup name **Sarah** |
| Sarah Hassaan | sarah.hassaan@integrant.com | Sara | Same person as Sara Hassan |
| Mahmoud Salah | mahmoud.salah@integrant.com | — | Full report only (`all-salah.eml`) |
| Hussein (Mohamed Ahmed) | Mohamed.Ahmed@integrant.com | — | Full report only (`all-hussein.eml`) |
| Nabawy | mnabawy@integrant.com | — | Full report only (`all-nabawy.eml`) |

## Default for unlisted assignees

1. Split `displayName` on space → `{first}.{last}@integrant.com` (all lowercase).
2. Greeting = first token of `displayName`.
3. Tell the user the address is inferred and should be verified before first send.

## Examples

| displayName | Inferred email |
|-------------|----------------|
| Youssef Yahiya | youssef.yahiya@integrant.com |
| Mohamed Hamed | mohamed.hamed@integrant.com |

Add rows to **Confirmed addresses** once verified.
