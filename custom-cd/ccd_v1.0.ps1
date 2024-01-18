# Mushphyqur Raham Tanveer (c) 2024
# Version 1.0

param(
    [string]$searchString
)

if (-not $searchString) {
    Write-Host "Usage: $((Get-Command $MyInvocation.InvocationName).Definition) -searchString <search_string>"
    exit 1
}

$matchingDirectories = Get-ChildItem -Directory | Where-Object { $_.Name -like "*$searchString*" }

if ($matchingDirectories.Count -gt 0) {
    $matchingDirectories | ForEach-Object {
        Set-Location -Path $_.FullName
        Write-Host "Changed to: $((Get-Location).Path)"
    }
    exit 0
} else {
    Write-Host "No directory found partially matching the specified string: $searchString"
    exit 1
}

