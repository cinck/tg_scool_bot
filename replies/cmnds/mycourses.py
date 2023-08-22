from replies.replier import CommandReplier
from botapp import database as db
from models.models import Group, AssignedCourse, TeacherUser, Course, StudentUser, Subject, ParentUser


class MyCourseReplier(CommandReplier):

    reply = f"Список дисциплін:\n\n"

    def __init__(self, update):
        super().__init__(update)

        if self.registered:
            if "T" in self.usertype:
                self.reply += self.list_teacher_courses()
            if "S" in self.usertype or "P" in self.usertype:
                self.reply += self.list_student_courses()
            if "X" in self.usertype:
                self.reply += self.list_teacher_courses() + self.list_student_courses()
            # if "X" in self.usertype:
            #     self.reply = self.list_teacher_courses() + self.list_student_courses()

    def list_teacher_courses(self):
        courses = db.session.query(Course).join(AssignedCourse).filter_by(teacher=self.profile.id)
        reply = ""

        if not courses:
            return '- список порожній -'

        for c in courses.order_by(Course.grade):
            reply += (f"{c.grade} клас. {c.subject}: {c.course_name}\n"
                      f" - переглянути деталі:  /coursedetail_{c.id}\n\n")
        reply += "-------------\n\n"
        return reply

    def list_student_courses(self):
        courses = None
        student_id = self.profile.id
        if "P" in self.usertype:
            student_id = self.parent.selected_student
        group = db.session.query(Group).join(StudentUser).filter_by(user_id=student_id).first()
        reply = ""

        if group:
            courses = db.session.query(Course).join(AssignedCourse).filter_by(group_id=group.id)
        if not courses:
            return '- список порожній -'
        for c in courses:
            reply += (f"{c.course_name}\n"
                      f"  - оцінки:  /marks_course_{c.id}\n\n")
        reply += "-------------\n\n"
        return reply