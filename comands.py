from telegram import Update
from telegram.ext import ContextTypes

# Command pattern:
# async def <name>_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     from replies.<replier> import <CommandReplier>
#     reply = "Bot reply text here"
#     await context.bot.send_message(chat_id=update.effective_chat.id, text=reply)


# async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     from replies.cmnds.start import StartReplier
#     reply = StartReplier(update).reply
#     await context.bot.send_message(chat_id=update.effective_chat.id, text=reply)
#
#
# async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     reply = ("Вітаю!\nФункціонал ще в розробці, але ти можеш назвати мені своє ім'я,"
#              " виконавши команду '/name' і я тебе запам'ятаю!\n"
#              "Іноді я не відповідаю одразу. Це може бути через те, що була проблема із зв'язоком, або мене вимкнули.\n"
#              "Спробуй команду /test із меню щоб дізнатися, чи є зв'язок і спробуй повторити запит"
#              " ще один або кілька разів, поки не відповім."
#              "\n\n"
#              "Hi! Functionality is still in development."
#              " But you can tell me your name '/name' and I'll remember you.\n"
#              "Sometimes I don't reply. If so try /test to check if I'm online and try again few times."
#              )
#     await context.bot.send_message(chat_id=update.effective_chat.id, text=reply)
#
#
# async def register_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     from replies.comreplies import Registrator
#     message = update.effective_message
#     registrator = Registrator(message)
#     reply = registrator.reply
#     await context.bot.send_message(chat_id=update.effective_chat.id, text=reply)
#
#
# async def test_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     reply = "Yes, I'm online!\n\nТак, я на зв'язку!\n\n /start"
#     await context.bot.send_message(chat_id=update.effective_chat.id, text=reply)
#
#
# async def list_teachers_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     from replies.list_teacher import TeachersList
#     reply = TeachersList().reply
#     await context.bot.send_message(chat_id=update.effective_chat.id, text=reply)
#
#
# async def create_user_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     from replies.cmnds.createuser import CreateUserReplier
#     reply = CreateUserReplier(update).reply
#     await context.bot.send_message(chat_id=update.effective_chat.id, text=reply)
#
#
# async def iamteacher_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     from replies.cmnds.iamteacher import IamTeacherReplier
#     reply = IamTeacherReplier(update).reply
#     await context.bot.send_message(chat_id=update.effective_chat.id, text=reply)
#
#
# async def iamparent_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     from replies.cmnds.iamparent import IamParentReplier
#     reply = IamParentReplier(update).reply
#     await context.bot.send_message(chat_id=update.effective_chat.id, text=reply)
#
#
# async def iamstudent_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     from replies.cmnds.iamstudent import IamStudentReplier
#     reply = IamStudentReplier(update).reply
#     await context.bot.send_message(chat_id=update.effective_chat.id, text=reply)
#
#
# async def admin_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     from replies.cmnds.adminreplier import AdminReplier
#     reply = AdminReplier(update).reply
#     await context.bot.send_message(chat_id=update.effective_chat.id, text=reply)
#
#
# async def myprofile_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     from replies.cmnds.profile import ProfileReplier
#     reply = ProfileReplier(update).reply
#     await context.bot.send_message(chat_id=update.effective_chat.id, text=reply)
#
#
# async def myschedule_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     from replies.cmnds.myschedule import MyScheduleReplier
#     reply = MyScheduleReplier(update).reply
#     await context.bot.send_message(chat_id=update.effective_chat.id, text=reply)
#
#
# async def listusers_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     from replies.cmnds.listusers import ListUsersReplier
#     reply = ListUsersReplier(update).reply
#     await context.bot.send_message(chat_id=update.effective_chat.id, text=reply)