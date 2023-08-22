from replies.replier import CommandReplier
from models.models import StudentUser, Group
from botapp import database as db
from utils.utils import get_token


class IamStudentReplier(CommandReplier):
    __nameinputpattern__ = "\n\nНапиши отак:\n/name Ім'я Прізвище"
    reply = f"Здається, щось пішло не так."

    def __init__(self, update):
        super().__init__(update)
        if self.registered and len(self.params) > 1:
            binder = self.params[1]
            self.group = db.session.query(Group).filter(Group.binder == binder).first()
            if "G" in self.usertype and self.group:
                self.register_student()
                self.reply = "Вітаю нового учня!"
            else:
                self.reply = "Я тобі не вірю!"
        elif not self.registered:
            self.reply = f"Давай спершу позайомимось!{self.__nameinputpattern__}"
        elif self.usertype == "S":
            self.reply = f'Так, я знаю, що ти учень!'

    def register_student(self):
        student = StudentUser()
        student.user_id = self.profile.id
        student.group = self.group.id
        student.binder = get_token(StudentUser)
        if self.profile.type == "G":
            self.profile.type = "S"
        db.session.add(student)
        db.session.commit()