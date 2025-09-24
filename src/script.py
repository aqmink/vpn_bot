def from_data(data) -> dict[dict[str, int | None | str]]:
    data = data["obj"]
    result = {
        "id": data["id"],
        "up": data["up"],
        "down": data["down"],
        "total": data["total"],
        "remark": data["remark"],
        "enable": data["enable"],
        "expiryTime": data["expiryTime"],
        "clientStats": data["clientStats"],
        "listen": data["listen"],
        "port": data["port"],
        "protocol": data["protocol"],
        "settings": {
            "clients": [],
        },
        "streamSettings": {}

    }
    for k, v in data.items():
        if k == "settings":
            lst = v.split("\n")
            lst = lst[2:]
            for i in range(len(lst)):
                lst[i] = lst[i].rstrip().lstrip()
                if lst[i] == "{" or lst[i] == "}," or lst[i] == "}" or lst[i] == "]," or lst[i] == "\"comment\": \"\",":
                    lst[i] = "/"
            while "/" in lst:
                lst.remove("/")
            val = {}
            for i in range(len(lst) - 1):
                tmp = lst[i].split(":")
                val[tmp[0].rstrip().lstrip()] = tmp[1].rstrip().lstrip()
                if len(val) == 10:
                    result["settings"]["clients"].append(val)
                    val = {}
        if k == "streamSettings":
            lst = v.split("\n")
            result["streamSettings"]["pbk"] = lst[28].split(":")[1].rstrip().lstrip()[1:-2]
            result["streamSettings"]["sid"] = lst[17].rstrip().lstrip()[1:-2]
    return result


def get_current_user(data, email):
    for i in data["settings"]["clients"]:
        if i["\"email\""] == "\"" + email + "\",":
            i["pbk"] = data["streamSettings"]["pbk"]
            i["sid"] = data["streamSettings"]["sid"]
            return i


def get_url(user_id, pbk, sid):
    return f"""vless://{user_id}@saveserf.com:443?type=tcp&security=reality&pbk={pbk}&fp=chrome&sni=google.com&sid={sid}&spx=%2F&flow=xtls-rprx-vision#freenetvpn-{user_id}"""


def get_channels(path):
    with open(path, encoding="ascii") as file:
        channels = file.readlines()
    return channels
