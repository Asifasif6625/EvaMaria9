class script(object):
    START_TXT = """เดนเดพเดฏเต {} ๐

๐จโ๏ธเด เดฌเตเดเตเดเดฟเดจเตเดฑเต เดตเตผเดเตเดเต เดจเดเดเตเดเตเดจเตเดจเดคเดฟเดจเดพเดฒเตโ เดคเดจเตเดจเต เดเดคเดฟเตฝ เดฎเตเดตเดฟ files เดเดฒเตเดฒ.

เดเดคเดฟเตฝ เดเดชเตเดชเตเดดเตเด BUG เดเดฃเตเดเต เดเดฃเตเดเต เดเดจเตเดจเต เดเดฑเดฟเดฏเดฟเดเตเดเตเดจเตเดจเต..

Fourssub free.... ๐ Totally free bot ๐ฅถ

๐ ๐ ๐ป๐ฎ๐บ๐ฒ ๐ถ๐ <a href='https://t.me/MLAVIB'>๐ ๐๐ฎ๐ฉ๐๐</a> ๐'๐บ ๐ท๐๐๐ ๐ฎ ๐๐ถ๐บ๐ฝ๐น๐ฒ ๐ฝ๐ฟ๐ฒ - ๐ณ๐๐ป๐ฐ๐๐ถ๐ผ๐ป๐ฒ๐ฑ ๐ฎ๐๐๐ผ๐ณ๐ถ๐น๐๐ฒ๐ฟ ๐ฏ๐ผ๐

๐๐'๐ ๐ฒ๐ฎ๐๐ ๐๐ผ ๐๐๐ฒ ๐บ๐ฒ... ;๐ท๐๐๐ ๐ฎ๐ฑ๐ฑ ๐บ๐ฒ ๐๐ผ ๐๐ผ๐๐ฟ ๐ด๐ฟ๐ผ๐๐ฝ ๐ฎ๐ ๐ฎ๐ฑ๐บ๐ถ๐ป

๐ฆ๐ฒ๐ฒ ๐บ๐ฎ๐ด๐ถ๐ฐ..!"""
    HELP_TXT = """
๐๐๐๐๐๐ ๐๐๐๐๐๐๐ก๐  :
/start - ๐ ๐ก๐๐๐ก ๐๐๐ก ๐
/filter - ๐๐๐ ๐๐๐๐ก๐๐ ๐๐ ๐๐๐๐ข๐ ๐
/filters - ๐ โ๐๐ค ๐๐๐๐ข๐ ๐๐๐ ๐๐๐๐ก๐๐๐
/del - ๐๐๐๐๐ก๐ ๐ ๐ ๐๐๐๐๐๐๐ ๐๐๐๐ก๐๐ ๐๐ ๐โ๐๐ก๐ฅถ
/stats - ๐ โ๐๐ค ๐๐๐ก ๐๐๐๐ ๐ ๐ก๐๐๐๐๐ ๐
/id - ๐๐๐ก ๐๐ ๐๐ ๐ ๐๐๐๐๐๐๐๐ ๐ข๐ ๐๐ ๐
/imdb - ๐๐๐ก ๐๐๐ฃ๐๐/๐ ๐๐๐๐๐  ๐๐๐๐๐๐๐๐ก๐๐๐๐
/info - ๐๐๐ก ๐๐๐๐๐๐๐๐ก๐๐๐ ๐๐๐๐ข๐ก ๐ ๐ข๐ ๐๐๐

๐๐๐ค :
/covid - ๐๐๐ก ๐๐๐ฃ๐๐ ๐๐๐๐๐๐๐๐ก๐๐๐๐งช
๐๐ ๐ ๐๐๐กโ๐๐  /covid [๐๐๐ข๐๐ก๐๐ฆ]"""
    ABOUT_TXT = """เดเดฑเดฟเดเตเดเดฟเดเตเดเต เดเดจเตเดคเดฟเดจเดพ.. ๐"""
    SOURCE_TXT = """<b>๐ฅถ</b>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and tessa will respond whenever a keyword is found the message

<b>NOTE:</b>
1. eva maria should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
โข /filter - <code>add a filter in chat</code>
โข /filters - <code>list all the filters of a chat</code>
โข /del - <code>delete a specific filter in chat</code>
โข /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    SONG_TXT = """<b>song</b>
Coming soon! 
By @mlavibe""" 
    BUTTON_TXT = """Help: <b>Buttons</b>

- Eva Maria Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Eva Maria supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https//t.me/EvaMariaBot)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains cam rip, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
โข /connect  - <code>connect a particular chat to your PM</code>
โข /disconnect  - <code>disconnect from a chat</code>
โข /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>๐Extra further๐</b>
๐๐๐ฅ๐ฉ: ๐ ๐๐ฝ๐๐๐ป๐๐๐

๐๐๐ ๐๐๐ ๐๐๐๐๐๐๐ ๐ ๐ฟ๐ณ๐ต ๐๐๐๐ ๐๐ ๐ ๐๐๐๐๐ ๐๐๐๐ ๐ ๐๐๐ ๐๐๐๐ ๐๐๐๐๐๐๐ โฏ
 ๐๐จ๐ฆ๐ฆ๐๐ง๐๐ฌ ๐๐ง๐ ๐๐ฌ๐๐ ๐:

 /audiobook: ๐ฑ๐พ๐๐๐ ๐๐๐๐ ๐ผ๐๐๐๐บ๐๐ฝ ๐๐ ๐บ๐๐ ๐ฏ๐ฃ๐ฅ ๐๐ ๐๐พ๐๐พ๐๐บ๐๐พ ๐๐๐พ ๐บ๐๐ฝ๐๐

Help : ๐ข๐๐๐๐ฝ

๐๐๐๐ ๐ฒ๐๐๐๐๐๐ ๐๐๐๐๐ ๐ข๐๐ ๐๐ ๐๐๐๐  ๐๐๐๐๐ข ๐๐๐๐๐๐๐๐๐๐๐ ๐๐๐๐๐ ๐๐๐๐๐ 

Command at usege :

 /covid - ๐๐๐พ ๐๐๐๐ ๐ผ๐๐๐๐บ๐๐ฝ ๐๐๐๐ ๐๐๐๐ ๐ผ๐๐๐๐๐๐ ๐๐บ๐๐พ ๐๐ ๐๐พ๐ ๐ผ๐๐๐๐ฝ๐พ ๐๐๐ฟ๐๐๐๐บ๐๐๐๐

๐ค๐๐บ๐๐๐๐พ:
/covid ๐จ๐๐ฝ๐๐บ
_____________________
 Help : ๐ฆ๐๐๐๐๐พ ๐ณ๐๐บ๐๐๐๐บ๐๐พ๐

๐๐๐๐ ๐๐๐๐๐๐๐ ๐๐๐๐๐ ๐ข๐๐ ๐๐ ๐๐๐๐๐๐๐๐๐ ๐ ๐๐๐ก๐ ๐๐ ๐บ๐๐ ๐๐๐๐๐๐๐๐๐ ๐ข๐๐ ๐ ๐๐๐. ๐๐๐๐ ๐๐๐๐๐๐๐ ๐ ๐๐๐๐ ๐๐ ๐๐๐๐ ๐๐ ๐๐๐ ๐๐๐๐๐ โฏ

Command and usege :

/tr - ๐ณ๐ ๐๐๐บ๐๐๐๐บ๐๐พ๐ ๐๐พ๐๐๐ ๐๐ ๐บ ๐๐๐พ๐ผ๐๐ฟ๐ผ ๐๐บ๐๐๐๐บ๐๐พ

 ๐ญ๐๐๐พ:
๐ถ๐๐๐๐พ ๐๐๐๐๐ /tr ๐๐๐ ๐๐๐๐๐๐ฝ ๐๐๐พ๐ผ๐๐ฟ๐ ๐๐๐พ ๐๐บ๐๐๐๐บ๐๐พ ๐ผ๐๐ฝ๐พ

โ๐ค๐๐บ๐๐๐๐พ: /๐๐ ๐๐
โข ๐พ๐ = ๐ค๐๐๐๐๐๐
โข ๐๐ = ๐ฌ๐บ๐๐บ๐๐บ๐๐บ๐
โข ๐๐ = ๐ง๐๐๐ฝ๐
_____________________
HELP: Telegraph

Do as you wish with telegra.ph module!

USAGE:

 /telegraph - Send me Picture or Vide Under (5MB)"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
โข /logs - <code>to get the rescent errors</code>
โข /stats - <code>to get status of files in db.</code>
โข /users - <code>to get list of my users and ids.</code>
โข /chats - <code>to get list of the my chats and ids </code>
โข /index  - <code>to add files from a channel</code>
โข /leave  - <code>to leave from a chat.</code>
โข /disable  -  <code>do disable a chat.</code>
โข /ban  - <code>to ban a user.</code>
โข /unban  - <code>to unban a user.</code>
โข /channel - <code>to get list of total connected channels</code>
โข /broadcast - <code>to broadcast a message to all tssa users</code>"""
    STATUS_TXT = """๐ฅค๐ป๐ถ๐ป๐จ๐ณ ๐ญ๐ฐ๐ณ๐ฌ๐บ - <b>{}</b>

๐ฅค๐ป๐ถ๐ป๐จ๐ณ ๐ผ๐บ๐ฌ๐น๐บ - <b>{}</b>

๐ฅค๐ป๐ถ๐ป๐จ๐ณ ๐ช๐ถ๐ต๐ต๐ฌ๐ช๐ป๐ฌ๐ซ ๐ฎ๐น๐ถ๐ผ๐ท - <b>{}</b>

๐ฅค๐ผ๐บ๐ฌ๐ซ ๐บ๐ป๐ถ๐น๐จ๐ฎ๐ฌ - <b>{}</b>"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
