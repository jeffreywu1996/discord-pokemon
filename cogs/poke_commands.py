from discord.ext import commands
from poke_client import pokedb
from utils.validate import validate_admin, validate_pokemon


class PokeCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
            print('Cog: PokeCommands is ready!')

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

    @commands.command(alias=['showmypokemon'])
    async def showpokemon(self, ctx):
        # Get pokemon collections from db
        pokemons = pokedb.get_pokemon(str(ctx.author.id))

        msg = 'Your collection: ' + ', '.join(map(str, pokemons.keys()))
        await ctx.send(msg)

    @commands.command(pass_context=True)
    async def showspawn(self, ctx):
        pokemons = pokedb.get_spawns()

        msg = 'The spawning area has: ' + ', '.join(map(str, pokemons))
        await ctx.reply(msg)


    @commands.command(pass_context=True)
    async def catch(self, ctx, pokemon):
        spawned_pokemons = pokedb.get_spawns()

        if pokemon.lower() not in spawned_pokemons:
            await ctx.send('Sorry! There are currently no '
                           '{} that you can find'.format(pokemon))
            return

        # remove one count of pokemon from db
        amount = pokedb.remove_spawn(pokemon.lower())

        await ctx.send('{} catched a {} from the island'.format(
            ctx.author.name, pokemon))

        await ctx.send('There are {} more {} in spawning area'.format(
            amount, pokemon))

        # Add pokemon to user collection
        pokedb.add_pokemon(str(ctx.author.id), pokemon.lower())
        await ctx.send('You have caught {} !'.format(pokemon))


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(PokeCommands(bot))
