@echo off
set script_path=%~dp0Encrypt.ps1
powershell -ExecutionPolicy Bypass -File "%script_path%"
exit
