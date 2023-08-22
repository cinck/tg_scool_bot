from replies.replier import CommandReplier
from botapp import database as db
from models.models import Group, AssignedCourse, TeacherUser, Course, Lesson, Subject


class CourseDetailReplier(CommandReplier):

    def __init__(self, update):
        super().__init__(update)

        if self.registered:
            if "X" in self.usertype or "T" in self.usertype:
                self.course_id = self.get_course_id()
                self.reply = self.get_course_data()

    def get_course_id(self):
        course_id = self.params[1]
        return course_id

    def get_course_data(self):
        course_data = db.session.query(Course).filter_by(id=self.course_id).join(AssignedCourse)
        my_course = course_data.filter_by(teacher=self.profile.id).first()
        subject = db.session.query(Subject).filter(Subject.id==my_course.subject).first()
        reply = (f"{subject}\n"
                 f"Курс: {my_course.course_name}. {my_course.grade} клас:\n\n")

        reply += "Класи: "
        groups = db.session.query(Group).join(AssignedCourse)
        my_groups = groups.filter_by(course_id=self.course_id, teacher=self.profile.id)
        for g in my_groups:
            reply += f"{g.grade}-{g.letter},"
        reply += "\n\n"

        reply += "Програма курсу:\n"
        lessons = db.session.query(Lesson).filter_by(course=self.course_id)
        n = 0
        for l in lessons:
            n += 1
            reply += f"{n}. {l.theme}\n"

        return reply
