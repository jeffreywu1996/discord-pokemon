# import discord
# from discord.ext import commands
import pokepy
# import logging
import os
# import asyncio
# import beckett.exceptions
# from commands.test import Test

import pokedb

# Set up logging
# logger = logging.getLogger('discord')
# logger.setLevel(logging.DEBUG)
# handler = logging.FileHandler(filename='discord.log', encoding='utf-8',
#                               mode='w')
# handler.setFormatter(
#         logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
# logger.addHandler(handler)

# Gets bot token from env
TOKEN = os.environ.get('TOKEN')

# Launches pokedb and pokepy clients
pokepy_client = pokepy.V2Client()
pokedb = pokedb.PokeDB()

# Launch discord bot client
# intents = discord.Intents.all()
# intents.members = True
# bot = commands.Bot(command_prefix='!', intents=intents)
#
# # Set admin_whitelist
# admin_whitelist = {
#     402615595943854080,   # Jeff's
#     404065314201010176    # Connor's
# }


# @bot.event
# async def on_ready():
#     logger.info('Logged in as:\n{0} (ID: {0.id})'.format(bot.user))
#
# @bot.command(pass_context=True)
# async def test2(ctx):
#     await ctx.send('test2!')

# async def main():
#     await bot.load_extension('cogs.test')
#     TOKEN = 'NTg1Njk4Mzg4MjI2NDczOTg3.GCqsO2.TWKikmvuWRnL7MdC0air_5LB2Q6PdxllOKL4FU'
#     await bot.start(TOKEN)
#
# asyncio.run(main())


# async def main():
#     await bot.load_extension('cogs.test')
#     TOKEN = 'NTg1Njk4Mzg4MjI2NDczOTg3.GCqsO2.TWKikmvuWRnL7MdC0air_5LB2Q6PdxllOKL4FU'
#     bot.run(TOKEN)
#
# main()
