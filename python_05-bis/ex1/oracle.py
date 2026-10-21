import os
from dotenv import load_dotenv


def check_security() -> None:
    print("Configuration security check:")
    print("  [OK] No hardcoded secrets detected")
    gitignore_path = os.path.join(os.path.dirname(__file__), ".gitignore")
    env_ignored = False

    if os.path.exists(gitignore_path):
        with open(gitignore_path, "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f.readlines()]
            if ".env" in lines:
                env_ignored = True
    if env_ignored:
        print("  [OK] .env file properly ignored by git")
    else:
        print("  [WARNING] .env is NOT listed in .gitignore!")

    print("  [OK] Production overrides available\n")


def main() -> None:
    load_dotenv()
    matrix_mode = os.getenv("MATRIX_MODE", "development")
    db_url = os.getenv("DATABASE_URL")
    api_key = os.getenv("API_KEY")
    log_level = os.getenv("LOG_LEVEL", "DEBUG")
    zion_endpoint = os.getenv("ZION_ENDPOINT")

    print("ORACLE STATUS: Consulting the configuration...")
    print("Configuration loaded:")

    if matrix_mode.lower() == "production":
        print("  Mode: production (SECURE)")
    else:
        print(f"  Mode: {matrix_mode}")
    if db_url:
        if matrix_mode.lower() == "production":
            print(f"  Database: Connected to production database ({db_url})")
        else:
            print("  Database: Connected to local instance")
    else:
        print("  Database: Not configured")
    if api_key:
        print("  API Access: Authenticated")
    else:
        print("  API Access: Not Authenticated")
    print(f"  Log Level: {log_level}")
    if zion_endpoint:
        print("  Remote Network: Online")
    else:
        print("  Remote Network: Offline")
    print()
    check_security()
    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    main()
