import discord
# from discord.ext import commands
from redbot.core import commands
import sys
import json
# from cogs.utils.checks import load_moderation


HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKCYAN = '\033[96m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

class Setup(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.command()
    @commands.bot_has_permissions(manage_channels=True)
    @commands.has_permissions(manage_channels=True)
    async def setup(self,ctx):
        '''
        Setup the bot in your server with this command.
        '''

        #=========================== VERY OLD =======================================#
        # guild = ctx.guild
        # member = ctx.author
        # mods = load_moderation()
        # mod_role_strings = mods[ctx.message.guild.name]
        # mod_roles = []
        # try:
        #     for m in mod_role_strings:
        #         mod_roles.append(discord.utils.get(ctx.message.guild,name=m))
        # except:
        #     mod_roles = []
        
        # overwrites = {
        #     guild.default_role: discord.PermissionOverwrite(read_messages=False),
        #     guild.me: discord.PermissionOverwrite(read_messages=True),
        # }
        # for m in mod_roles:
        #     await ctx.channel.set_permissions(m,read_messages=True,send_messages=True)
        # await guild.create_text_channel("thecoderzbot-private",overwrites=overwrites)
        # await ctx.send("Setup the bot in your guild!")
        #=============================================================================#

        # TODO - A VERY GOOD SETUP COMMAND SOOONN!!

        setup_channel = await ctx.guild.create_text_channel(f"{self.bot.user.name}-private")
        await setup_channel.set_permissions(ctx.guild.get_role(ctx.guild.id),
                                             send_messages=False,
                                             read_messages=False)

        em = discord.Embed(description=" ",color=discord.Color.purple())
        em.add_field(name="What is this channel for?",value="This channel is made for you to get regular updates about bot. All the changelogs/update logs/bug fixes / official giveaways will be sent here.",inline=False)
        em.add_field(name="__Important Notes__",value="• Do not rename this channel.\n• You can test bot's commands here if you want to.",inline=False)
        em.add_field(name="__Important Links__",value=f"[Support Server](https://discord.gg/padK6GW) | [Invite Me](https://top.gg/bot/732916004656513077/invite)")
        own = self.bot.get_user(728183506953437185)
        em.set_author(name=f"{own.name}#{own.discriminator}",icon_url=own.avatar_url)
        await setup_channel.send(embed=em)
