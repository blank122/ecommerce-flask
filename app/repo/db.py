from app.database.db import SessionLocal
from ..models import Account

def get_all_accounts():
    db = SessionLocal()
    try:
        accounts = db.query(Account.email).all()
        return [email for (email,) in accounts]
    finally:
        db.close()
