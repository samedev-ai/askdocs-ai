# 🚀 Deployment Guide

## Step 1: Initialize Git Repository

Open your terminal in the project directory (`C:\Users\DELL\Desktop\python`) and run these commands:

```bash
# Initialize git repository
git init

# Add all files
git add .

# Make first commit
git commit -m "Initial commit: Document QA System"
```

## Step 2: Create GitHub Repository

1. Go to [GitHub.com](https://github.com)
2. Click the "+" icon → "New repository"
3. Name it: `document-qa-system` (or any name you prefer)
4. **Don't** initialize with README (we already have one)
5. Click "Create repository"

## Step 3: Connect Local Repository to GitHub

After creating the repository, GitHub will show you commands. Run these:

```bash
# Add remote origin (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/document-qa-system.git

# Push to GitHub
git branch -M main
git push -u origin main
```

## Step 4: Deploy to Streamlit Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Sign in with your GitHub account
3. Click "New app"
4. Select your repository: `YOUR_USERNAME/document-qa-system`
5. Main file path: `app.py`
6. Click "Deploy!"

## Step 5: Configure API Key in Streamlit Cloud

1. In your Streamlit Cloud app, click the gear icon (⚙️) → "Settings"
2. Go to "Secrets" tab
3. Add this content:
```toml
OPENROUTER_API_KEY = "your-actual-api-key-here"
```
4. Click "Save"
5. Your app will automatically restart

## 🎉 Your App is Now Live!

Your Document QA System will be available at:
`https://YOUR_USERNAME-document-qa-system-app-xyz123.streamlit.app/`

## Alternative: One-Click Commands

If you want to do this all at once, here are the complete commands:

```bash
# Navigate to your project
cd "C:\Users\DELL\Desktop\python"

# Initialize and push to GitHub (replace YOUR_USERNAME and YOUR_REPO_NAME)
git init
git add .
git commit -m "Initial commit: Document QA System"
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git branch -M main
git push -u origin main
```

## Troubleshooting

### If git is not installed:
1. Download from [git-scm.com](https://git-scm.com/download/win)
2. Install with default settings
3. Restart your terminal

### If you get authentication errors:
1. Use GitHub Desktop instead
2. Or set up SSH keys: [GitHub SSH Guide](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)

### If deployment fails:
1. Check the logs in Streamlit Cloud
2. Ensure all dependencies are in requirements.txt
3. Verify the API key is correctly set in secrets
