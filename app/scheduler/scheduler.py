from ..utils.mail_service import send_deal_email
from ..repo.db import get_all_accounts
from apscheduler.schedulers.background import BackgroundScheduler
import os
import json
import random


DEALS = [
  {
    "id": 1,
    "title": "50% Off Designer Frames",
    "description": "Get half off on selected designer eyeglass frames this week only!"
  },
  {
    "id": 2,
    "title": "Free Eye Exam with Purchase",
    "description": "Enjoy a complimentary eye exam when you purchase any complete pair of glasses."
  },
  {
    "id": 3,
    "title": "Back to School Promo",
    "description": "Students get 20% off on all prescription eyeglasses until September!"
  },
  {
    "id": 4,
    "title": "Buy 1, Get 1 Free",
    "description": "Buy one pair of eyeglasses and get the second pair FREE. Limited time only!"
  },
  {
    "id": 5,
    "title": "Father’s Day Special",
    "description": "Dads get 30% off on all eyeglasses this Father’s Day weekend!"
  },
  {
    "id": 6,
    "title": "Clearance Sale",
    "description": "Up to 70% off on last season’s frames while supplies last."
  },
  {
    "id": 7,
    "title": "Free Lens Upgrade",
    "description": "Get a free lens coating upgrade with every new frame purchase."
  },
  {
    "id": 8,
    "title": "Kids' Glasses at 15% Off",
    "description": "Protect their vision! Get 15% off on all kids' eyeglasses this month."
  },
  {
    "id": 9,
    "title": "UV Protection Special",
    "description": "Free UV protection coating on all lenses ordered this week."
  },
  {
    "id": 10,
    "title": "Senior Citizen Discount",
    "description": "All seniors 60+ receive 25% off their total bill every Tuesday!"
  },
  {
    "id": 11,
    "title": "Referral Reward",
    "description": "Refer a friend and get P200 off your next purchase."
  },
  {
    "id": 12,
    "title": "New Year, New Vision",
    "description": "Start the year right with 20% off all eyewear."
  },
  {
    "id": 13,
    "title": "Anniversary Week Sale",
    "description": "Celebrate with us! Up to 40% off everything in-store."
  },
  {
    "id": 14,
    "title": "Eyeglass + Sunglass Combo",
    "description": "Buy eyeglasses, get 50% off prescription sunglasses."
  },
  {
    "id": 15,
    "title": "Free Frame Fitting",
    "description": "Enjoy professional frame fitting with every pair purchased."
  },
  {
    "id": 16,
    "title": "End of Month Flash Sale",
    "description": "Flash sale: 30% off all lenses for the next 48 hours!"
  },
  {
    "id": 17,
    "title": "Women's Month Special",
    "description": "Ladies enjoy 25% off all pink and red frame styles."
  },
  {
    "id": 18,
    "title": "Anti-Blue Light Bundle",
    "description": "Buy a pair with anti-blue light lenses and get a FREE lens cleaner!"
  },
  {
    "id": 19,
    "title": "Weekend Walk-In Discount",
    "description": "Walk-ins every Saturday get an instant 15% discount!"
  },
  {
    "id": 20,
    "title": "2-in-1 Deal",
    "description": "Get 2 pairs of glasses for only P1,999. Styles may vary."
  },
  {
    "id": 21,
    "title": "Loyalty Card Launch",
    "description": "Sign up for our loyalty card and get instant 10% off your first purchase."
  },
  {
    "id": 22,
    "title": "Corporate Partner Discount",
    "description": "Employees of our partner companies get 20% off on eyewear."
  },
  {
    "id": 23,
    "title": "Birthday Bonus",
    "description": "Come in on your birthday month and receive a special gift and 20% off!"
  },
  {
    "id": 24,
    "title": "Frame Trade-In",
    "description": "Trade in your old frames and get P300 off your new pair."
  },
  {
    "id": 25,
    "title": "Holiday Glow Special",
    "description": "Festive sale: Get up to 50% off on holiday-themed frames."
  },
  {
    "id": 26,
    "title": "Lens Subscription Promo",
    "description": "Sign up for our lens care plan and get 2 free cleanings per year!"
  },
  {
    "id": 27,
    "title": "Rainy Day Deal",
    "description": "Come in when it rains and get 10% off just for showing up!"
  },
  {
    "id": 28,
    "title": "Early Bird Discount",
    "description": "First 10 customers daily get P100 off their bill."
  },
  {
    "id": 29,
    "title": "Clear Vision Package",
    "description": "Package deal: Eye exam + glasses starting at P1,299."
  },
  {
    "id": 30,
    "title": "Social Media Follower Perk",
    "description": "Follow us on social media and get an exclusive 5% discount coupon!"
  }
]

def assign_and_send_deals():
    print("🔁 Running scheduled job...")
    try:
        accounts = get_all_accounts()

        if not DEALS:
            print("⚠️ No deals found. Skipping email sending.")
            return

        if not accounts:
            print("⚠️ No accounts found. Skipping email sending.")
            return

        for email in accounts:
            deal = random.choice(DEALS)
            try:
                send_deal_email(deal, "🔥 Your Brand Deal", email)
                print(f"✅ Deal sent to {email}")
            except Exception as e:
                print(f"❌ Failed to send email to {email}: {e}")
    except Exception as e:
        print(f"❌ Error in assign_and_send_deals: {e}")

def start_scheduler(app, interval_minutes):
    scheduler = BackgroundScheduler()

    @scheduler.scheduled_job('interval', minutes=interval_minutes)
    def job():
        with app.app_context():
            assign_and_send_deals()

    scheduler.start()
    print(f"✅ Scheduler started! Sending deals every {interval_minutes} minute(s).")
