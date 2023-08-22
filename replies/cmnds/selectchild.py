from replies.replier import CommandReplier
from models.models import ParentUser, StudentUser, ParentBinding, User
from botapp import database as db


class SelectChildReplier(CommandReplier):
    reply = f"Здається, щось пішло не так."

    def __init__(self, update):
        super().__init__(update)
        if self.registered and "P" in self.usertype:
            self.parent = db.session.query(ParentUser).filter_by(user_id=self.profile.id).first()
            self.selected_student_id = self.parent.selected_student
            if len(self.params) == 2:
                select_id = self.params[1]
                self.set_student_selection(select_id)

            elif len(self.params) == 1:
                self.reply = f"Поточний вибір:\n"
                if selection := db.session.query(User).filter_by(id=self.selected_student_id).first():
                    self.reply += f"{selection.first_name} {selection.last_name}\n\n"
                else:
                    self.reply += "- не вибрано -\n\n"

                self.reply += f"Ваші діти:\n\n{self.get_children()}"

    def set_student_selection(self, select_id):
        student = db.session.query(ParentBinding).filter_by(student_id=select_id).first()
        if not student:
            self.reply = "Такого учня не існує"
        else:
            self.parent.selected_student = student.student_id
            db.session.commit()
            self.reply = "Вибір зроблено"

    def get_children(self):
        reply = ""
        children = db.session.query(User).join(StudentUser).join(ParentBinding).filter_by(parent_id=self.parent.user_id)
        for c in children:
            reply += f"{c.first_name} {c.last_name}\n вибрати - /selectchild_{c.id}\n\n"
        return reply
