from replies.replier import CommandReplier
from models.models import TeacherUser
from botapp import database as db, BotSettings


class IamTeacherReplier(CommandReplier):
    __nameinputpattern__ = "\n\nНапиши отак:\n/name Ім'я Прізвище"
    reply = f"Здається, щось пішло не так. Чогось не вистачає."

    def __init__(self, update):
        super().__init__(update)
        if self.registered and len(self.msg_attributes) == 1:
            school_token = self.msg_attributes[0]
            if ("S" or "T") not in self.usertype and school_token == BotSettings.SCHOOL:
                self.register_teacher()
                self.reply = "Вітаю нового вчителя!"
            else:
                self.reply = "Я тобі не вірю!"
        elif not self.registered:
            self.reply = f"Давай спершу позайомимось!{self.__nameinputpattern__}"
        elif "T" in self.usertype:
            self.reply = f'Так, я знаю, що Ви - вчитель!'

    def register_teacher(self):
        """
        Creates new record in 'teachers' table binded to user
        :return:
        """
        teacher = TeacherUser()
        teacher.user_id = self.profile.id
        self.profile.type = "T"
        db.session.add(teacher)
        db.session.commit()
