from telegram import Update
from botapp import database as db
from models.models import User, ParentUser
from utils.utils import get_token


class Replier:
    reply = 'Reply text'
    username = 'Незнайомцю'
    registered = False

    def __init__(self, update: Update):
        self.u_id = update.effective_chat.id
        self.message = update.effective_message
        self.msg_text: str = self.message.text
        self.msg_decomposed = self.msg_text.split(" ")
        self.msg_attributes = self.msg_text.split(' ')[1:]
        self.profile = self.get_profile()
        if self.profile:
            self.registered = True
            self.username = self.profile.username
            self.usertype = self.profile.type
            if 'P' in self.usertype:
                self.parent = db.session.query(ParentUser).filter_by(user_id=self.profile.id).first()
            if self.usertype == 'X':
                self.username = 'Господарю'

    def get_profile(self):
        return db.session.query(User).filter(User.tg_id == self.u_id).first()


class CommandReplier(Replier):

    def __init__(self, update):
        super().__init__(update)
        self.command = self.msg_decomposed[0]
        self.params = self.command.split('_')
        self.msg_attributes = self.msg_decomposed[1:]


class MessageReplier(Replier):
    reply = ("Вітаю, Незнайомцю!\n"
             "Як я можу тебе називати?\n\n"
             "Напиши мені:\n\"Зви мене Ім'я Прізвище\"\n\n"
             "Наприклад:\n"
             "\"Зви мене Люк Скайвокер\"\n\n"
             "і я запам'ятаю тебе.")

    def __init__(self, update):
        super().__init__(update)
        if self.registered:
            self.reply = (
                f"Вітаю, {self.username}\nЯ поки що вмію лише виконувати команди.\n"
                "Команди - це повідомлення, які починаються значком '/' з командним словом наприклад '/help'.\n"
                "Список доступних команд є у меню, що ліворуч поля, де ти друкуєш повідомлення.\n"
                "Команди у моїх повідомленнях зазвичай підсвічуються синім "
                "і на них можна натискати, щоб вони виконувались."
            )

        if len(self.msg_decomposed) > 2 and " ".join(self.msg_decomposed[:2]).lower() == 'зви мене':
            self.register()
        elif " ".join(self.msg_decomposed[:2]).lower() == 'зви мене' and len(self.msg_decomposed) < 3:
            self.reply = "Щось пішло не так. Спробуй написати подібно такому:\n\nЗви мене Люк Скайвокер "

    def register(self):
        if not self.registered:
            user = User()
            user.username = " ".join(self.msg_decomposed[2:])
            user.tg_id = self.u_id
            user.binder = get_token(User)
            db.session.add(user)
        else:
            self.profile.username = " ".join(self.msg_decomposed[2:])
        db.session.commit()
        self.reply = f"Тепер я зватиму тебе {self.profile.username}."
