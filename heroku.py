import tweepy
import requests
import os
import discord
from keep_alive import keep_alive
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


#----------------------------------------------------------------
#JSONファイル作成
f = open('credentials.json', 'w')
f.write(os.environ['JSON'])
f.close()
f = open('client_secrets.json', 'w')
f.write(os.environ['CLIENT'])
f.close()

#Googleにログイン
gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)
os.remove('credentials.json')
os.remove('client_secrets.json')

# keyの指定
consumer_key = os.environ['CONSUMER_KEY']
consumer_secret = os.environ['CONSUMER_SECRET']
access_token = os.environ['ACCESS_TOKEN']
access_token_secret = os.environ['ACCESS_TOKEN_SECRET']

# tweepyの設定(認証情報を設定)
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# tweepyの設定(APIインスタンスの作成)
api = tweepy.API(auth, wait_on_rate_limit=True)

#LINEの設定
notify_group = os.environ['NOTIFY_GROUP']

#Discordの設定
Discord_token = os.environ['DISCORD_TOKEN']
channel_id = int(os.environ['CHANNEL_ID'])
debug_channel_id = int(os.environ['DEBUG_CHANNEL_ID'])
id = int(os.environ['ID'])
#----------------------------------------------------------------
#Discordの接続に必要なオブジェクトを生成
client = discord.Bot

#DiscordBot起動時に動作する処理
@client.slash_command(guild_ids=[id])
async def upload(ctx):
  #画像取得(時間割)
  file_id = drive.ListFile({'q': 'title = "upload.png"'}).GetList()[0]['id']
  f = drive.CreateFile({'id': file_id})
  f.GetContentFile('upload.png')
        
  #Twitterで通知
  api.update_status_with_media(status="時間割が更新されました！", filename="upload.png")
        
  #LINEで通知
  line_url = 'https://notify-api.line.me/api/notify'
  line_access_token = notify_group
  headers = {'Authorization': 'Bearer ' + line_access_token}
  line_message = '時間割が更新されました。'
  line_image = 'upload.png'
  payload = {'message': line_message}
  files = {'imageFile': open(line_image, 'rb')}
  r = requests.post(line_url, headers=headers, params=payload, files=files,)
        
  #Discordで通知
  await ctx.respond('時間割が更新されました。', file=discord.File('upload.png'))
  os.remove('upload.png')

keep_alive()
try:
  client.run(Discord_token)
except discord.errors.HTTPException:
    print("\n\n\nBLOCKED BY RATE LIMITS\nRESTARTING NOW\n\n\n")
    os.system("python restarter.py")
    os.system('kill 1')
