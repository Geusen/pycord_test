import settings
from time import sleep
import discord

bot = discord.Bot()
token = settings.TOKEN
id = int(settings.ID)
channel = int(settings.CHANNEL)

@bot.event
async def on_ready():
    cha = bot.get_channel(channel)
    await bot.change_presence(activity=discord.Game(name="Hollow Knight"))
    #await cha.send('a', file=discord.File('white.png'))

@bot.slash_command(guild_ids=[id])
async def upload(ctx):
    await ctx.respond('test', file=discord.File('white.png'))
    await bot.close()
    exit()

@bot.slash_command(guild_ids=[id], description="退出")
async def exit(ctx):
    cha = bot.get_channel(channel)
    #await cha.send('a', file=discord.File('white.png'))
    await ctx.respond('exit.')
    #await ctx.respond('exit.', delete_after=1)
    #sleep(3)
    await bot.close()
    exit()

bot.run(token)
