from dotenv import load_dotenv
import os

load_dotenv()

from app import create_app

app = create_app()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(debug=os.getenv("FLASK_DEBUG") == "True", host="0.0.0.0", port=port)