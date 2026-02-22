# System Stats Dashboard

A live terminal dashboard for macOS that displays CPU, RAM, and disk usage with progress bars. Refreshes every 2 seconds.

## Screenshot

```
┌─────────────────────────────────────────────────────┐
│              System Stats Dashboard                  │
├─────────────────────────────────────────────────────┤
│ CPU   43%  ████████████░░░░░░░░░░░░░░░░  43.0%      │
│ RAM   61%  ████████████████░░░░░░░░░░░░  9.8 GB / 16 GB │
│ Disk  80%  ████████████████████░░░░░░░░  716 GB / 926 GB │
│                                                      │
│       uptime 2d 4h 12m  •  press ctrl+c to quit      │
└─────────────────────────────────────────────────────┘
```

## Requirements

- Python 3.8+
- macOS (also works on Linux)

## Setup

```bash
git clone https://github.com/gsealander/system-stats-dashboard.git
cd system-stats-dashboard
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

```bash
source venv/bin/activate   # if not already active
python3 dashboard.py
```

Press `ctrl+c` to quit.
