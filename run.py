from app import app
import os
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Default to 5000 if PORT not set
    app.run(host='0.0.0.0', port=port)  # Bind to 0.0.0.0
