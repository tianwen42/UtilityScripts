@echo off
setlocal enabledelayedexpansion
set i=1

:: Gets a non-duplicate list of file extensions
set "extensions="
for %%A in (*) do (
    set "ext=%%~xA"
    if /I not "%%~xF" == ".bat" (
        if "!extensions!" == "" (
            set "extensions=!ext!"
        ) else (
            echo !extensions! | findstr /C:"!ext!" >nul || set "extensions=!extensions! !ext!"
        )
    )
)

:: Rename each type in turn
for %%E in (%extensions%) do (
    set i=1
    if not exist "%%~E" mkdir "%%~E"
    for %%F in (*%%E) do (
            move "%%F" "%%~E\img!i!%%~xE"  
            :: if you want 1.jpg 2.jpg 3.jpg, please refer [move "%%F" "%%~E\!i!%%~xE"]
            set /a i+=1
    )
)

echo File rename complete!
pause