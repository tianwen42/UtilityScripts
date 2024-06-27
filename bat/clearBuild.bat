@echo off
set "targetFolder=.\"

echo Searching and deleting the build folder in all subfolders...

for /d /r %targetFolder% %%i in (*build) do (
    rmdir /s /q "%%i"
    echo %%i...Deleted
)

echo The Build folder in all subfolders has been successfully deleted.

pause