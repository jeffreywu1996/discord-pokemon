import discord
from discord.ext import commands

# from poke_client import bot, pokedb
# from utils.valildate import validate_admin, validate_pokemon
import utils

@commands.command(pass_context=True)
async def spawn(ctx, *pokemons):
    # This is an admin only command
    if not validate_admin(ctx.author.id):
        await ctx.send('Sorry {}, you do not have admin privileges '
                       'to use this command!'.format(ctx.author.name))
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

async def setup(bot):
    bot.add_command(spawn)


# @bot.command(pass_context=True)
# async def showspawn(ctx):
#     pokemons = pokedb.get_spawns()
#
#     msg = 'The spawning area has: ' + ', '.join(map(str, pokemons))
#     await ctx.send(msg)
#
#
# @bot.command(pass_context=True)
# async def catch(ctx, pokemon):
#     spawned_pokemons = pokedb.get_spawns()
#
#     if pokemon.lower() not in spawned_pokemons:
#         await ctx.send('Sorry! There are currently no '
#                        '{} that you can find'.format(pokemon))
#         return
#
#     # remove one count of pokemon from db
#     amount = pokedb.remove_spawn(pokemon.lower())
#
#     await ctx.send('{} catched a {} from the island'.format(
#         ctx.author.name, pokemon))
#
#     await ctx.send('There are {} more {} in spawning area'.format(
#         amount, pokemon))
#
#     # Add pokemon to user collection
#     pokedb.add_pokemon(str(ctx.author.id), pokemon.lower())
#     await ctx.send('You have caught {} !'.format(pokemon))
#
# def setup(bot):
#     bot.add_command(spawn)
#     bot.add_command(test)
