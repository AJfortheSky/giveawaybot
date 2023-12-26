import hikari
from venv.config import TOKEN
from db_handler import database_shit

bot = hikari.GatewayBot(token=TOKEN, intents=hikari.Intents.ALL)



async def create_message(channel_id, emoji):
    temp_id = await bot.rest.create_message(
        channel=channel_id,
        content=hikari.Embed(title='Test', description='Test')
    )

    message_id = temp_id.id
    await bot.rest.add_reaction(message=message_id, emoji=emoji, channel=channel_id)

    await monitor_message(message_id=message_id)


@bot.listen(hikari.GuildReactionAddEvent)
async def monitor_message(event=hikari.GuildReactionAddEvent, message_id=int):
    db_vals = []
    if event.message_id == message_id and event.emoji_name == '✨':
        db_vals.append(event.member.user.id)
        db_vals.append(event.member.user.username)
        database_shit(db_vals)
        db_vals = []


def main():
    bot.run()


if __name__ == '__main__':
    main()
