from replies.replier import CommandReplier
from botapp import database as db, BotSettings


class HelpReplier(CommandReplier):
    reply = (
        f"Довідка\n\n"
        f"Ви завжди можете попросити бота звертатися до вас за вказаним ім'ям."
        f" Для цього напишіть йому:\n\n"
        f"Зви мене ...\n\n"
        f"(замість крапок напишіть ім'я)\n\n"
    )

    guest_reply = (
        f"Для подальшої нашої співпраці тобі потрібно зареєструватися як учаснику навчального процесу.\n"
        f"Звернись до адміністрації школи, щоб надали тобі твій персональний код для реєстрації.\n\n"
        f"Щоб зареєструватися вчителем введи команду:\n"
        f"/iamteacher <персональний код>\n\n"
        f"Щоб зареєструватися учнем введи команду:\n"
        f"/iamstudent <персональний код>\n\n"
        f"Щоб зареєструватися як батько чи матір учня введи команду:\n"
        f"/iamparent <персональний код>"
    )

    teacher_reply = (
        f"Тут Ви можете переглядати ваш розклад, списки ваших дисциплін та класів, у яких викладаєте.\n"

    )

    student_reply = (
        f"Цей бот може показувати розклад уроків, оцінки."
    )

    parent_reply = (
        f"Цей бот може показувати розклад та оцінки Вашої дитини."
        f"Виберіть дитину, інформацію якої хочете дізнатися."
    )

    admin_reply = (
        f"Ви маєте права адміністратора. Ви можете створювати, додавати та редагувати:\n"
        f" -дисципліни, що викладаються,\n"
        f" -класи,\n"
        f" -учнів,\n"
        f" -вчителів,\n"
        f" -батьків учнів\n\n"
    )

    start_link = (
        f"Розпочніть роботу, натиснувши на посилання:\n"
        f"/start"
    )

    def __init__(self, update):
        super().__init__(update)

        if self.registered:

            if 'G' in self.usertype:
                self.reply += self.guest_reply

            if 'T' in self.usertype:
                self.reply += self.teacher_reply

            if 'S' in self.usertype:
                self.reply += self.student_reply

            if 'P' in self.usertype:
                self.reply += self.parent_reply

            if self.profile.admin:
                self.reply += self.admin_reply

        self.reply += self.start_link