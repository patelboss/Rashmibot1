class script(object):
    START_TXT = """Hello {},
๐ผ๐ ๐ฝ๐ฐ๐ผ๐ด ๐ธ๐ <a href=https://t.me/{}>{}</a>,\n\nเคฎเฅเค เคเคชเคเฅ เคฎเฅเคตเฅเค เคเฅเคเคจเฅ เคฎเฅเค เคเคฎ เคธเคฎเคฏ เคเคฐ เคฎเฅเคนเคจเคค เคฎเฅเค เคธเคเฅเค เคชเคฐเคฟเคฃเคพเคฎ เคฆเฅเคจเฅ เคเฅ เคฒเคฟเค เคธเคฎเคเฅเคท เคนเฅเค...๐คช"""
    HELP_TXT = """๐ท๐ด๐ {}
๐ท๐ด๐๐ด ๐ธ๐ ๐๐ท๐ด ๐ท๐ด๐ป๐ฟ ๐ต๐พ๐ ๐ผ๐ ๐ฒ๐พ๐ผ๐ผ๐ฐ๐ฝ๐ณ๐."""
    ABOUT_TXT = """โฏ ๐ผ๐ ๐ฝ๐ฐ๐ผ๐ด: แแแแแทแฅ
โฏ ๐๐๐๐๐: <a href=https://t.me/Filmykeedha_ask>๐๐ข๐ฅ๐ฆ๐ฒ๐ค๐๐๐๐ก๐_๐๐ฌ๐ค</a>
โฏ ๐๐ผ๐๐ ๐พ๐๐ผ๐๐๐๐: <a href=https://t.me/Filmykeedha>๐๐ข๐ฅ๐ฆ๐ฒ๐ค๐๐๐๐ก๐</a>
โฏ ๐พ๐๐๐ผ๐๐๐: <a href=https://t.me/pankaj_patel_p>แฎแฅฒแฅโฒแฅฒแ๐ฎ๐ผโค๏ธ๐</a>
โฏ ๐ ๐ผ๐๐ถ๐ฒ ๐๐ฎ๐ป๐ด๐๐ฎ๐ด๐ฒ:๐๐ข๐ง๐๐ข, ๐๐ง๐ ๐ฅ๐ข๐ฌ๐ก, ๐๐๐ฆ๐ข๐ฅ ๐๐ง๐ ๐๐๐ง๐ฒ ๐๐จ๐ซ๐ ๐๐จ๐ฏ๐ข๐ ๐๐๐ง๐ ๐ฎ๐๐ ๐
โฏ ๐๐ผ๐ ๐๐ฎ๐ป๐ด๐๐ฎ๐ด๐ฒ: ๐๐ข๐ง๐๐ข ๐๐ง๐ ๐๐ง๐ ๐ฅ๐ข๐ฌ๐ก
โฏ ๐ฑ๐๐ธ๐ป๐ณ ๐๐๐ฐ๐๐๐: V1.0.1 [ ๐ฑ๐ด๐๐ฐ ]"""
    SOURCE_TXT = """<b>NOTE:</b>
- แแแแแทแฅ is an open source project. 
-   

<b>DEVS:</b>
- <a href=https://t.me/pankaj_patel_p>แฎแฅฒแฅโฒแฅฒแ๐ฎ๐ผโค๏ธ๐</a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and แแแแแทแฅ will respond whenever that keyword hits the message

<b>NOTE:</b>
1. BOT should have admin privillage.
2. Only admins can add filters in a chat.
3. Alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
โข /filter - <code>add a filter in chat</code>
โข /filters - <code>list all the filters of a chat</code>
โข /del - <code>delete a specific filter in chat</code>
โข /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. BOT supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/Filmykeedha)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. Make sure that your channel does not contains camrips, porn and fake files.
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
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of แแแแแทแฅ

<b>Commands and Usage:</b>
โข /id - <code>get id of a specified user.</code>
โข /info  - <code>get information about a user.</code>
โข /imdb  - <code>get the film information from IMDb source.</code>
โข /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
โข /logs - <code>to get the rescent errors</code>
โข /stats - <code>to get status of files in db.</code>
โข /delete - <code>to delete a specific file from db.</code>
โข /users - <code>to get list of my users and ids.</code>
โข /chats - <code>to get list of the my chats and ids </code>
โข /leave  - <code>to leave from a chat.</code>
โข /disable  -  <code>do disable a chat.</code>
โข /ban  - <code>to ban a user.</code>
โข /unban  - <code>to unban a user.</code>
โข /channel - <code>to get list of total connected channels</code>
โข /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """โ ๐๐พ๐๐ฐ๐ป ๐ต๐ธ๐ป๐ด๐: <code>{}</code>
โ ๐๐พ๐๐ฐ๐ป ๐๐๐ด๐๐: <code>{}</code>
โ ๐๐พ๐๐ฐ๐ป ๐ฒ๐ท๐ฐ๐๐: <code>{}</code>
โ ๐๐๐ด๐ณ ๐๐๐พ๐๐ฐ๐ถ๐ด: <code>{}</code> ๐ผ๐๐ฑ
โ ๐ต๐๐ด๐ด ๐๐๐พ๐๐ฐ๐ถ๐ด: <code>{}</code> ๐ผ๐๐ฑ"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
