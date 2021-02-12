# from redbot.core import commands
import redbot
from discord.ext import commands
import discord


class Suggest(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    @commands.bot_has_guild_permissions(send_messages=True)
    @commands.has_guild_permissions(send_messages=True)
    async def suggest(self,ctx,*,msg):
        suggestion_channel = 733962142604328970
        # suggestion_channel = 801853625877266443 # TEST CHANNEL
        # suggestion_channel = 732941183478661154 # PVT CHANNEL
        channel = discord.utils.get(self.bot.get_all_channels(),id=suggestion_channel)
        webhook_list = await channel.webhooks()
        webhook_names= []
        for webhook in webhook_list:
            webhook_names.append(webhook.name)
        if "Suggestions | Elixir" not in webhook_names:
            suggestion_hook = await channel.create_webhook(name="Suggestions | Elixir")
        else:
            elixir_server = 732941183478661151
            server = await self.bot.fetch_guild(elixir_server)
            suggestion_hook = discord.utils.get(await server.webhooks(),name="Suggestions | Elixir")
        em = discord.Embed(description=" ",color=discord.Color.purple())
        em.add_field(name=f"Suggestion by {ctx.message.author} ({ctx.message.author.id})",value=f"```\n{msg}```")
        em.set_footer(text="To add your suggestions use `suggest` command!")
        await suggestion_hook.send(embed=em,avatar_url="https://cdn.discordapp.com/avatars/732916004656513077/8636fca205b8c8eb71cd5f1c5ec91cd9.png?size=1024")
        await ctx.send("Done! Your suggestion was sent to Elixir Support Server")

        
