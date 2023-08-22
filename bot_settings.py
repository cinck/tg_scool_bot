from dotenv import load_dotenv
import os

load_dotenv()


class BotSettings:
    TOKEN = os.getenv("TOKEN")
    BOT_USERNAME = os.getenv("BOT_USERNAME")
    DATABASE = os.getenv('DB_NAME')
    SCHOOL = os.getenv('SCHOOL')
    ADMIN_PASS = os.getenv('ADMIN_PASS')
    SU_PASS = os.getenv('SU_PASS')
