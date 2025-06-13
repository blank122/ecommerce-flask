from ..extensions import db
from ..models import Account

def get_all_accounts():
    try:
        accounts = db.query(Account.email).all()
        return [email for (email,) in accounts]
    finally:
        db.close()
