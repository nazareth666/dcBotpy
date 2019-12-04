import discord, json, requests, urllib3, datetime


#Tokeni discordiin että saa bottiin yhteyden
TOKEN = 'NTMxNzAxNzk3NzQwNjA5NTM2.DxRyfQ.xWlWy_cKQQL-GSrLb3s5Cm9pIDs'

client = discord.Client()

#Kyrpä url tarvii vuoden, kuukauden, päivän
now = datetime.datetime.now()
day = now.day
month = now.month
year = now.year

def updateDate():
    now = datetime.datetime.now()
    day = now.day
    month = now.month
    year = now.year



url = ''
msg = ''
array = []

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):

        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    
    if message.content.startswith('!ruoka'):

        updateDate()
        array = []
        datemsg = datetime.datetime.now().strftime("%y/%m/%d")
        str1 = ''

        try:
            url = 'https://www.sodexo.fi/ruokalistat/output/daily_json/28009/'+ str(datemsg)+'/fi'
            http = urllib3.PoolManager()
            r = http.request('GET', url)
            _json = json.loads(r.data.decode('utf-8'))

            for i in _json['courses']:
                hinta = i['price']
                msg = i['title_fi']+" - "+hinta[0:4]+" €" + '\n'
                array.append(msg)       
        
            str1 = ''.join(array)
            await client.send_message(message.channel, str1)
            del str1, array

        except:
            await client.send_message(message.channel, 'Tänään ei syödäkkään ;__;')
            del str1, array
    
    if message.content.startswith('!eppu'):

        msg = 'Eppu on gay :DD :D:D'
        await client.send_message(message.channel, msg)


    if message.content.startswith('!huomenna'):

        updateDate()
        array = []
        datemsg = datetime.datetime.today() + datetime.timedelta(days=1)
        datemsg = datemsg.strftime("%y/%m/%d")
        str2 = ''

        try:
            url = 'https://www.sodexo.fi/ruokalistat/output/daily_json/28009/'+str(datemsg)+'/fi'
            http = urllib3.PoolManager()
            r = http.request('GET', url)
            _json = json.loads(r.data.decode('utf-8'))

            for i in _json['courses']:
                hinta = i['price']
                msg = i['title_fi']+" - "+hinta[0:4]+" €" + '\n'
                array.append(msg)       
        
            str2 = ''.join(array)
            await client.send_message(message.channel, str2)
            del str2, array

        except:
            await client.send_message(message.channel, 'huomenna ei syödäkkään ;__;')
            del str2, array, datemsg


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)