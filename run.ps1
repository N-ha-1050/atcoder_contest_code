Param(
    [parameter(Mandatory=$true)][string]$file,
    [string]$in=".\in.txt",
    [string]$out=".\out.txt"
)
Write-Host $file を実行します。
Get-Content $in | python $file > $out
Write-Host black と isort を実行します
Write-Host
python -m black $file
Write-Host
python -m isort $file
Write-Host
# python -m mypy $file
Write-Host 実行が完了しました。