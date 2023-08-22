from replies.replier import CommandReplier
from botapp import database as db, BotSettings
from models.models import User


class ListUsersReplier(CommandReplier):

    def __init__(self, update):
        super().__init__(update)
        if self.registered and 'X' in self.usertype:
            self.reply = self.list_users()

    def list_users(self):
        lst = db.session.query(User).all()
        reply_text = "Всі користувачі:\n\n"
        for user in lst:
            reply_text += f"{user.id}. {user.first_name} {user.last_name}, {user.type}\n"
        return reply_text
