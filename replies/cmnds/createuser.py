from replies.replier import CommandReplier
from models.models import User
from botapp import database as db
from utils.utils import get_token


class CreateUserReplier(CommandReplier):
    __inputpattern__ = "\n\nНапиши отак:\n/name Ім'я Прізвище"
    reply = f"Здається, щось пішло не так.{__inputpattern__}"

    def __init__(self, update):
        super().__init__(update)
        if self.registered:
            self.reply = f"{self.username}, ми вже знайомились раніше."
        else:
            if not self.msg_attributes:
                self.reply = f"Вибач, не розчув...{self.__inputpattern__}"
            elif len(self.msg_attributes) == 1:
                self.reply = f"Це ім'я чи приізвище?{self.__inputpattern__}"
            elif len(self.msg_attributes) > 2:
                self.reply = f"Ой, я стільки багато не запам'ятаю.{self.__inputpattern__}"
            else:
                self.__create_user__()
                if self.get_profile():
                    self.reply = f"Радий знайомству!"

    def __create_user__(self):
        user = User()
        user.first_name = self.msg_attributes[0].capitalize()
        user.last_name = self.msg_attributes[1].capitalize()
        user.tg_id = self.u_id
        user.binder = get_token(User)
        db.session.add(user)
        db.session.commit()

