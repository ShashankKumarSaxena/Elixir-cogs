from redbot.core import commands
import discord

class Links(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    @commands.bot_has_guild_permissions(send_messages=True)
    async def links(self,ctx):
        em = discord.Embed(description=" ",color=discord.Color.purple())
        em.add_field(name="🔗 Elixir Invite:-",value=f"[Elixir Invite](https://top.gg/bot/732916004656513077/invite)",inline=False)
        em.add_field(name="🔗 Elixir Support Server:-",value=f"[Support Server](https://discord.gg/padK6GW)",inline=False)
        em.add_field(name="🔗 Elixir Website:-",value=f"[Elixir Website](https://bit.ly/elixirbot)",inline=False)
        em.add_field(name="🔗 Elixir Patreon:-",value=f"[Elixir Patreon](https://www.patreon.com/join/Elixir_Bot)",inline=False)
        em.add_field(name="🔗 Elixir Premium:-",value=f"[Elixir Premium](https://bit.ly/elixirpremium)",inline=False)
        em.add_field(name="🔗 Elixir top.gg:-",value=f"[Top.gg](https://top.gg/bot/732916004656513077)",inline=False)
        em.add_field(name="🔗 Elixir Status:-",value=f"[Status](https://elixir.betteruptime.com/)",inline=False)
        em.add_field(name="🔗 Elixir Partner:-",value=f"[Elixir Partner](https://forms.gle/fFkpucye3fn9vbow8)",inline=False)
        em.set_thumbnail(url="https://cdn.discordapp.com/avatars/732916004656513077/8636fca205b8c8eb71cd5f1c5ec91cd9.png?size=256")
        em.set_image(url="https://cdn.discordapp.com/attachments/758316351407259678/847036691821887528/unknown_1.gif")
        await ctx.send(embed=em)
