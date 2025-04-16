from flask import Flask
from app.config import config
import os

def create_app(config_name=None):
    """Application factory function"""
    app = Flask(__name__)
    
    # Configure the app
    if config_name is None:
        config_name = os.environ.get('FLASK_ENV', 'production')
    
    app.config.from_object(config[config_name])
    
    # Register blueprints
    from app.routes import bp as main_bp
    app.register_blueprint(main_bp)
    
    return app