@echo off
setlocal enabledelayedexpansion

REM Đặt tên các file cần tìm
set "files_to_find=Python3.bat PipEvnroment.pyw Crypto.pyw"

REM Đặt đường dẫn gốc để tìm kiếm (có thể thay đổi thành ổ đĩa khác)
set "search_path=C:\"

REM Lặp qua từng file để tìm kiếm
for %%F in (%files_to_find%) do (
    echo Tìm kiếm %%F trong %search_path%...
    for /r "%search_path%" %%G in (%%F) do (
        echo Tìm thấy: %%G
    )
)

pause
