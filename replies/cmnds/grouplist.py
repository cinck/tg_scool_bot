from replies.replier import CommandReplier
from botapp import database as db
from models.models import Group, AssignedCourse, TeacherUser, Course, StudentUser, User


class GroupListReplier(CommandReplier):
    reply = 'Щось пішло не туди'
    parameters = {'grouplist': None}

    def __init__(self, update):
        super().__init__(update)
        print(self.params)
        if self.registered:
            print("Registered ok")
            if ("X" or "T") in self.usertype:
                print("Usertype ok")
                self.group_id = self.get_group_id()
                if self.group_id:
                    print("group_id ok")
                    self.reply = self.list_students()

    def get_group_id(self):
        # group_id = None
        group_id = self.params[1]
        # try:
        #     print(self.params[1])
        #     group_id = self.params[1]
        # except Exception as e:
        #     self.reply = f'Виникла проблема {e}. Група не вибрана'

        return group_id

    def list_students(self):

        s_list = db.session.query(User).join(StudentUser).filter_by(group=self.group_id)
        group = db.session.query(Group).filter_by(id=self.group_id).first()
        reply = f"{group.grade}-{group.letter}. Список учнів:\n\n"

        if s_list.count() < 1:
            return reply + "- немає жодного учня -"

        n = 0
        for s in s_list.order_by(User.last_name):
            n += 1
            reply += f"{n}. {s.first_name} {s.last_name}\n"

        return reply

