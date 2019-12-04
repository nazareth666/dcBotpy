import json, requests, urllib3, datetime

now = datetime.datetime.now()
day = now.day
month = now.month
year = now.year
array = []
# url = 'https://www.sodexo.fi/ruokalistat/output/daily_json/28009/2019/01/07/fi'
url = 'https://www.sodexo.fi/ruokalistat/output/daily_json/28009/'+ str(year) +'/'+str(month)+'/07/fi'

http = urllib3.PoolManager()

r = http.request('GET', url)
_json = json.loads(r.data.decode('utf-8'))


for i in _json['courses']:
    hinta = i['price']
    msg = i['title_fi']+" - "+hinta[0:4]+" €" + '\n'
    array.append(msg)

str1 = ''.join(array)
print(str1)


