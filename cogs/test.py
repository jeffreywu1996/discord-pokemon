from discord.ext import commands


class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is online!')

    # @app_commands.command(name="command-1")
    # async def test(self, interaction: discord.Interaction) -> None:
    #     print('spawned!')
    #     await interaction.response.send_message('spawned', ephemeral=True)
    @commands.command()
    async def test(self, ctx) -> None:
        print('spawned!')
        await ctx.send('spawned')


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Test(bot))