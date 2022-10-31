import json
import requests

request_query = {
    "uuid": "e14b6e83a9b64c45bc62b6cf2b86ba37",
    "remote_uuid": "bec0779700da46689e298c3bebe2957c",
    "apikey": "46c18fa56c1e4375b3777e8c52939aaf"
}

request_header = {
    "Content-Type": "application/json",
    "charset": "utf-8"
}
r = requests.get("https://panel.friendship.org.cn/api/instance",
                 request_query, headers=request_header)

ret_dict = json.loads(r.text)
print(int(ret_dict["data"]["info"]["currentPlayers"]))
