import requests
from googletrans import Translator
from telethon import events
from telethon.tl.types import User

from userbot import CMD_HELP, LOGS, bot
from userbot.events import register
from userbot.modules.sql_helper.brend_chatbot_sql import brend, userbot, chatbot

translator = Translator()
LANGUAGE = "az"

url = "https://apitede.herokuapp.com/api/chatbot?message={message}"


async def ngapain_rep(message):
    hayulo_link_apa = url.format(message=message)
    try:
        data = requests.get(hayulo_link_apa)
        if data.status_code == 200:
            return (data.json())["msg"]
        else:
            LOGS.info("XƏTA: ChatBot funksiyası işləmir, @BrendSUP-a məlumat verin.")
    except Exception as e:
        LOGS.info(str(e))


async def chat_bot_toggle(event):
    status = event.pattern_match.group(1).lower()
    chat_id = event.chat_id
    if status == "on":
        if not brend(chat_id):
            userbot(chat_id)
            return await event.edit("✅ ChatBot Aktivdir!")
        await event.edit("✅ ChatBot Aktivləşdirildi.")
    elif status == "off":
        if brend(chat_id):
            chatbot(chat_id)
            return await event.edit("☑️ ChatBot Deaktivdir!")
        await event.edit("☑️ ChatBot Deaktivləşdirildi.")
    else:
        await event.edit("**Nümunə:** `.chatbot` <on/off>")


@register(outgoing=True, pattern=r"^\.chatbot(?: |$)(.*)")
async def on_apa_off(event):
    await chat_bot_toggle(event)


@bot.on(events.NewMessage(incoming=True, func=lambda e: (e.mentioned)))
async def brend_chatbot(event):
    sender = await event.get_sender()
    if not brend(event.chat_id):
        return
    if not isinstance(sender, User):
        return
    if event.text:
        rep = await ngapain_rep(event.message.message)
        tr = translator.translate(rep, LANGUAGE)
        if tr:
            await event.reply(tr.text)
        else:
            await event.reply(rep)
