from botapp import database as db
from models.models import TeacherUser, TeacherSubjectBinder as TsB, Subject

class TeachersList:

    reply = "Sorry! Can't do that for you."

    def __init__(self):
        self.tl = db.session.query(TeacherUser)
        t_list = []
        for t in self.tl:
            subjects = db.session.query(TsB).join(Subject)
            subjects.filter(TsB.teacher_id == t.id)
            sl = ""
            for s in subjects:
                sl += f'    {s.subjects.title}\n'
            t_list.append(f'{t.first_name} {t.last_name}:\n{sl}')
        self.reply = '\n'.join(t_list)

