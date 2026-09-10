from maxrubika import Bot
from maxrubika.bot.filters import ChatType, IsText
import random
from challenges import challenges

TOKEN = "TOKEN"

bot = Bot(TOKEN)


@bot.on_new_message(ChatType("group"), IsText())
async def group_handler(bot, event):
    text = (event.text or "").strip()

    print("========== GROUP ==========")
    print("Chat ID:", event.chat_id)
    print("Text:", text)

    # اگر فقط کلمه چالش بود
    if text == "چالش":
        await event.reply(random.choice(challenges))
        return

    # اگر ابتدای پیام چالش بود (مثل: چالش @BotName)
    if text.startswith("چالش"):
        await event.reply(random.choice(challenges))
        return


@bot.on_new_message(ChatType("user"), IsText())
async def private_handler(bot, event):
    text = (event.text or "").strip()

    print("========== PRIVATE ==========")
    print("Chat ID:", event.chat_id)
    print("Text:", text)

    if text.startswith("چالش"):
        await event.reply(random.choice(challenges))


bot.run()
