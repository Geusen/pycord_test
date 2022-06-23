import settings
import discord

bot = discord.Bot()
token = settings.TOKEN
id = int(settings.ID)
channel = int(settings.CHANNEL)

@bot.slash_command(guild_ids=[id])
async def upload(ctx):
    button = discord.ui.Button(label="pong",style=discord.ButtonStyle.green)
    view=View()
    view.add_item(button)
    await ctx.respond('test', file=discord.File('white.png'), view=view)
    await bot.close()
    exit()

bot.run(token)
