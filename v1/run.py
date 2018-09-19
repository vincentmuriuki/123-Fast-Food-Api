import os
from app import create_app

config = os.getenv("CONFIG_STAGE") or "default"
app=create_app(config)

if __name__ == '__main__':
    app.run(debug=True)
