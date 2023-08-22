from replies.replier import CommandReplier
from botapp import database as db
from models.models import Group, AssignedCourse, TeacherUser, Course


class MyGroupReplier(CommandReplier):
    reply = "Список порожній"

    def __init__(self, update):
        super().__init__(update)

        if self.registered:
            if ("X" or "T") in self.usertype:
                self.reply = self.list_groups()

    def list_groups(self):
        groups = db.session.query(Group).join(AssignedCourse).filter_by(teacher=self.profile.id, complete=False)
        g_list = "Класи, в яких викладаєте:\n\n"
        for g in groups.order_by(Group.grade):
            g_list += f"{g.grade}-{g.letter}\n список класу - /grouplist_{g.id}\n\n"

        return g_list

