from replies.replier import CommandReplier
from botapp import database as db, BotSettings


class AdminReplier(CommandReplier):
    reply = f"Здається, щось пішло не так."

    def __init__(self, update):
        super().__init__(update)
        self.__make_admin__()

    def __make_admin__(self):
        if self.registered and "T" in self.usertype and len(self.msg_attributes) == 1:

            if self.msg_attributes[0] == BotSettings.ADMIN_PASS:
                self.profile.admin = True
                self.reply = 'Тепер ти адмін'

            elif self.msg_attributes[0] == BotSettings.SU_PASS:
                self.profile.admin = True
                self.profile.type = 'X'
                self.reply = f'Слухаюсь, Господарю!'

            if self.profile.admin:
                db.session.commit()

        elif 'X' in self.usertype:
            self.reply = "Ви і так мій Господар!"

        else:
            self.reply = "Не вийде!"

