import os
from app import create_app

app = create_app()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5001))
    debug = os.environ.get('FLASK_ENV') == 'development'
    
    if debug:
        print("Running in development mode with debugging enabled")
    else:
        print("Running in production mode")
        
    app.run(host='0.0.0.0', port=port, debug=debug)