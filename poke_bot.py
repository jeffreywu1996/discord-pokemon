import os
import logging
import aiohttp
import discord
from discord.ext import commands, tasks

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)



class PokeBot(commands.Bot):
    def __init__(self, intents):

        super().__init__(command_prefix='!', intents=intents)
        self.session = None
        self.initial_extensions = [
            # 'cogs.test',
            'cogs.poke_admin',
            'cogs.poke_commands',
        ]

    async def setup_hook(self):
        # self.background_task.start()
        self.session = aiohttp.ClientSession()
        for ext in self.initial_extensions:
            await self.load_extension(ext)

    async def close(self):
        await super().close()
        await self.session.close()

    # @tasks.loop(minutes=1)
    # async def background_task(self):
    #     print('Running background test...')

    async def on_ready(self):
        logging.info('PokeBot is online!')


if __name__ == "__main__":
    intents = discord.Intents.all()
    intents.members = True

    TOKEN = os.environ['TOKEN']
    bot = PokeBot(intents=intents)
    bot.run(TOKEN)