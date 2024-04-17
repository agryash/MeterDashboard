import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    """Configuration class for the Flask application."""
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'meter_data.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False