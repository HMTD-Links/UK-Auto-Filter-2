import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

class script(object):
    HOME_BUTTONURL_UPDATES = environ.get("HOME_BUTTONURL_UPDATES", 'https://beingtek.com/ref/KarthikUK')
    START_TXT = environ.get("START_TXT", '''<b>Hello {} ๐๐ป I'm an UK Studios Official Auto Filter Bot (Movie Search Bot) Maintained by @UK_Studios_Official. We are Providing Tamil and Tamil Dubbed Movies. More Languages Coming Soon. I Can Support Upto 4GB File. You Can Get added Files GDrive Links and 4GB above Links also. You Can Get GDrive Links in www.HMTDMovies.tk. Keep me Join to Our Official Channel to Receive Bot & Movies Updates in @UK_Studios_Official. Check "๐ About" Button.</b>''')
    HELP_TXT = """<b>Hi {}
I have that Features.</b>"""
    ABOUT_TXT = """<b><i>๐ค My Name : <a href=https://t.me/UK_Auto_Filter_Bot><b>UK Auto Filter Bot</b></a>\n
๐ง๐ปโ๐ป Developer : <a href=https://t.me/HMTD_Karthik><b>Karthik</b></a>\n
๐ Language : Pyrogram\n
๐ Framework : Python3\n
๐ก Hosted on : VPS\n
๐ข Updates Channel : <a href=https://t.me/UK_Studios_Official><b></b>UK Studios Official</a>\n
๐ Website : www.HMTDMovies.tk\n</b></i>"""
    SOURCE_TXT = """<b>Create One Like This:</b>
ยป I will Create One Bot For You. But Paid<b>
ยป Contact Me @HMTD_Karthik<b>"""
    MANUELFILTER_TXT = """<b>Help :</b> <b>Filters</b>

<b>- Filter is the feature were users can set automated replies for a particular keyword and Search Bot will respond whenever a keyword is found the message</b>

<b>NOTE:</b>
<b>1. Search Bot should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.</b>

<b>Commands and Usage:</b>
<b>โข /filter - add a filter in chat
โข /filters - list all the filters of a chat
โข /del - delete a specific filter in chat
โข /delall - delete the whole filters in a chat (chat owner only)</b>"""
    BUTTON_TXT = """<b>Help :</b> <b>Buttons</b>

<b>- Search Bot Supports both url and alert inline buttons.</b>

<b>NOTE:</b>
<b>1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Search Bot supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format</b>

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/HMTD_Karthik)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """<b>Help :</b> <b>Auto Filter</b>

<b>NOTE:</b>
<b>1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db.</b>"""
    CONNECTION_TXT = """<b>Help :</b> <b>Connections</b>

<b>- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.</b>

<b>NOTE:</b>
<b>1. Only admins can add a connection.
2. Send</b> <code>/connect</code> <b>for connecting me to ur PM</b>

<b>Commands and Usage:</b>
<b>โข /connect  - connect a particular chat to your PM
โข /disconnect  - disconnect from a chat
โข /connections - list all your connections</b>"""
    EXTRAMOD_TXT = """<b>Help :</b> <b>Extra Modules</b>

<b>NOTE:</b>
<b>these are the extra features of Auto Filter Bot (Movie Search Bot)</b>

<b>Commands and Usage:</b>
<b>โข /id - get id of a specified user.
โข /info  - get information about a user.
โข /imdb  - get the film information from IMDb source.
โข /search  - get the film information from various sources.</b>"""
    ADMIN_TXT = """<b>Help :</b> <b>Admin mods</b>

<b>NOTE:</b>
<b>This module only works for my admins</b>

<b>Commands and Usage:</b>
<b>โข /logs - to get the rescent errors
โข /stats - to get status of files in db.
โข /delete - to delete a specific file from db.
โข /users - to get list of my users and ids.
โข /chats - to get list of the my chats and ids 
โข /leave  - to leave from a chat.
โข /disable  -  do disable a chat.
โข /ban  - to ban a user.
โข /unban  - to unban a user.
โข /channel - to get list of total connected channels
โข /broadcast - to broadcast a message to all users</b>"""
    STATUS_TXT = """โฆ๏ธ Total Files : <code>{}</code>
โฆ๏ธ Total Users : <code>{}</code>
โฆ๏ธ Total Chats : <code>{}</code>
โฆ๏ธ Used Storage : <code>{}</code> ๐ผ๐๐ฑ
โฆ๏ธ Free Storage : <code>{}</code> ๐ผ๐๐ฑ"""
    LOG_TEXT_G = """<b>#New Group</b>
    
<b>แโบ Group โชผ {}(<code>{}</code>)</b>
<b>แโบ Total Members โชผ <code>{}</code></b>
<b>แโบ Added By โชผ {}</b>
"""
    LOG_TEXT_P = """<b>#New User</b>
    
<b>แโบ ID - <code>{}</code></b>
<b>แโบ Name - {}</b>
"""
