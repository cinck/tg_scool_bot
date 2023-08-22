from botapp import database as db
from models.models import Group, Grade
from replies.replier import CommandReplier
from utils.utils import get_token


class NewGroup(CommandReplier):
    parameters = {'grade': None, 'letter': None}
    reply = "Something went wrong"
    grades = range(11)
    letters = {
        "1": "А",
        "2": "Б",
        "3": "В",
        "4": "Г",
        "5": "Д"
    }
    def __init__(self,update):
        super().__init__(update)
        self.params = self.command.split('_')
        self.set_params()
        self.group_grade = self.parameters.get('grade')
        self.group_letter = self.parameters.get('letter')
        if not self.group_grade:
            self.reply = self.select_grade_reply()
        elif not self.group_letter:
            self.reply = self.select_letter_reply()
        elif self.group_grade and self.group_letter:
            self.create_group()
            self.reply = f"Новий клас створено."

    def set_params(self):
        for p in self.params:
            for k in self.parameters.keys():
                if k in p:
                    self.parameters[k] = p.replace(k, "")

    def create_group(self):
        group = Group()
        group.grade = self.group_grade
        group.letter = self.letters.get(self.group_letter)
        group.binder = get_token(Group)
        db.session.add(group)
        db.session.commit()

    def select_grade_reply(self):
        reply = f"Виберіть клас:\n\n"
        # grades = db.session.query(Grade).all()
        for grade in range(1, 11):
            reply += f"{grade}-й клас - {self.command}_grade{grade}\n"

        return reply

    def select_letter_reply(self):
        reply = f"Виберіть літеру:\n\n"
        for k, l in self.letters.items():
            reply += f"{l} - {self.command}_letter{k}\n"

        return reply
