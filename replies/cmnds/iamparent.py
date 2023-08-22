from replies.replier import CommandReplier
from models.models import ParentUser, StudentUser, ParentBinding
from botapp import database as db


class IamParentReplier(CommandReplier):
    reply = f"Здається, щось пішло не так."

    def __init__(self, update):
        super().__init__(update)

        if self.registered and len(self.msg_attributes) == 1:
            binder = self.msg_attributes[0]
            self.student = db.session.query(StudentUser).filter(StudentUser.binder == binder).first()
            self.bound = self.binding()
            if self.usertype != "S" and self.student and not self.bound:
                self.bind_parent()
                student_name = f"{self.student.user_id.first_name} {self.student.user_id.last_name}"
                self.reply = f"Тепер Ви можете дізнаватися про успіхи в навчанні {student_name}."

            elif self.bound:
                self.reply = f"Цей зв'язок вже існує."

            elif not self.student:
                self.reply = "У нас немає такого учня!"

        elif not self.registered:
            self.reply = f"Давай спершу познайомимось!"



    def bind_parent(self):
        parent = ParentUser()
        binding = ParentBinding()
        binding.parent_id = parent.user_id = self.profile.id
        binding.student_id = self.student.user_id

        if 'P' not in self.usertype and 'G' not in self.usertype:
            self.profile.type += '+P'
        elif 'G' in self.usertype:
            self.profile.type = 'P'
        db.session.add(parent)
        db.session.add(binding)
        db.session.commit()

    def binding(self):
        q = db.session.query(ParentBinding)
        binding = q.filter_by(student_id=self.student.user_id, parent_id=self.profile.id).first()
        return binding
