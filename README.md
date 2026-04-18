# Instagram DM Notifier

Desktop notifications for Instagram Direct Messages on macOS.

## Who is this for
I kept noticing how easily Instagram Reels would eat up my time without me realizing it. I tried deleting the app a few times, but then I didn't get any notifications of my DMs either. DMs notifications are quite important me so I used to end up installing the app again in a few days.

Couldn’t find a simple fix for this tradeoff, so I built one.

This script sends macOS native notifications for Instagram DMs, so you can stay off the app but still be reachable. If you’ve faced something similar, this might help.

## Setup

### 1. Clone and enter the folder. Make sure to run the program in the home directory.
```bash
cd $HOME
git clone https://github.com/Holmes7/ig-dm-notifier.git
cd instadm
```

### 2. Create virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Add your Instagram credentials
```bash
cp sample.env .env
```

Open `.env` in a text editor and add your Instagram username and password:
```
INSTAGRAM_USERNAME=your_username
INSTAGRAM_PASSWORD=your_password
```

### 5. Copy plist file to LaunchAgents folder
```bash
mkdir -p ~/Library/LaunchAgents
cp com.instagram.notifier.plist ~/Library/LaunchAgents/
```

### 6. Load the service (auto-starts on login)
```bash
launchctl load ~/Library/LaunchAgents/com.instagram.notifier.plist
```

### 7. Start immediately
```bash
launchctl start com.instagram.notifier
```

## How to Manage

### Check if running
```bash
launchctl list | grep instagram
```

### Stop the service
```bash
launchctl unload ~/Library/LaunchAgents/com.instagram.notifier.plist
```

### Restart the service
```bash
launchctl unload ~/Library/LaunchAgents/com.instagram.notifier.plist
launchctl load ~/Library/LaunchAgents/com.instagram.notifier.plist
launchctl start com.instagram.notifier
```

## Notes

- Notification interval: ~2 minutes by default
- Edit `POLL_INTERVAL` in `main.py` to adjust frequency

If you face any issues feel free to DM me on any of my social handles.
