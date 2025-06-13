from flask import Flask, jsonify
from .extensions import db, jwt, mail
from .config import Config
from .routes.auth_routes import auth_bp
from sqlalchemy.exc import OperationalError
from sqlalchemy import text  # <-- add this import
from scheduler import start_scheduler
import time

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    jwt.init_app(app)
    mail.init_app(app) 

    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    
    if __name__ == "__main__":
        start_scheduler(interval_minutes=5)  # You can make this configurable

        try:
            while True:
                time.sleep(60)
        except KeyboardInterrupt:
            print("🛑 Scheduler stopped manually.")
            
    @app.route('/api/test-db')
    def test_db_connection():
        try:
            with db.engine.connect() as connection:
                connection.execute(text("SELECT 1"))  # wrap SQL in `text()`
            return jsonify({"message": "Database connection successful!"}), 200
        except OperationalError as e:
            return jsonify({"error": "Database connection failed", "details": str(e)}), 500
    
    return app
