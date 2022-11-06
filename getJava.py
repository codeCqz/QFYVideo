import json
from hyper import HTTPConnection
import downloadVedio

def getM3u8(filename,audio_url,video_url,sign,t,url,path,param,ts_path,all_title):
   # url = "https://pri-cdn-tx.xiaoeknow.com/appd8lwrtt98427/private_index/1663078523vUR13Q.m3u8"

    headers = {
        "Host":"encrypt-k-vod.xet.tech",
        "origin": "https://appd8lwrtt98427.pc.xiaoe-tech.com",
        "referer": "https://appd8lwrtt98427.pc.xiaoe-tech.com/",
        "sec-ch-ua ": '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105""',
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
    }




    conn = HTTPConnection("encrypt-k-vod.xet.tech", 443)


    conn.request('GET', url=path, headers=headers)
    resp = conn.get_response()

    m3u8_fileName = filename.replace('.mp4','')



    fileName = m3u8_fileName+".m3u8"
    with open(fileName, mode="wb") as f:
        f.write(resp.read())
        f.close()


    resp.close()
    print("下载m3u8文件成功！")
    downloadVedio.DownloadVedio(m3u8_fileName,audio_url,fileName,path,param,ts_path,all_title)


