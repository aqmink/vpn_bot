import random
from string import ascii_letters, digits


def get_sid():
    return ''.join([random.choice(ascii_letters + digits) for _ in range(3, 10)])


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
    print(result)
    return result


def get_current_user(data, email):
    for i in data["settings"]["clients"]:
        if i["\"email\""] == "\"" + email + "\",":
            i["pbk"] = data["streamSettings"]["pbk"]
            i["sid"] = data["streamSettings"]["sid"]
            return i


def get_url(user_id, pbk, sid):
    return f"""vless://{user_id}@saveserf.com:443?type=tcp&security=reality&pbk={pbk}&fp=chrome&sni=google.com&sid={sid}&spx=%2F&flow=xtls-rprx-vision#freenetvpn-{user_id}"""


def get(path):
    with open(path) as file:
        result = file.readlines()
    return result


def save_id(user_id):
    with open(r"C:\Users\89052\projects\vpn_bot\src\clients_ids.txt", "a") as file:
        if str(user_id) + "\n" not in get(r"C:\Users\89052\projects\vpn_bot\src\clients_ids.txt"):
            file.write(str(user_id) + "\n")


def get_text_1(channels):
    return f"🆓FREE INTERNET🆓\n\nВы попали в VPN, который предлагает услуги платных сервисов, за БЕСПЛАТНО.\n\nНО надо выполнить одно простое условие:\n\n🔵Подписаться на ниже перечисленные телеграмм каналы. И сразу после этого вы получите доступ автоматически\n\n🔥 Наши серверы не имеют ограничений по скорости и трафику, работает на всех устройствах, платформах и приложениях.\n\n🔐 Максимальная анонимность и безопасность, которую не даст ни один сервис в мире.\n\n🚀 Получите доступ в открытый Интернет без ограничений!\n\n🤗НИЖЕ, ТЕЛЕГРАММ КАНАЛЫ НА КОТОРЫЕ НУЖНО ПОДПИСАТЬСЯ:\n\n {show_channels(channels)}"


def get_text_2():
    return "🏁Всё! вы получили ДОСТУП к нашему сервису.\n\n😎Теперь вы можете наслаждаться просмотром ваших любимых видео и фильмов.\n\n⬇️Ниже вы найдёте:⬇️\n\n🧑‍🏫Инструкцию по подключению.\n\n🛟Ссылку на поддержу, которой вы сможете задать все ваши вопросы.\n"


def get_text_3(channels):
    return f"Вы не подписаны на все предложенные тгк 😕, проверьте ваши подписки на канналы ниже и попробуйте снрова\n\n {show_channels(channels)}"


def get_text_4(user_id): 
    return f"✅ Ваш FREE INTERNET активирован! 🎉\n\nВаш ID: {user_id}\n\nКлюч и инструкция для подключения 👇\n"


def get_text_5(channels):
    return f"Я отключил вам доступ к впн, так как вы не подписаны на все тгк:\n{show_channels(channels)}"


def get_text_6():
    return "🚀 Сервис использует протокол VLESS, который обеспечивает максимальную безопасность и анонимность.\n\n🌍 Сервер расположен в Германии и автоматически маскируется под локальные сервисы. Это исключает возможность определить Ваше местоположение.\n\n💡 Оставайтесь защищёнными и наслаждайтесь свободой интернета!"


def show_channels(channels): 
    return '👉 ' + '👉 '.join(channels)
