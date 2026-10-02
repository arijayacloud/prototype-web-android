$ProjectRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location -LiteralPath $ProjectRoot
Write-Host "Viewer berjalan di http://127.0.0.1:8080"
Write-Host "Tekan Ctrl+C untuk menghentikan server."
python -m http.server 8080 --bind 127.0.0.1
