from sqlalchemy import Column, Integer, SmallInteger, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from botapp import database as db


class User(db.ModelBase):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    patronimic = Column(String)
    birth_date = Column(String)
    type = Column(String, default='G')               # [T]eacher, [S]tudent, [P]arent, [G]uest, [X]-superuser
    admin = Column(Boolean, default=False)
    phone = Column(String)
    email = Column(String)
    binder = Column(String, unique=True)
    tg_id = Column(Integer, unique=True)
    teacher = relationship('TeacherUser')
    student = relationship('StudentUser')
    parent = relationship('ParentUser')

    def get_types(self):
        types = {
            'T': 'вчитель',
            'S': 'учень',
            'P': 'батьківство',
            'G': 'гість',
            'X': 'superuser'
        }
        sts = []
        for t in self.type:
            if s := types.get(t):
                sts.append(s)
        return " ,".join(sts)

    def get_user_data(self):
        general_data = {
            "Користувач": self.username,
            "Ім'я": f"{self.first_name} {self.last_name}",
            "По батькові": self.patronimic,
            "День народження": self.birth_date,
            "Телефон": self.birth_date,
            "Пошта": self.email,
            "Статус": self.get_types()
        }
        return general_data

    def get_teacher_data(self):

        t_data = db.session.query(TeacherUser).filter_by(user_id=self.id).first()
        subjects = db.session.query(Subject).join(TeacherSubjectBinder).filter(TeacherSubjectBinder.teacher_id==self.id)
        subs = ""
        for s in subjects:
            subs += f"{s}, "
        if not t_data:
            return None
        teacher_data = {
            "Предмети": subs[:-2],
            "Кабінет": t_data.classroom,
            "Кураторство": t_data.lead_group
        }
        return teacher_data

    def get_parent_data(self):
        bound_students = db.session.query(User).join(StudentUser).join(ParentBinding).filter_by(parent_id=self.id)
        if not bound_students:
            return None
        student_names = ""
        for s in bound_students:
            student_names += f"{s.first_name} {s.last_name}\n"
        parent_data = {
            'Діти': student_names
        }
        return parent_data

    def get_student_data(self):
        s_data = db.session.query(Group).join(StudentUser).filter(StudentUser.user_id == self.id).first()
        if not s_data:
            return None
        student_data = {
            'Група': f"{s_data.grade}-{s_data.letter}"
        }
        return student_data


class TeacherUser(db.ModelBase):
    __tablename__ = 'teachers'

    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    subject = relationship('TeacherSubjectBinder')
    classroom = Column(String, ForeignKey('classrooms.id'))
    lead_group = Column(Integer, ForeignKey('groups.id'))
    assigned_course = relationship('AssignedCourse')

    def __repr__(self):
        return f"{self.first_name} {self.patronimic} {self.last_name}"


class TeacherStateSelector(db.ModelBase):
    __tablename__ = 't_selectors'

    teacher_id = Column(Integer, ForeignKey('teachers.user_id'), primary_key=True)
    course = Column(Integer, ForeignKey('courses.id'))
    group = Column(Integer, ForeignKey('groups.id'))
    lesson = Column(Integer, ForeignKey('lessons.id'))
    student = Column(Integer, ForeignKey('students.user_id'))


class ParentUser(db.ModelBase):
    __tablename__ = 'parents'

    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    student = relationship('ParentBinding')
    selected_student = Column(Integer)

    def __init__(self, first_name: str = '', last_name: str = ''):
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return f"{self.first_name} {self.patronimic} {self.last_name}"


class StudentUser(db.ModelBase):
    __tablename__ = 'students'

    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    group = Column(Integer, ForeignKey("groups.id"))
    parent = relationship('ParentBinding')
    binder = Column(String, default='')
    mark = relationship('Mark')


class StudentStateSelector(db.ModelBase):
    __tablename__ = 's_selectors'

    s_id = Column(Integer, ForeignKey('students.user_id'), primary_key=True)
    course = Column(Integer, ForeignKey('courses.id'))


class ParentBinding(db.ModelBase):
    __tablename__ = "parentsbindings"
    student_id = Column(Integer, ForeignKey('students.user_id'), primary_key=True)
    parent_id = Column(Integer, ForeignKey('parents.user_id'), primary_key=True)

    # def __init__(self, student_id, parent_id):
    #     self.parent_id = parent_id
    #     self.student_id = student_id


class Group(db.ModelBase):
    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True)
    grade = Column(SmallInteger, ForeignKey('grades.id'))
    letter = Column(String)
    lead_teacher = Column(Integer, ForeignKey('teachers.user_id'))
    student = relationship('StudentUser')
    classroom = Column(Integer, ForeignKey('classrooms.id'))
    course = relationship('AssignedCourse')
    binder = Column(String)
    schedule = relationship('Schedule')


class Grade(db.ModelBase):
    __tablename__ = 'grades'

    id = Column(Integer, primary_key=True)
    group = relationship('Group')
    course = relationship('Course')


class Course(db.ModelBase):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    grade = Column(SmallInteger, ForeignKey('grades.id'))
    course_name = Column(String, nullable=False)
    subject = Column(Integer, ForeignKey('subjects.id'))
    lesson = relationship('Lesson')
    assigned_to = relationship('AssignedCourse')

    def __repr__(self):
        subject = db.session.query(Subject).filter(Subject.id==self.subject)
        return f"{subject}. {self.course_name}"


class AssignedCourse(db.ModelBase):
    __tablename__ = 'assigned_courses'

    group_id = Column(Integer, ForeignKey('groups.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)
    teacher = Column(Integer, ForeignKey('teachers.user_id'), primary_key=True)
    complete = Column(Boolean, default=False)


class Subject(db.ModelBase):
    __tablename__ = 'subjects'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    teacher = relationship('TeacherSubjectBinder')
    course = relationship('Course')
    lesson = relationship('Lesson')

    def __repr__(self):
        return f'{self.title}'


class TeacherSubjectBinder(db.ModelBase):
    __tablename__ = 'teachersubjectbindings'
    teacher_id = Column(Integer, ForeignKey('teachers.user_id'), primary_key=True)
    subject_id = Column(Integer, ForeignKey('subjects.id'), primary_key=True)


class Lesson(db.ModelBase):
    __tablename__ = 'lessons'

    id = Column(Integer, primary_key=True)
    course = Column(Integer, ForeignKey('courses.id'), nullable=False)
    subject = Column(Integer, ForeignKey('subjects.id'))
    theme = Column(String, nullable=False)
    schedule = relationship('Schedule')
    mark = relationship('Mark')


class Mark(db.ModelBase):
    __tablename__ = 'marks'

    id = Column(Integer, primary_key=True)
    lesson = Column(Integer, ForeignKey('lessons.id'))
    student = Column(Integer, ForeignKey('students.user_id'))
    mark = Column(SmallInteger, nullable=False, default=0)
    type = Column(String, nullable=False, default=1)      # Types: [C]lasswork, [H]omework, [T]est
    description = Column(String)
    #
    # def __init__(self):
    #     self.mark_type = self.get_mark_type()

    def __repr__(self):
        mark = f"= {self.mark} =  - {self.get_mark_type()}. "
        if self.description:
            mark += self.description
        return mark

    def get_mark_type(self):
        types = {
            "C": "Класна робота",
            "H": "Домашня робота",
            "T": "Контрольна"
        }
        return types.get(self.type)


class Homework(db.ModelBase):
    __tablename__ = 'homeworks'

    id = Column(Integer, primary_key=True)
    lesson = Column(Integer, ForeignKey('lessons.id'))
    group = Column(Integer, ForeignKey('groups.id'))


class Classroom(db.ModelBase):
    __tablename__ = 'classrooms'

    id = Column(Integer, primary_key=True)
    room_no = Column(String)
    description = Column(String)
    teacher = relationship('TeacherUser')
    group = relationship('Group')


class Schedule(db.ModelBase):
    __tablename__ = 'schedule'

    id = Column(Integer, primary_key=True)
    timetable_id = Column(Integer, ForeignKey('timetable.id'))
    lesson_id = Column(Integer, ForeignKey('lessons.id'))
    course_id = Column(Integer, ForeignKey('courses.id'))
    group_id = Column(Integer, ForeignKey('groups.id'))


class Timetable(db.ModelBase):
    __tablename__ = 'timetable'

    id = Column(Integer, primary_key=True)
    lesson_no = Column(SmallInteger)
    weekday_no = Column(SmallInteger)
    week_no = Column(Integer)
    year = Column(Integer)
    schedule = relationship('Schedule')


db.create_db()
