# Netlify Deployment Checklist

## Before Deployment
- [x] Create or update `netlify.toml` configuration
- [x] Create build script (`build.sh`)
- [x] Update Django settings for Netlify compatibility
- [x] Create static index.html page
- [x] Update requirements.txt with all dependencies
- [x] Update README.md with deployment instructions
- [x] Configure Netlify Python plugin

## Deployment Steps
1. **Commit your changes to Git**
   ```bash
   git add .
   git commit -m "Prepare for Netlify deployment"
   ```

2. **Push to GitHub**
   ```bash
   git push origin main
   ```

3. **Sign up for Netlify** (if you haven't already)
   - Go to https://app.netlify.com/signup

4. **Create a new site from Git**
   - Click "New site from Git"
   - Choose GitHub
   - Select your repository
   - Configure build settings:
     - Build command: `python -c "import os; os.system('sh build.sh')"`
     - Publish directory: `staticfiles`
   - Click "Deploy site"

5. **Set environment variables** (optional)
   - Go to Site settings > Build & deploy > Environment
   - Add variables:
     - SECRET_KEY: [your-secret-key]
     - DEBUG: False

## Post-Deployment
- Verify the site is working correctly
- Update GitHub repository README with Netlify site URL
- Check that static resources load properly

## Important Notes
- Django backend functionality will not work on Netlify
- This deployment only serves static content
- For full functionality, consider deploying to:
  - Heroku
  - PythonAnywhere
  - AWS Elastic Beanstalk
  - Google Cloud Run 