import random
from challenges import challenges

def handle_challenge(message, bot):
    if message.text == "چالش":
        bot.sendMessage(
            message.chat_id,
            random.choice(challenges)
        )
