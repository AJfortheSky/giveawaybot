import argparse
import time

from main import create_message, main


parser = argparse.ArgumentParser(
    prog='Discord Giveaway Manager',
)

parser.add_argument('-c', '--channel', action='store', dest='channel_id', required=True)
parser.add_argument('-e', '--emoji', action='store', dest='emoji', required=True)

args = parser.parse_args()

async def start(channel_id: str, emoji: str):
    await main()
    time.sleep(7)
    await create_message(args.channel_id, args.emoji)