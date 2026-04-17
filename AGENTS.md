# InstaDM

Instagram DM notifier for macOS (Python 3).

## Setup
- `python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt`
- Copy `sample.env` → `.env` and add `INSTAGRAM_USERNAME` / `INSTAGRAM_PASSWORD`

## Run
- `python main.py`

## Key Files
| File | Purpose |
|------|---------|
| `main.py` | Main app (154 lines) |
| `requirements.txt` | Dependencies |
| `sample.env` | Env template |
| `.env` | Credentials (gitignored) |
| `ig_session.json` | Login session (gitignored) |
| `ig_seen.json` | Message deduplication (gitignored) |
| `com.instagram.notifier.plist` | macOS LaunchAgent for background service |

## Important
- **macOS only** (uses `pync` for native notifications)
- `instagrapi` handles session persistence automatically
- `POLL_INTERVAL = 120` seconds in `main.py` (adjustable)
- No tests exist in this repo
