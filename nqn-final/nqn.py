# from discord.ext import commands
from redbot.core import commands
from discord import utils
import discord
import json
import sys

class NQN(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
	
	@commands.group(pass_context=True)
	async def nqn(self,ctx):
		# if ctx.invoked_subcommand is None:
		# 	helper = str(ctx.invoked_subcommand) if ctx.invoked_subcommand else str(ctx.command)
        # 	await ctx.send(f"{ctx.author.name} To use this command - ")
        # 	await ctx.send_help(helper)
		pass

	@nqn.command()
	async def enable(self,ctx):
		with open(f'{sys.path[0]}\\cogs\\flags.json','r') as f:
			data = json.load(f)
		try:
			if data[f"{ctx.guild.id}"] == "True":
				return await ctx.send("NQN is already enabled for this server!")
		except KeyError:
			data[f"{ctx.guild.id}"] = "True"
			with open(f"{sys.path[0]}\\cogs\\flags.json",'w') as f:
				json.dump(data, f,indent=4)
		else:
			data[f"{ctx.guild.id}"] = "True"
			with open(f'{sys.path[0]}\\cogs\\flags.json','w') as f:
				json.dump(data, f, indent=4)
		await ctx.send("NQN is now enabled for this server!")
	
	@nqn.command()
	async def disable(self,ctx):
		with open(f'{sys.path[0]}\\cogs\\flags.json','r') as f:
			data = json.load(f)
		try:
			if data[f"{ctx.guild.id}"] == "False":
				return await ctx.send("NQN is already disabled for this server!")
		except KeyError:
			data[f"{ctx.guild.id}"] = "False"
			with open(f'{sys.path[0]}\\cogs\\flags.json','w') as f:
				json.dump(data, f, indent=4)
		else:
			data[f"{ctx.guild.id}"] = "False"
			with open(f'{sys.path[0]}\\cogs\\flags.json','w') as f:
				json.dump(data, f, indent=4)
		await ctx.send("NQN is now disabled for this server!")

	async def getemote(self, arg):
		emoji = utils.get(self.bot.emojis, name = arg.strip(":"))

		if emoji is not None:
			if emoji.animated:
				add = "a"
			else:
				add = ""
			return f"<{add}:{emoji.name}:{emoji.id}>"
		else:
			return None

	async def getinstr(self, content):
		ret = []

		spc = content.split(" ")
		cnt = content.split(":")

		if len(cnt) > 1:
			for item in spc:
				if item.count(":") > 1:
					wr = ""
					if item.startswith("<") and item.endswith(">"):
						ret.append(item)
					else:
						cnt = 0
						for i in item:
							if cnt == 2:
								aaa = wr.replace(" ", "")
								ret.append(aaa)
								wr = ""
								cnt = 0

							if i != ":":
								wr += i
							else:
								if wr == "" or cnt == 1:
									wr += " : "
									cnt += 1
								else:
									aaa = wr.replace(" ", "")
									ret.append(aaa)
									wr = ":"
									cnt = 1

						aaa = wr.replace(" ", "")
						ret.append(aaa)
				else:
					ret.append(item)
		else:
			return content

		return ret


	# i added extra indent by mistake -_-

	@commands.Cog.listener()
	async def on_message(self, message):
		with open(f'{sys.path[0]}\\cogs\\flags.json', 'r') as f:
			data = json.load(f)
		
		try:
			if data[f"{message.guild.id}"] == "True":
				if message.author.bot:
					return

				if ":" in message.content:
					msg = await self.getinstr(message.content)
					ret = ""
					em = False
					smth = message.content.split(":")
					if len(smth) > 1:
						for word in msg:
							if word.startswith(":") and word.endswith(":") and len(word) > 1:
								emoji = await self.getemote(word)
								if emoji is not None:
									em = True
									ret += f" {emoji}"
								else:
									ret += f" {word}"
							else:
								ret += f" {word}"

					else:
						ret += msg
					

					if em:
						webhooks = await message.channel.webhooks()
						webhook = utils.get(webhooks, name = "Elixir NQN")
						if webhook is None:
							webhook = await message.channel.create_webhook(name = "Elixir NQN")

						await webhook.send(ret, username = message.author.name, avatar_url = message.author.avatar_url)
						await message.delete()
		except KeyError:
			pass

# def setup(bot):
# 	bot.add_cog(nqn(bot))
# 	print("NQN is ready to give free nitro") # NO NEED FOR RED

    
