import settings
import discord

bot = discord.Bot()
token = settings.TOKEN
id = int(settings.ID)
channel = int(settings.CHANNEL)

@client.event
  async def on_ready():
      cha = bot.get_channel(channel)
      await cha.send('a', file=discord.File('white.png'))

@bot.slash_command(guild_ids=[id])
async def upload(ctx):
    await ctx.respond('test', file=discord.File('white.png'))
    await bot.close()
    exit()

bot.run(token)
