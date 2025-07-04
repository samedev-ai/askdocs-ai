@echo off
echo 🚀 Document QA System - Deployment Script
echo ========================================
echo.

REM Check if git is installed
git --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Git is not installed. Please install Git first:
    echo https://git-scm.com/download/win
    pause
    exit /b 1
)

echo ✅ Git is installed
echo.

REM Initialize git repository if not already done
if not exist ".git" (
    echo 📦 Initializing Git repository...
    git init
    echo ✅ Git repository initialized
) else (
    echo ✅ Git repository already exists
)

REM Add all files
echo 📁 Adding all files to git...
git add .

REM Check if there are changes to commit
git diff --cached --quiet
if errorlevel 1 (
    echo 💾 Committing changes...
    git commit -m "Deploy: Document QA System"
    echo ✅ Changes committed
) else (
    echo ℹ️ No changes to commit
)

echo.
echo 🎯 Next Steps:
echo 1. Create a new repository on GitHub.com
echo 2. Copy and run this command (replace YOUR_USERNAME and YOUR_REPO):
echo.
echo    git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
echo    git branch -M main
echo    git push -u origin main
echo.
echo 3. Go to share.streamlit.io and deploy your app
echo 4. Add your OPENROUTER_API_KEY in Streamlit Cloud secrets
echo.
echo 📖 See deploy.md for detailed instructions
echo.
pause
