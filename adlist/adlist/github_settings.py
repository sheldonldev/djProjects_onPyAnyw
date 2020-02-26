# Copy this file to github_settings.py (don't check it into github)

# Go to https://github.com/settings/developers

# Add a New OAuth2 App

# Using ngrok is hard because the url changes every time you start ngrok

# If you are running on localhost, here are some settings:

# Application name: Ads
# Homepage Url: http://localhost:8000
# Application Description: Whatever
# Authorization callback URL: http://127.0.0.1:8000/oauth/complete/github/


# Using PythonAnywhere here are some settings:

# Application name: ChuckList PythonAnywhere
# Homepage Url: https://sheldonlee.pythonanywhere.com
# Application Description: Whatever
# Authorization callback URL: https://sheldonlee.pythonanywhere.com/oauth/complete/github/

# Also on PythonAnywhere, go into the Web tab and enable "Force HTTPS"
# so you don't get a redirect URI mismatch.

# Then copy the client_key and secret to this file


# # My local
# SOCIAL_AUTH_GITHUB_KEY = 'e18d77f2a18fca2fb1ce'    # read above and setting github, copy from github
# SOCIAL_AUTH_GITHUB_SECRET = '7ce99885d987e293930fce93ad5d731c9a033370'    # copy from github

# My PythonAnywhere
SOCIAL_AUTH_GITHUB_KEY = 'c53a3b9e39a55a8e459f'
SOCIAL_AUTH_GITHUB_SECRET = '0a121d649b17afcf3894ef3b03c68ad0a9cba2a9'
