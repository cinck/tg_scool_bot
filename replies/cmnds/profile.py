from replies.replier import CommandReplier
from utils.utils import collect_info


class ProfileReplier(CommandReplier):
    reply = f"Здається, щось пішло не так."

    general_info = None
    teacher_info = None
    student_info = None
    parent_info = None

    def __init__(self, update):
        super().__init__(update)
        if self.registered:
            self.general_info = self.profile.get_user_data()

            if "T" in self.usertype or "X" in self.usertype:
                self.teacher_info = self.profile.get_teacher_data()

            if "S" in self.usertype or "X" in self.usertype:
                self.student_info = self.profile.get_student_data()

            if "P" in self.usertype or "X" in self.usertype:
                self.parent_info = self.profile.get_parent_data()

            profile_data = {
                'Загальна інформація': self.general_info,
                'Вчитель': self.teacher_info,
                'Батьківство': self.parent_info,
                'Учень': self.student_info,
            }

            self.reply = collect_info(profile_data)
