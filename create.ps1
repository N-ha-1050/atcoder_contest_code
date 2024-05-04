Param(
    [parameter(Mandatory=$true)][string]$contest,
    [array]$problems
)
Write-Host $contest を作成します
New-Item -Path . -Name $contest -ItemType "directory" -Force
Write-Host $problems を作成します
foreach ($problem in $problems) {
    Copy-Item ".\main.py" -Destination ".\$contest\$problem.py"
}
Write-Host
Write-Host 作成が完了しました
