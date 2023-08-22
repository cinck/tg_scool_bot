import logging
from telegram.ext import ApplicationBuilder, MessageHandler
from telegram.ext.filters import BaseFilter
from bot_settings import BotSettings
from replies.msgs.messagereplier import msg_reply
from models.database import DataBase

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

database = DataBase(BotSettings.DATABASE)

if __name__ == '__main__':

    app = ApplicationBuilder().token(BotSettings.TOKEN).build()

    app.add_handler(MessageHandler(BaseFilter(), msg_reply))

    app.run_polling()

