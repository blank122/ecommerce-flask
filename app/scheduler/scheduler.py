from ..utils.mail_service import send_deal_email
from ..repo.db import get_all_accounts
from apscheduler.schedulers.background import BackgroundScheduler
import os
import json
import random

# Load the deals from the JSON file
def load_deals():
    try:
        # Get the absolute path to deals.json relative to this file
        deals_path = os.path.join(os.path.dirname(__file__), '..', '..', 'deals.json')
        with open(deals_path, 'r') as f:
            deals = json.load(f)
            if not isinstance(deals, list):
                raise ValueError("Expected a list of deals in deals.json")
            return deals
    except FileNotFoundError:
        print(f"❌ Error: deals.json file not found at path: {deals_path}")
    except json.JSONDecodeError as e:
        print(f"❌ Error decoding deals.json: {e}")
    except Exception as e:
        print(f"❌ Unexpected error while loading deals: {e}")
    return []

# Assign a random deal to each account and send it via email
def assign_and_send_deals():
    print("🔁 Running scheduled job...")
    try:
        accounts = get_all_accounts()
        deals = load_deals()

        if not deals:
            print("⚠️ No deals found. Skipping email sending.")
            return

        if not accounts:
            print("⚠️ No accounts found. Skipping email sending.")
            return

        for email in accounts:
            deal = random.choice(deals)
            try:
                send_deal_email(deal, "🔥 Your Brand Deal", [email])
                print(f"✅ Deal sent to {email}")
            except Exception as e:
                print(f"❌ Failed to send email to {email}: {e}")
    except Exception as e:
        print(f"❌ Error in assign_and_send_deals: {e}")

def start_scheduler(app, interval_minutes=5):
    scheduler = BackgroundScheduler()

    @scheduler.scheduled_job('interval', minutes=interval_minutes)
    def job():
        with app.app_context():
            assign_and_send_deals()

    scheduler.start()
    print(f"✅ Scheduler started! Sending deals every {interval_minutes} minute(s).")
