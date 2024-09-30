@echo off
:: Check if Node.js is installed
where node >nul 2>nul
if %errorlevel% neq 0 (
    echo Node.js is not installed. Please install Node.js from https://nodejs.org/
    pause
    exit /b
)

:: Run npm install for discord.js-selfbot-v13@latest
echo Installing discord.js-selfbot-v13@latest...
npm install discord.js-selfbot-v13@latest

if %errorlevel% neq 0 (
    echo Failed to install discord.js-selfbot-v13. Please check for errors.
    pause
    exit /b
)

echo Installation completed successfully.
pause
