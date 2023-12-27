import hikari
from config import TOKEN
from db_handler import database_shit

bot = hikari.GatewayBot(token=TOKEN, intents=hikari.Intents.ALL)  # TODO Replace TOKEN with your bot's token

monitor_msg = []


@bot.listen(hikari.StartedEvent)
async def start(event):
    if event:
        await create_message(1056868091889455165,
                             '✨')  # TODO Specify here the channel id and the emoji that should be used


async def create_message(channel_id, emoji):
    temp_id = await bot.rest.create_message(
        channel=channel_id,
        content=hikari.Embed(title='Test', description='Test')  # TODO Make your own embed
    )

    message_id = temp_id.id
    await bot.rest.add_reaction(message=message_id, emoji=emoji, channel=channel_id)

    monitor_msg.append(message_id)


@bot.listen(hikari.GuildReactionAddEvent)
async def monitor_message(event=hikari.GuildReactionAddEvent):
    db_vals = []
    msg_id = monitor_msg.copy()
    if event.message_id == msg_id.pop(0):
        db_vals.append(event.member.user.id)
        db_vals.append(event.member.user.username)
        database_shit(db_vals)
        db_vals = []


def main():
    bot.run()


if __name__ == '__main__':
    main()
