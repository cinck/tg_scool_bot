from replies.replier import CommandReplier
from models.models import TeacherUser, StudentUser, Schedule, Group, Lesson, Course, Timetable
from botapp import database as db
from utils.utils import collect_info


class MyScheduleReplier(CommandReplier):
    reply = f"Здається, щось пішло не так."

    def __init__(self, update):
        super().__init__(update)

        if self.registered:
            if 'T' in self.usertype:
                self.reply = self.get_teacher_schedule()
            elif 'S' in self.usertype:
                self.my_group_id = db.session.query(Group).filter(Group.student == self.profile.id).first().id
                self.reply = self.get_group_schedule()
            elif 'X' in self.usertype:
                self.reply = (f"Розклад вчителя:\n{self.get_teacher_schedule()}\n"
                              f"Розклад учня:\n{self.get_group_schedule()}")

    def get_teacher_schedule(self):
        yearly_schedule = db.session.query(Timetable).filter_by(year=2023)

        schedule = {}
        for w in range(1, yearly_schedule.count()):
            weekly_schedule = yearly_schedule.filter_by(week_no=w)
            for d in range(1, weekly_schedule.count()):
                daily_schedule = weekly_schedule.filter_by(weekday_no=d)
                for l in range(1, daily_schedule.count()):
                    lessons = daily_schedule.join(Schedule).join(Course)
                    lesson = lessons.filter(Course.teacher == self.profile.id).first()
                    schedule[w[d[l]]] = f"{l}. {lesson.course.group} {lesson.course} {lesson.theme}"

        return collect_info(schedule)

    def get_group_schedule(self):
        yearly_schedule = db.session.query(Timetable).filter_by(year=2023)

        schedule = {}
        for w in range(1, yearly_schedule.count()):
            weekly_schedule = yearly_schedule.filter_by(week_no=w)
            for d in range(1, weekly_schedule.count()):
                daily_schedule = weekly_schedule.filter_by(weekday_no=d)
                for l in range(1, daily_schedule.count()):
                    lesson = daily_schedule.join(Schedule).join(Group).filter(Group.id == self.my_group_id).first()
                    schedule[w[d[l]]] = f"{l}. {lesson.course} {lesson.theme}"

        return collect_info(schedule)
