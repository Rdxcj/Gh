import requests
import re
import json
import os
from pathlib import Path
session = requests.session()

#path = Path("cookies.json")
#Cookies = json.loads(path.read_bytes())
Cookies = {"csrftoken": "nStbIsIYUO0X295MwaOVbjFAaqso2g9p", "rur": "\"CCO\\0548510847248\\0541751905491:01f7eae16c1314ba80ecbef1455f19ddbfc1f89a4c275e27db21a79eea89ad661d92e577\"", "mid": "Zki-HwALAAHGxyPe3ATMxcewqF5-", "ds_user_id": "8510847248", "ig_did": "174B4DF3-F44A-43B1-8FE5-B65885FB0256", "sessionid": "8510847248%3A13LbljrII1IAmd%3A18%3AAYdyWz2pCoG0uD7qyQLWzCZ2qhp3Cm_XJBGMQ2sEbw"}


csrf = Cookies["csrftoken"]
id = Cookies["ds_user_id"]

cookies = requests.utils.cookiejar_from_dict(Cookies)
session.cookies.update(cookies)

headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'no-cache',
    'Pragma': 'no-cache',
    'Priority': 'u=1, i',
    'Referer': 'https://www.instagram.com/settings/help/account_status/?hl=en',
    'sec-ch-prefers-color-scheme': 'light',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    'x-csrftoken': f'{csrf}',
    'x-ig-app-id': '936619743392459',
    'X-Requested-With': 'XMLHttpRequest',
}


session.headers = headers
data = {
    'broadcast_message': 'Horror nights with evil within 2',
    'internal_only': 'false',
    'preview_height': '1920',
    'preview_width': '1080',
    'source_type': '5',
    'broadcast_type': 'RTMP',
    'visibility': '0',
}


#res = session.post("https://www.instagram.com/api/v1/live/create/", params={'hl': 'en'}, data=data)
#p6 = res.json()
#print(p6)
#broadcastid = p6['broadcast_id']
#upload_url = p6['upload_url']
#print(upload_url)
#print(broadcastid)


#rr = session.post(f"https://www.instagram.com/api/v1/live/{broadcastid}/start/", data={'should_send_notifications': 1})

headers = {
    'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-platform': '"Android"',
    'dnt': '1',
    'sec-ch-ua-mobile': '?1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Mobile Safari/537.36',
    'content-type': 'application/json',
    'accept': '*/*',
    'origin': 'https://dlive.tv',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://dlive.tv/',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
    'priority': 'u=1, i',
}

json_data = {
    'playlisturi': 'https://livestreamb.prdv3.dlivecdn.com/dlive-05900794/1720443826/src/live.m3u8'
}

esponse44 = requests.post('https://live.prd.dlive.tv/hls/sign/url', headers=headers, json=json_data).text
print(esponse44)

os.system(f"ffmpeg -headers $'User-Agent: Mozilla/5.0 (Android; vivo V2311) Android/14 version/1.17.74\r\nHost: livestreamc.prdv3.dlivecdn.com\r\nConnection: Keep-Alive\r\nAccept-Encoding: identity\r\nReferer: https://dlive.tv/\r\n' -re -i '{esponse44}' -threads 4 -vcodec libx264 -b:v 6000k -acodec aac -preset ultrafast -f flv 'rtmp://alpush.rtmp.nimo.tv/live/su2299515339885rcaf93ac2e0aee5c25cedf5d4c5fadf81?guid=0aa89b1d4ad38c663d01621d631d83b1&hyapp=81&hymuid=2299515339885&hyroom=4490358181&psign=5b93a4a7d8f12db17a80e3ad7d14dcd8&rtag=cah5FXgQJ9&sru=71C44B2I1&txHost=txpush.rtmp.nimo.tv&ua=d2ViJjEuMC40Jm5pbW9UVg==&appid=81&room=4490358181&muid=4599030693329&seq=1720507838506&streamcode=huya_inner_user'")
