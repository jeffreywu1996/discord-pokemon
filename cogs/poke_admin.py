import logging
from discord.ext import commands
from poke_client import pokedb
from utils.validate import validate_admin, validate_pokemon

logger = logging.getLogger(__name__)


class PokeAdmin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Cog: PokeAdmin is ready!')

    @staticmethod
    async def __validate_admin(ctx) -> bool:
        await ctx.send('WARN: This is admin only command')
        if not validate_admin(ctx.author.id):
            await ctx.send('Sorry {}, you do not have admin privileges '
                           'to use this command!'.format(ctx.author.name))
            return False
        await ctx.send(f'Admin {ctx.author.name} detected.')
        return True

    @commands.command(pass_context=True)
    async def givemepokemon(self, ctx, *pokemons) -> None:
        if not await self.__validate_admin(ctx):
            return

        if not pokemons:
            await ctx.send(
                'You must specify at least one pokemon\n'
                'Usage: !givemepokemon eevee mewtwo'
            )
            return

        added_pokemons = []
        for pokemon in pokemons:
            pokemon = pokemon.replace(",", "")  # strip comma if in pokemon names

            if validate_pokemon(pokemon):
                pokedb.add_pokemon(str(ctx.author.id), pokemon)
                added_pokemons.append(pokemon)
            else:
                await ctx.send('{} is not a valid pokemon, '
                               'cannot add to your collection.'.format(pokemon))

        if len(added_pokemons) == 0:
            await ctx.send('No pokemons added to your collections..')
            return

        msg_str = ', '.join(map(str, added_pokemons))
        await ctx.send('Added {} to your collection..'.format(msg_str))

    @commands.command(pass_context=True)
    async def spawn(self, ctx, *pokemons) -> None:
        if not await self.__validate_admin(ctx):
            return

        if not pokemons:
            await ctx.send(
                'You must specify at least one pokemon\n'
                'Usage: !givemepokemon eevee mewtwo'
            )
            return

        added_pokemons = []
        for pokemon in pokemons:
            pokemon = pokemon.replace(",", "")  # strip comma if in pokemon names
            pokemon = pokemon.lower()

            if validate_pokemon(pokemon):
                pokedb.add_spawn(pokemon)
                added_pokemons.append(pokemon)
            else:
                await ctx.send('{} is not a valid pokemon, '
                               'cannot add to the island.'.format(pokemon))

        if len(added_pokemons) == 0:
            await ctx.send('No pokemons added to spawn..')
            return

        msg_str = ', '.join(map(str, added_pokemons))
        await ctx.send('Added {} to the island..'.format(msg_str))


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(PokeAdmin(bot))