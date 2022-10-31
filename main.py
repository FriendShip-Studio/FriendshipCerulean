import requests
import json
from nonebot import on_message
from nonebot.rule import fullmatch
from nonebot.adapters.mirai2 import Bot, GroupMessage, MessageSegment
import requests

online_players = on_message(fullmatch("服务器在线玩家"))


@online_players.handle()
async def request_server_players():

    request_query = {
        "uuid": "e14b6e83a9b64c45bc62b6cf2b86ba37",
        "remote_uuid": "bec0779700da46689e298c3bebe2957c",
        "apikey": "46c18fa56c1e4375b3777e8c52939aaf"
    }

    request_header = {
        "Content-Type": "application/json",
        "charset": "utf-8"
    }
    r = await requests.get("https://panel.friendship.org.cn/api/instance",
                           request_query, headers=request_header)

    ret_dict = await json.loads(r.text)

    await online_players.send(MessageSegment.plain(f'当前12周目服务器在线人数为{ret_dict["data"]["info"]["currentPlayers"]}'))
