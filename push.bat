@echo off
chcp 65001 >nul

echo === fowt-cable-ai push ===
echo.

:: Check remote origin
git remote get-url origin >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] No remote origin found.
    echo.
    echo Run this once:
    echo   git remote add origin https://github.com/YOUR_USERNAME/REPO.git
    echo.
    pause
    exit /b 1
)

:: Check for changes
git status --short > "%TEMP%\_fowt_status.tmp"
for %%A in ("%TEMP%\_fowt_status.tmp") do set SIZE=%%~zA
del "%TEMP%\_fowt_status.tmp"
if %SIZE%==0 (
    echo Nothing to commit. Already up to date.
    echo.
    pause
    exit /b 0
)

git status --short
echo.

git add -A

:: Get today's date
for /f %%D in ('powershell -NoProfile -Command "Get-Date -Format yyyy-MM-dd"') do set TODAY=%%D
set DEFAULT_MSG=update: %TODAY%

set MSG=
set /p MSG=Commit message [%DEFAULT_MSG%]:
if "%MSG%"=="" set MSG=%DEFAULT_MSG%

git commit -m "%MSG%"
if %errorlevel% neq 0 (
    echo.
    echo [ERROR] Commit failed.
    pause
    exit /b 1
)

for /f %%B in ('git rev-parse --abbrev-ref HEAD') do set BRANCH=%%B
git push origin %BRANCH%
if %errorlevel% neq 0 (
    echo.
    echo [ERROR] Push failed. Check your internet connection.
    pause
    exit /b 1
)

echo.
echo Done - pushed to GitHub (branch: %BRANCH%)
echo.
pause
