from redbot.core import commands
import discord

class Info(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.command(aliases=["botinfo"])
    @commands.bot_has_guild_permissions(send_messages=True)
    @commands.has_guild_permissions(send_messages=True)
    async def about(self,ctx):
        em = discord.Embed(description=" ",color=discord.Color.purple())
        em.add_field(name="Instance owned by",value="**Ronish**:- Owner of Elixir\n**Micky**:- Cog developer of Elixir\n**𝓢𝓬𝔂𝓹𝓱𝓮𝓻**:- Cog developer of Elixir\n**Rj**:- Management of Elixir",inline=False)
        em.add_field(name="Python",value="3.8.5",inline=True)
        em.add_field(name="discord.py",value="1.5.1",inline=True)
        em.add_field(name="Red version",value="3.4.5",inline=True)
        em.add_field(name="About Elixir",value=f"This bot is an instance of [Red, an open source Discord bot](https://github.com/Cog-Creators/Red-DiscordBot) created by [Twentysix](https://github.com/Twentysix26) and [improved by many.](https://github.com/Cog-Creators)",inline=False)
        em.add_field(name="Story Behind Elixir",value="Elixir was made by Ronish and then developed by others elixir has its own [website](https://bit.ly/elixirbot) now and is also on [Top.gg](https://top.gg/bot/732916004656513077) also now elixir has a [Status Page](https://elixir.betteruptime.com/)  for any support join the [support server](https://discord.gg/padK6GW)")
        em.set_thumbnail(url="https://cdn.discordapp.com/avatars/732916004656513077/8636fca205b8c8eb71cd5f1c5ec91cd9.png?size=1024")
        await ctx.send(embed=em)
