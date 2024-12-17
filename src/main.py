import argparse
from auto_login_rpa.config import LoginConfig
from auto_login_rpa.login_bot import LoginBot

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="RPA Login Automation Tool")
    parser.add_argument(
        "--config", type=str, required=True, help="Path to the JSON configuration file"
    )
    args = parser.parse_args()

    # Load configuration
    try:
        config = LoginConfig.from_json(args.config)
    except Exception as e:
        print(f"Failed to load configuration: {e}")
        return

    # Run the bot
    bot = LoginBot(config)
    try:
        bot.setup_driver()
        if bot.login():
            print("Login successful!")
        else:
            print("Login failed!")
    finally:
        bot.close()

if __name__ == "__main__":
    main()
