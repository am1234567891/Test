import os

# *****************************
# Environment specific settings
# *****************************

# DO NOT use "DEBUG = True" in production environments
DEBUG = True

# DO NOT use Unsecure Secrets in production environments
# Generate a safe one with:
#     python -c "import os; print repr(os.urandom(24));"
SECRET_KEY = 'This is an UNSECURE Secret. CHANGE THIS for production environments.'

# SQLAlchemy settings
SQLALCHEMY_DATABASE_URI = 'sqlite:///../app.sqlite'
SQLALCHEMY_TRACK_MODIFICATIONS = False    # Avoids a SQLAlchemy Warning

# Flask-Mail settings
# For smtp.gmail.com to work, you MUST set "Allow less secure apps" to ON in Google Accounts.
# Change it in https://myaccount.google.com/security#connectedapps (near the bottom).
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USE_TLS = False
MAIL_USERNAME = 'cifwebdev@gmail.com'
MAIL_PASSWORD = 'cifun@CA20'
MAIL_DEFAULT_SENDER = 'cifwebdev@gmail.com'

# Sendgrid settings
SENDGRID_API_KEY='place-your-sendgrid-api-key-here'

# Flask-User settings
USER_APP_NAME = "Web GUI Design"  # Shown in and email templates and page footers
USER_ENABLE_EMAIL = True  # Enable email authentication
USER_ENABLE_USERNAME = False  # Disable username authentication
USER_EMAIL_SENDER_NAME = USER_APP_NAME
USER_EMAIL_SENDER_EMAIL = "noreply@example.com"
USER_REQUIRE_RETYPE_PASSWORD = True  # Enable retype password

ADMINS = [
    '"Admin One" <admin1@gmail.com>',
    ]
