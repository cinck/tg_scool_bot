from replies.replier import CommandReplier
from botapp import database as db
from models.models import Group, AssignedCourse, TeacherUser, Course, StudentUser, Mark, Lesson, ParentUser


class MarksReplier(CommandReplier):

    reply = f"Список дисциплін:\n\n"

    def __init__(self, update):
        super().__init__(update)

        if self.registered:

            if "S" in self.usertype or "X" in self.usertype:
                self.student_id = self.profile.id
            elif "P" in self.usertype:
                if self.parent:
                    self.student_id = self.parent.selected_student

            if len(self.params) == 3:
                self.reply = self.get_course_marks(course=self.params[2])
            # elif len(self.params) == 1:
            #     self.reply = self.get_all_marks()

    def get_course_marks(self, course):
        course_name = db.session.query(Course).filter_by(id=course).first().course_name
        reply = f"Оцінки {course_name}:\n"
        lessons = db.session.query(Lesson).filter_by(course=course)
        course_lessons = lessons.join(Mark).filter_by(student=self.student_id)
        if course_lessons.count() < 1:
            reply += " - оцінок немає - "
            return reply
        # reply += f"\n{}:\n"

        for lesson in course_lessons:
            reply += f"\n{lesson.theme}:\n"
            for mark in lesson.mark:
                reply += f"{mark}\n"

        return reply

    # def get_all_marks(self):
    #     reply = ""
    #     courses = db.session.query(AssignedCourse).join(Course).join(Group).filter_by(student=self.student_id)
    #     for course in courses:
    #
    #         marks = db.session.query(Mark).filter_by(student=self.student_id).join(Lesson).filter_by(course=course.course_id)
    #         course_marks = ""
    #         for mark in marks:
    #             course_marks += f"{mark.mark},"
    #
    #         reply += f"{course.course_name}:\n {course_marks}\n"
    #
    #     return reply
