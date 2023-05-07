Get-ChildItem -Directory | ForEach-Object {
    $size = (Get-ChildItem $_.FullName -Recurse | Measure-Object -Property Length -Sum).Sum
    "$($_.FullName): $(($size / 1MB).ToString("0.00")) MB" | Out-File -Append -FilePath "folder_sizes.txt"
}
