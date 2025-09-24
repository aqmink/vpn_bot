import asyncio

from aiogram import Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import (
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    URLInputFile,
    CallbackQuery,
    WebAppInfo,
)
from aiogram.utils.formatting import Text, Pre

from client import APIClient
from script import get_url, get_channels

dp = Dispatcher()

client = APIClient()


@dp.message(CommandStart())
async def hello(message: Message):
    # image = URLInputFile(
    #     url="https://exa-pizza.ru/files/products/pomidor.1800x1200.png",
    #     filename="python-logo.png"
    # )
    await message.answer(
        text="🆓FREE INTERNET🆓\n\nВы попали в VPN, который предлагает услуги платных сервисов, за БЕСПЛАТНО.\n\nНО надо выполнить одно простое условие:\n\n🔵Подписаться на ниже перечисленные телеграмм каналы. И сразу после этого вы получите доступ автоматически\n\n🔥 Наши серверы не имеют ограничений по скорости и трафику, работает на всех устройствах, платформах и приложениях.\n\n🔐 Максимальная анонимность и безопасность, которую не даст ни один сервис в мире.\n\n🚀 Получите доступ в открытый Интернет без ограничений!\n\n🤗НИЖЕ, ТЕЛЕГРАММ КАНАЛЫ НА КОТОРЫЕ НУЖНО ПОДПИСАТЬСЯ:\n\n 👉 @freeimternet",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text="👥️ О сервисе",
                        callback_data="about1"
                    ),
                    InlineKeyboardButton(
                        text="✅ Проверить",
                        callback_data="check"
                    ),
                ],
            ],
        )
    )
    while True:
        user_id = message.from_user.id
        await asyncio.sleep(12 * 3600)
        flag = True
        for channel in get_channels(r"C:\Users\89052\projects\vpn_bot\src\channels_list.txt"):
            if (await message.bot.get_chat_member(channel, user_id)).status not in ["member", "creator", "administrator"]:
                flag = False
        if not flag: #Измени на проде!!!
            await client.update_client(user_id, False)
            await message.answer(
                text="Перепроверьте ваши подписки",
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


@dp.callback_query(F.data == "check")
async def check(callback_query: CallbackQuery):
    user_id = callback_query.from_user.id
    flag = True
    for channel in get_channels(r"C:\Users\89052\projects\vpn_bot\src\channels_list.txt"):
        if (await callback_query.bot.get_chat_member(channel, user_id)).status not in ["member", "creator", "administrator"]:
            flag = False
    if flag: #Измени на проде!!!
        response_data = await client.set_client(user_id)
        if response_data["success"] == True:
            await callback_query.bot.send_message(chat_id=-4971478443, text="ура, новый пользователь")
        await client.update_client(user_id, True)
        await callback_query.message.edit_text(
            text="🏁Всё! вы получили ДОСТУП к нашему сервису.\n\n😎Теперь вы можете наслаждаться просмотром ваших любимых видео и фильмов.\n\n⬇️Ниже вы найдёте:⬇️\n\n🧑‍🏫Инструкцию по подключению.\n\n🛟Ссылку на поддержу, которой вы сможете задать все ваши вопросы.\n",
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
            text=f"Вы не подписались на все каналы",
            reply_markup=InlineKeyboardMarkup(
                inline_keyboard=[
                    [
                        InlineKeyboardButton(
                            text="✅ Проверить",
                            callback_data="check1"
                        ),
                        InlineKeyboardButton(
                            text="🔙 Назад",
                            callback_data="back"
                        ),
                    ]
                ]
            )
        )


@dp.callback_query(F.data == "check1")
async def check(callback_query: CallbackQuery):
    user_id = callback_query.from_user.id
    flag = True
    for channel in get_channels(r"C:\Users\89052\projects\vpn_bot\src\channels_list.txt"):
        if (await callback_query.bot.get_chat_member(channel, user_id)).status not in ["member", "creator", "administrator"]:
            flag = False
    if flag: #Измени на проде!!!
        response_data = await client.set_client(user_id)
        if response_data["success"] == True:
            await callback_query.bot.send_message(chat_id=-4971478443, text="ура, новый пользователь")
        await client.update_client(user_id, True)
        await callback_query.message.edit_text(
            text="🏁Всё! вы получили ДОСТУП к нашему сервису.\n\n😎Теперь вы можете наслаждаться просмотром ваших любимых видео и фильмов.\n\n⬇️Ниже вы найдёте:⬇️\n\n🧑‍🏫Инструкцию по подключению.\n\n🛟Ссылку на поддержу, которой вы сможете задать все ваши вопросы.\n",
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
            text=f"Вы не подписались на все каналы",
            reply_markup=InlineKeyboardMarkup(
                inline_keyboard=[
                    [
                        InlineKeyboardButton(
                            text="✅ Проверить",
                            callback_data="check"
                        ),
                        InlineKeyboardButton(
                            text="🔙 Назад",
                            callback_data="back"
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
                f"✅ Ваш FREE INTERNET активирован! 🎉\n\nВаш ID: {user_id}\n\nКлюч и инструкция для подключения 👇\n", 
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
        text="йо, в разработке...",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[[
                InlineKeyboardButton(
                    text="🔙 Назад", callback_data="back1"
                )
            ]]
        )
    )


@dp.callback_query(F.data == "about1")
async def access(callback_query: CallbackQuery):
    await callback_query.message.edit_text(
        text="йо, в разработке...",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[[
                InlineKeyboardButton(
                    text="🔙 Назад", callback_data="back"
                )
            ]]
        )
    )


@dp.callback_query(F.data == "back")
async def hello(callback_query: CallbackQuery):
    await callback_query.message.edit_text(
        text="🆓FREE INTERNET🆓\n\nВы попали в VPN, который предлагает услуги платных сервисов, за БЕСПЛАТНО.\n\nНО надо выполнить одно простое условие:\n\n🔵Подписаться на ниже перечисленные телеграмм каналы. И сразу после этого вы получите доступ автоматически\n\n🔥 Наши серверы не имеют ограничений по скорости и трафику, работает на всех устройствах, платформах и приложениях.\n\n🔐 Максимальная анонимность и безопасность, которую не даст ни один сервис в мире.\n\n🚀 Получите доступ в открытый Интернет без ограничений!\n\n🤗НИЖЕ, ТЕЛЕГРАММ КАНАЛЫ НА КОТОРЫЕ НУЖНО ПОДПИСАТЬСЯ:\n\n 👉 @freeimternet",
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
        text="🆓FREE INTERNET🆓\n\nВы попали в VPN, который предлагает услуги платных сервисов, за БЕСПЛАТНО.\n\nНО надо выполнить одно простое условие:\n\n🔵Подписаться на ниже перечисленные телеграмм каналы. И сразу после этого вы получите доступ автоматически\n\n🔥 Наши серверы не имеют ограничений по скорости и трафику, работает на всех устройствах, платформах и приложениях.\n\n🔐 Максимальная анонимность и безопасность, которую не даст ни один сервис в мире.\n\n🚀 Получите доступ в открытый Интернет без ограничений!\n\n🤗НИЖЕ, ТЕЛЕГРАММ КАНАЛЫ НА КОТОРЫЕ НУЖНО ПОДПИСАТЬСЯ:\n",
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
