from botapp import database as db
from models.models import TeacherUser, ParentUser, StudentUser
# from bot_settings import BotSettings
# from telegram import Update


class Registrator:

    reply = 'Failed to register'

    def __init__(self, message):
        self.message = message
        self.message_text = message.text.replace('/register', '')
        self.attributes = self.message_text.split()
        if self.__validate__():
            self.__create_user__()

    def __validate__(self):
        if not self.message.chat.type == 'private':
            return False
        if not len(self.attributes) == 3:
            return False
        if not self.attributes[0].lower() in 'tsp':
            return False
        return True

    def __create_user__(self):
        user_type = self.attributes[0]
        first_name = self.attributes[1].capitalize()
        last_name = self.attributes[2].capitalize()

        if user_type == 't':
            user = TeacherUser()
        elif user_type == 's':
            user = StudentUser()
        elif user_type == 'p':
            user = ParentUser()
        else:
            self.reply = 'Invalid user type.'
            return

        user.first_name = first_name
        user.last_name = last_name
        db.session.add(user)
        db.session.commit()
        self.reply = f'User: {first_name} {last_name} created successfully.'









