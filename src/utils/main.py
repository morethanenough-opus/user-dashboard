import os
from user_dashboard.config import config
from user_dashboard.app import create_app

if __name__ == '__main__':
    app = create_app(config)
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)