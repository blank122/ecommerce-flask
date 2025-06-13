from ..models.account import Account

def get_all_accounts():
    try:
        accounts = Account.query.with_entities(Account.email).all()
        return [email for (email,) in accounts]
    except Exception as e:
        print(f"❌ DB Error in get_all_accounts: {e}")
        return []
