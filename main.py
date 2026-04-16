import json
import os
import random
import time

from dotenv import load_dotenv
from instagrapi import Client
from pync import Notifier

load_dotenv()  # take environment variables from .env.

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

USERNAME = os.getenv("INSTAGRAM_USERNAME")
PASSWORD = os.getenv("INSTAGRAM_PASSWORD")
SESSION_FILE = os.path.join(BASE_DIR, "ig_session.json")
SEEN_FILE = os.path.join(BASE_DIR, "ig_seen.json")

POLL_INTERVAL = 120  # seconds (recommended: 30–60)

cl = Client()


# -----------------------
# LOGIN
# -----------------------
def login():
    try:
        if os.path.exists(SESSION_FILE):
            cl.load_settings(SESSION_FILE)
            cl.login(USERNAME, PASSWORD)
        else:
            cl.login(USERNAME, PASSWORD)

        cl.dump_settings(SESSION_FILE)
        print("Logged in successfully")

    except Exception as e:
        print(f"Login failed: {e}")
        raise e


# -----------------------
# SEEN MESSAGE TRACKING
# -----------------------
def load_seen():
    try:
        return set(json.load(open(SEEN_FILE)))
    except:
        return set()


def save_seen(seen):
    json.dump(list(seen), open(SEEN_FILE, "w"))


# -----------------------
# NOTIFICATION
# -----------------------
def notify(sender, message):
    if len(message) > 120:
        message = message[:117] + "..."

    Notifier.notify(message, title=sender, subtitle="Instagram")


# -----------------------
# MESSAGE EXTRACTION
# -----------------------


def extract_message(item):
    item_type = item.get("item_type")

    # Handle explicit item types
    if item_type == "text":
        return item.get("text", "Text message")

    if item_type == "xma_clip" or item.get("clip"):
        return "🎬 Reel"

    if item_type == "xma_media_share":
        return "📸 Shared post"

    if item_type == "action_log":
        return "Reacted"


def check():
    seen = load_seen()

    try:
        result = cl.private_request(
            "direct_v2/inbox/",
            params={"persistentBadging": "true", "limit": "5"},
        )

        threads = result.get("inbox", {}).get("threads", [])
        item_types = set()  # Set to store all item_types
        for thread in threads:
            try:
                users = thread.get("users", [])
                user_map = {str(user["pk"]): user["username"] for user in users}
                items = thread.get("items", [])
                if not items:
                    continue

                title = thread.get("thread_title", "Someone")
                for item in items:
                    item_types.add(item.get("item_type"))
                    msg_id = str(item["item_id"])
                    sender_id = str(item.get("user_id"))
                    sender_name = user_map.get(sender_id, "Unknown")

                    if msg_id in seen or item.get("is_sent_by_viewer"):
                        break

                    seen.add(msg_id)

                    message = f"{sender_name}: {extract_message(item)}"

                    notify(title, message)
                    print(f"{title}: {message}")

            except Exception as te:
                print(f"Skipping thread: {te}")
                continue

    except Exception as e:
        print(f"Error fetching messages: {e}")
        print("Trying to re-login...")
        try:
            login()
        except Exception as re:
            print(f"Re-login failed: {re}")

    save_seen(seen)


# -----------------------
# RUN LOOP
# -----------------------
def main():
    print("Starting Instagram notifier...")
    login()

    while True:
        check()
        print(f"Checked. Sleeping {POLL_INTERVAL}s...\n")
        time.sleep(POLL_INTERVAL + random.randint(-20, 20))


if __name__ == "__main__":
    main()
