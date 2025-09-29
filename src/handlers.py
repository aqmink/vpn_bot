import asyncio

from aiogram import Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import (
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery,
    WebAppInfo,
)
from aiogram.utils.formatting import Text, Pre

from client import APIClient
from script import (
    get_url, 
    get, 
    save_id, 
    get_text_1, 
    get_text_2, 
    get_text_3, 
    get_text_4, 
    get_text_5,
    get_text_6,
)

dp = Dispatcher()

client = APIClient()


@dp.message(Command("show"))
async def show(message: Message):
    if message.from_user.id == 1485867091:
        while True:
            for user_id in get(r"C:\Users\89052\projects\vpn_bot\src\clients_ids.txt"):
                flag = True
                channels = get(r"C:\Users\89052\projects\vpn_bot\src\channels_list.txt")
                for channel in channels:
                    if (await message.bot.get_chat_member(channel, user_id)).status not in ["member", "creator", "administrator"]:
                        flag = False
                if not flag:
                    try:
                        await client.update_client(int(user_id), False)
                        await message.bot.send_message(
                            chat_id=int(user_id),
                            text=get_text_5(channels),
                            reply_markup=InlineKeyboardMarkup(
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(
                                            text="✅ Проверить",
                                            callback_data="check",
                                        ),
                                    ]   
                                ],
                            )
                        )
                    except:
                        pass
            await asyncio.sleep(12 * 3600)


@dp.message(Command("post"))
async def post(message: Message):
    if message.chat.id == -4971478443:
        for user_id in get(r"C:\Users\89052\projects\vpn_bot\src\clients_ids.txt"):
            await message.bot.send_message(int(user_id), message.text[6:])
        await message.answer("Рассылка прошла успешно")


@dp.message(CommandStart())
async def hello(message: Message):
    save_id(message.from_user.id)
    await message.answer(
        text=get_text_1(get(r"C:\Users\89052\projects\vpn_bot\src\channels_list.txt")),
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text="👥️ О сервисе",
                        callback_data="about"
                    ),
                    InlineKeyboardButton(
                        text="✅ Проверить",
                        callback_data="check"
                    ),
                ],
            ],
        )
    )
    


@dp.callback_query(F.data == "check")
async def check(callback_query: CallbackQuery):
    user_id = callback_query.from_user.id
    flag = True
    for channel in get(r"C:\Users\89052\projects\vpn_bot\src\channels_list.txt"):
        if (await callback_query.bot.get_chat_member(channel, user_id)).status not in ["member", "creator", "administrator"]:
            flag = False
    if flag: #Измени на проде!!!
        response_data = await client.set_client(user_id)
        if response_data["success"] == True:
            await callback_query.bot.send_message(chat_id=-4971478443, text="ура, новый пользователь")
        await client.update_client(user_id, True)
        await callback_query.message.edit_text(
            text=get_text_2(),
            reply_markup=InlineKeyboardMarkup(
                inline_keyboard=[
                    [
                        InlineKeyboardButton(
                            text="🔙 Назад",
                            callback_data="back"
                        ),
                        InlineKeyboardButton(
                            text="📄 Инструкция",
                            web_app=WebAppInfo(url="https://telegra.ph/Instrukciya-po-ustanovke-VPN-na-vse-tipy-ustrojstv-08-28")
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            text="🛡 Подключится",
                            callback_data="access"
                        ),
                        InlineKeyboardButton(
                            text="🛟 Поддержка",
                            callback_data="support"
                        ),
                    ],
                ]
            )
        )
    else:
        if await client.get_client_by_email(f"freenet-vpn-{user_id}"):
            await client.update_client(user_id, False)
        await callback_query.message.edit_text(
            text=get_text_3(get(r"C:\Users\89052\projects\vpn_bot\src\channels_list.txt")),
            reply_markup=InlineKeyboardMarkup(
                inline_keyboard=[
                    [
                        InlineKeyboardButton(
                            text="✅ Проверить",
                            callback_data="check1"
                        ),
                        InlineKeyboardButton(
                            text="🔙 Назад",
                            callback_data="back1"
                        ),
                    ]
                ]
            )
        )


@dp.callback_query(F.data == "check1")
async def check(callback_query: CallbackQuery):
    user_id = callback_query.from_user.id
    flag = True
    for channel in get(r"C:\Users\89052\projects\vpn_bot\src\channels_list.txt"):
        if (await callback_query.bot.get_chat_member(channel, user_id)).status not in ["member", "creator", "administrator"]:
            flag = False
    if flag: #Измени на проде!!!
        response_data = await client.set_client(user_id)
        if response_data["success"] == True:
            await callback_query.bot.send_message(chat_id=-4971478443, text="ура, новый пользователь")
        await client.update_client(user_id, True)
        await callback_query.message.edit_text(
            text=get_text_2(),
            reply_markup=InlineKeyboardMarkup(
                inline_keyboard=[
                    [
                        InlineKeyboardButton(
                            text="🔙 Назад",
                            callback_data="back"
                        ),
                        InlineKeyboardButton(
                            text="📄 Инструкция",
                            web_app=WebAppInfo(url="https://telegra.ph/Instrukciya-po-ustanovke-VPN-na-vse-tipy-ustrojstv-08-28")
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            text="🛡 Подключится",
                            callback_data="access"
                        ),
                        InlineKeyboardButton(
                            text="🛟 Поддержка",
                            callback_data="support"
                        ),
                    ],
                ]
            )
        )
    else:
        if await client.get_client_by_email(f"freenet-vpn-{user_id}"):
            await client.update_client(user_id, False)
        await callback_query.message.edit_text(
            text=get_text_3(get(r"C:\Users\89052\projects\vpn_bot\src\channels_list.txt")),
            reply_markup=InlineKeyboardMarkup(
                inline_keyboard=[
                    [
                        InlineKeyboardButton(
                            text="✅ Проверить",
                            callback_data="check"
                        ),
                        InlineKeyboardButton(
                            text="🔙 Назад",
                            callback_data="back1"
                        ),
                    ]
                ]
            )
        )


@dp.callback_query(F.data == "access")
async def access(callback_query: CallbackQuery):
    user_id = callback_query.from_user.id
    user = await client.get_client_by_email(f"freenet-vpn-{user_id}")
    if user and user["\"enable\""] != "false,":
        await callback_query.message.edit_text(
            **Text(
                get_text_4(user_id), 
                Pre(
                    f"{get_url(user_id, user['pbk'], user['sid'])}", 
                    language="copy")
                ).as_kwargs(),
            reply_markup=InlineKeyboardMarkup(
                inline_keyboard=[
                    [
                        InlineKeyboardButton(
                            text="🔙 Назад",
                            callback_data="back"
                        ),
                        InlineKeyboardButton(
                            text="📄 Инструкция",
                            web_app=WebAppInfo(url="https://telegra.ph/Instrukciya-po-ustanovke-VPN-na-vse-tipy-ustrojstv-08-28")
                        ),
                    ]
                ]
            )
        )
    else:
        await callback_query.message.edit_text(
            text="Вы не подписались на все тгк",
            reply_markup=InlineKeyboardMarkup(
                inline_keyboard=[
                    [
                        InlineKeyboardButton(
                            text="✅ Проверить",
                            callback_data="check"
                        ),
                        InlineKeyboardButton(
                            text="🔙Назад",
                            callback_data="back1"
                        ),
                    ],
                ]
            )
        )


@dp.callback_query(F.data == "support")
async def access(callback_query: CallbackQuery):
    await callback_query.message.edit_text(
        text="🆘 Нужна помощь?\n\n❓ Что-то не получается?\n❓ Как пользоваться?\n❓ Как все устроено?\n\nМожете открыть инструкцию или связаться с ботом поддержки:\n\n@saveserf_support_bot",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[[
                InlineKeyboardButton(
                    text="🔙 Назад", callback_data="back"
                )
            ]]
        )
    )


@dp.callback_query(F.data == "about")
async def access(callback_query: CallbackQuery):
    await callback_query.message.edit_text(
        text=get_text_6(),
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text="🔙 Назад", callback_data="back1"
                    ),
                    InlineKeyboardButton(
                        text="📄 Правила", web_app=WebAppInfo(url="https://telegra.ph/Freeinternet-09-25")
                    ),
                ]
            ]
        )
    )


@dp.callback_query(F.data == "about1")
async def access(callback_query: CallbackQuery):
    await callback_query.message.edit_text(
        text=get_text_6(),
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text="🔙 Назад", callback_data="back"
                    ),
                    InlineKeyboardButton(
                        text="📄 Правила", web_app=WebAppInfo(url="https://telegra.ph/Freeinternet-09-25")
                    ),
                ]
            ]
        )
    )


@dp.callback_query(F.data == "back")
async def hello(callback_query: CallbackQuery):
    await callback_query.message.edit_text(
        text=get_text_1(get(r"C:\Users\89052\projects\vpn_bot\src\channels_list.txt")),
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text="📄 Инструкция",
                        web_app=WebAppInfo(url="https://telegra.ph/Instrukciya-po-ustanovke-VPN-na-vse-tipy-ustrojstv-08-28")
                    ),
                    InlineKeyboardButton(
                        text="🛡 Подключение",
                        callback_data="access"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        text="🆘️ Поддержка",
                        callback_data="support"
                    ), 
                    InlineKeyboardButton(
                        text="👥️ О сервисе",
                        callback_data="about1"
                    ),
                ],
            ],
        )
    )


@dp.callback_query(F.data == "back1")
async def hello(callback_query: CallbackQuery):
    await callback_query.message.edit_text(
        text=get_text_1(get(r"C:\Users\89052\projects\vpn_bot\src\channels_list.txt")),
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text="👥️ О сервисе",
                        callback_data="about"
                    ),
                    InlineKeyboardButton(
                        text="✅ Проверить",
                        callback_data="check"
                    ),
                ],
            ],
        )
    )


# @dp.message(F.text == "test")
# async def test(message):
#     await client.set_client(1)
#     pprint(await client.get_clients())
