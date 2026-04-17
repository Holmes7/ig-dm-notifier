# Instagram DM Notifier

Desktop notifications for Instagram Direct Messages on macOS.

## Features

- Real-time monitoring of Instagram DMs
- Native macOS notifications
- Automatic re-login on session expiry

## Setup

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd instadm
   ```

2. **Create virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure credentials**
   ```bash
   cp sample.env .env
   # Edit .env with your Instagram username and password
   ```

5. **Run**
   ```bash
   python main.py
   ```

## Notes

- Notification interval: ~2 minutes by default
- Edit `POLL_INTERVAL` in `main.py` to adjust frequency
