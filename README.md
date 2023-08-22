# tg_scool_bot

This telegram bot provides school study process info and managing.

Please visit landing page https://cinck.github.io/ 
or http://t.me/RD_sCool_Bot to start using bot.

Bot program uses database to store and retrieve users data and their requests.

There are four types of users:
- guest
- teacher
- student
- parent
Also availabe types combination ie teacher+parent types.

Each usertype has it own requests functionality.

Guest user will be kindly asked to register as one of the study process member.
School administartion should provide registration tokens to finish this process.
Tokens are used for users authentification.


Registration:

to register as teacher execute command (send message):
/iamteacher token

to register as student execute command (send message):
/iamstudent token

to register as parent execute command (send message):
/iamparent token

Teacher type users may obtain administrative options by executing:
/makemeadminplease admin_token

Admin options allow to create and make changes into database ie
create new groups and courses, add students, assign courses to teachers and groups, edit schedule etc.

Main command menu contains 'help' and 'start' commands.
Bot replies may contain clickable links with available options for easy navigation.
Available options depend on usertype.

Bot application is still in developement so not all described options are available at the moment.
