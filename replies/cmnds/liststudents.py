from replies.replier import CommandReplier
from botapp import database as db, BotSettings
from models.models import Group, Course, StudentUser, User


class ListStudentsReplier(CommandReplier):

    def __init__(self, update):
        super().__init__(update)
        if self.registered and self.profile.admin:
            self.list_students()

    def list_students(self):
        self.reply = "Всі учні:\n"
        # todo: write function
        students = db.session.query(User).join(StudentUser)
        for s in students:
            self.reply += f"{s.first_name} {s.last_name}\n"


