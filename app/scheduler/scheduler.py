from ..utils.mail_service import send_deal_email
from ..repo.db import get_all_accounts
from apscheduler.schedulers.background import BackgroundScheduler
import json
import random

#load the deals.json 
def load_deals():
    with open('deals.json') as f:
        return json.load(f)

def assign_and_send_deals():
    print("🔁 Running scheduled job...")
    accounts = get_all_accounts()
    deals = load_deals()

    for email in accounts:
        deal = random.choice(deals)
        send_deal_email(email, deal)

def start_scheduler(interval_minutes=5):
    scheduler = BackgroundScheduler()
    scheduler.add_job(assign_and_send_deals, 'interval', minutes=interval_minutes)
    scheduler.start()
    print(f"✅ Scheduler started! Sending deals every {interval_minutes} minute(s).")