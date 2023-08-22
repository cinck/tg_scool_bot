# from botapp import database as db
# from models.models import User
from replies.replier import CommandReplier


class StartReplier(CommandReplier):
    reply = ("Вітаю!\nРадий бачити нові обличчя! Давай знайомитись!\nЯ - бот, твій шкільний помічник!\n"
             "А як тебе звати?\nНапиши мені повідомлення у такому форматі:\n\n"
             "'Зви мене Люк Скайвокер'\n\n Тоді я зможу запам'ятати твоє ім'я"
             " і завжди так звертатимусь до тебе.")

    t_reply = (
        f"---------------------\n"
        f"/schedule - розклад занять;\n\n"
        f"/groups - список груп, в яких викладаєте;\n\n"
        f"/courses - список поточних дисциплін, які викладаєте;\n\n"
        # f"---------------------\n"
    )

    s_reply = (
        f"---------------------\n"
        f"/courses - список поточних дисциплін, які вивчаєте;\n\n"
        f"/schedule - розклад уроків;\n\n"
        # f"/marks - оцінки;\n\n"
        # f"---------------------\n"
    )

    p_reply = (
        f"---------------------\n"
        f"/selectchild - вибрати дитину для перегляду\n\n"
        f"/courses - список дисциплін, які вивчає учень;\n\n"
        f"/schedule - розклад уроків учня;\n\n"
        # f"---------------------\n"
    )

    u_reply = (
        f"---------------------\n"
        f"/profile - відомості профілю;\n\n"
        f"/help - довідка;\n\n"
        # f"---------------------\n"
    )

    g_reply = (
        f"---------------------\n"
        f"Отже, як я бачу ти тут вперше.\n"
        f"Щоб ми могли далі співпрацювати тобі потрібно зареєструватися як учаснику навчального процесу.\n"
        f"Звернись до адміністрації школи, щоб надали тобі твій персональний код для реєстрації.\n\n"
        f"Щоб зареєструватися вчителем введи команду:\n"
        f"/iamteacher <персональний код>\n\n"
        f"Щоб зареєструватися учнем введи команду:\n"
        f"/iamstudent <персональний код>\n\n"
        f"Щоб зареєструватися як батько чи матір учня введи команду:\n"
        f"/iamparent <персональний код>"
    )

    def __init__(self, update):
        super().__init__(update)
        if self.registered:
            self.reply = f"Вітаю, {self.username}!\nЧим можу допомогти?\n\n"
            if 'T' in self.usertype:
                self.reply += self.t_reply
            if 'S' in self.usertype:
                self.reply += self.s_reply
            if 'P' in self.usertype:
                self.reply += self.p_reply
            if 'X' in self.usertype:
                self.reply += self.t_reply + self.s_reply + self.p_reply
            self.reply += self.u_reply
            if 'G' in self.usertype:
                self.reply = self.g_reply
