from replies.cmnds.newgroup import NewGroup
from replies.cmnds.mygroups import MyGroupReplier
from replies.cmnds.grouplist import GroupListReplier
from replies.cmnds.mycourses import MyCourseReplier
from replies.cmnds.coursedetail import CourseDetailReplier
from replies.cmnds.iamstudent import IamStudentReplier
from replies.cmnds.marks import MarksReplier
from replies.cmnds.adminreplier import AdminReplier
from replies.cmnds.iamteacher import IamTeacherReplier
from replies.cmnds.iamparent import IamParentReplier
from replies.cmnds.liststudents import ListStudentsReplier
from replies.cmnds.listusers import ListUsersReplier
from replies.cmnds.myschedule import MyScheduleReplier
from replies.cmnds.profile import ProfileReplier
from replies.cmnds.start import StartReplier
from replies.cmnds.help import HelpReplier
from replies.cmnds.test import TestReplier
from replies.cmnds.selectchild import SelectChildReplier


COMMANDS_HANDLERS = {
    '/newgroup': NewGroup,
    '/groups': MyGroupReplier,
    '/grouplist': GroupListReplier,
    '/courses': MyCourseReplier,
    '/coursedetail': CourseDetailReplier,
    '/iamstudent': IamStudentReplier,       # IamStudentReplier
    '/marks': MarksReplier,
    '/makemeadminplease': AdminReplier,
    '/iamteacher': IamTeacherReplier,
    '/iamparent': IamParentReplier,
    '/liststudents': ListStudentsReplier,
    '/listusers': ListUsersReplier,
    '/schedule': MyScheduleReplier,
    # '/newcourse': NewCourseReplier,
    '/profile': ProfileReplier,
    '/start': StartReplier,
    '/help': HelpReplier,
    '/test': TestReplier,
    '/selectchild': SelectChildReplier
}


def get_command_handler(message: str):
    command = message.split(" ")[0].split("_")[0]
    return COMMANDS_HANDLERS.get(command)