# Github_Streak

This Python script uses Selenium to log in to your GitHub account and fetch your current contribution streak from a third-party GitHub streak stats image.

##  Features

- Logs in to GitHub using your credentials securely via environment variables
- Uses a random user-agent to mimic real browser behavior
- Navigates to the contribution streak stats image and extracts the streak count

## Requirements

- Python 3.7+
- Google Chrome browser

### Python Packages:

```bash
pip install selenium webdriver-manager fake-useragent
```

# Setup
Set your GitHub login credentials & Telegram Bot and Chat id as environment variables

Linux/macOS

    export EMAIL="your_email@example.com"
    export PASS="your_password"
    export TOKEN="your_bot_token"
    export ID="your_chat_id"
    
Windows (CMD)

    set EMAIL=your_email@example.com
    set PASS=your_password
    set TOKEN="your_bot_token"
    set ID="your_chat_id"

Github Streak image

    driver.get("your_Streak_link")

Run the script:

    python github_Streak.py

# Output
The script will print your current GitHub login streak to the console
The Current Login Streak Is: 56
