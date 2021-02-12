from redbot.core import commands
import discord

class Links(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    @commands.bot_has_guild_permissions(send_messages=True)
    async def links(self,ctx):
        em = discord.Embed(description=" ",color=discord.Color.purple())
        em.add_field(name="Elixir Invite:-",value=f"[Invite](https://top.gg/bot/732916004656513077/invite)",inline=False)
        em.add_field(name="Elixir Support Server:-",value=f"[Support Server](https://discord.gg/padK6GW)",inline=False)
        em.add_field(name="Elixir Website:-",value=f"[Elixir Website](https://bit.ly/elixirbot)",inline=False)
        em.add_field(name="Elixir Premium:-",value=f"[Premium](https://bit.ly/elixirpremium)",inline=False)
        em.add_field(name="Elixir top.gg:-",value=f"[top.gg](https://top.gg/bot/732916004656513077)",inline=False)
        em.add_field(name="Elixir Status:-",value=f"[Status](https://elixir.betteruptime.com/)",inline=False)
        await ctx.send(embed=em)
