from discord.ext import commands
from poke_client import pokedb


@commands.command(pass_context=True)
async def start(self, ctx):
    # Check for existing account
    if pokedb.has_account(str(ctx.message.author.id)):
        await ctx.send('{}, you already have started your journey!'.format(
                       ctx.author.name))
        return

    await ctx.send('Welcome to the Pokémon world!')
    await ctx.send('You get to choose a starter pokemon.')
    await ctx.send('Choose a starter from Bulbasaur, Charmander, Squirtle, '
                   'Treecko, Torchic, Mudkip, Turtwig, Chimchar, Piplup, '
                   'Snivy, Tepig, Oshawott, Chespin, Fennekin, Froakie, '
                   'Rowlet, Litten, Popplio')
    await ctx.send('Please enter the name of the pokemon you want as a '
                   'starter pokemon:')

    starter_pokemons = ['bulbasaur', 'charmander', 'squirtle', 'treecko',
                        'torchic', 'mudkip', 'turtwig', 'chimchar', 'piplup',
                        'snivy', 'tepig', 'oshawott', 'chespin', 'fennekin',
                        'froakie', 'rowlet', 'litten', 'popplio']

    async def check_starter(m):
        if m.content.lower() not in starter_pokemons:
            await ctx.send('The pokemon you entered is not from the starters')
            await ctx.send('Pick one from the starters above!')
            return False

        return m.author == ctx.author and m.channel == ctx.channel

    # Wait for user input
    poke_pick = await commands.wait_for('message', check=check_starter)

    # Create account with pokedb
    await ctx.send('We are getting you your {}.'.format(poke_pick.content))
    pokedb.add_user(str(ctx.author.id), poke_pick.content)
    await ctx.send('You can now set off on your journey!')


async def setup(bot):
    bot.add_command(start)