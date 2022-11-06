from Crypto.Util.Padding import pad
from hyper import HTTPConnection
import compositeFile
from Crypto.Cipher import AES


import os

# url = https://encrypt-k-vod.xet.tech/
# 529d8d60vodtransbj1252524126/
# 4d07d4b7387702302389449247/drm
# /v.f421220_0.ts
# ?start=0
# &end=112991
# &type=mpegts
# &sign=66e0217f41807d485c22df2db3a2cb00
# &t=63247515
# &us=ptTPWDTNkh
# &whref=appd8lwrtt98427.pc.xiaoe-tech.com

def DownloadVedio(m3u8_fileName,audio_url,fileName,path,param,ts_path,all_title):
    #m3u8_fileName没有后缀名的name,做路径备用
    dir_path = "./" + m3u8_fileName
    dirs = dir_path+"/"

    print("视频下载中======>")
    # file_name读取文件名
    path = path.split('?')[0].replace("m3u8","ts")
    ts_name = path.split("/")[len(path.split("/"))-1]

    with open(fileName, "r+") as f:
        lines = f.readlines()
        f.close()
    i = 0
    print("解析m3u8文件并下载ts文件中======>")
    for line in lines:
        line = str(line)
        if 'EXT-X-KEY' in line:
            print("获取key======>")
            index_start = line.index('URI="')
            index_end = line.index('",')
            url = line[int(index_start) + 5:int(index_end)]
            index_start = line.index('IV=')
            iv = line[int(index_start) + 3:]
            vt = iv.replace("0x", "")[:16].encode()
            param = url.split("?")[1]
            url = url.split("?")[0].replace("https://", "")
            uri = url.split("/")[1]
            url = url.split("/")[0]
            path = "/" + uri + "?" + param
            headers = {
                ":authority": "app.xiaoe-tech.com",
                ":method": "GET",
                ":path": path,
                ":scheme": "https",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
            }

            conn = HTTPConnection(url, 443)

            conn.request('GET', path, headers=headers)
            resp = conn.get_response()

            key = resp.read()


            cryptor = AES.new(key, AES.MODE_CBC,key)
            print("获取成功,开始下载并解密ts文件，请耐心等候=====>")
            # ts_path
        if '.ts?' in str(line):
            line = line.replace("\n","")
            ts_url_part =  ts_path + line
            headers = {
                "Host": "encrypt-k-vod.xet.tech",
                "Origin": "https://appd8lwrtt98427.pc.xiaoe-tech.com",
                "Referer": "https://appd8lwrtt98427.pc.xiaoe-tech.com/",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
            }
            conn = HTTPConnection("encrypt-k-vod.xet.tech", 443)
            conn.request('GET', ts_url_part, headers=headers)

            resp = conn.get_response()


            dir_path = "./" + m3u8_fileName

            fileName = dir_path + "/" + ts_name + "_" + str(i) + ".ts"

            ffmpeg_ts_list = dir_path + "/" + "file_list.txt"

            ts_file_name = "file" + "  '" + ts_name + "_" + str(i) + ".ts" + "'" + "\n"
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)
            with open(ffmpeg_ts_list, 'a+') as f:
                f.write(ts_file_name)
                f.close()

            with open(fileName, 'ab') as ts:
                # 解密
                encrypted_data = resp.read()
                # 获取长度
                encrypted_data_len = len(encrypted_data)
                # 判断当前的数据长度是不是16的倍数
                if encrypted_data_len % 16 != 0:
                    # 把长度不是16的倍数的显示出来
                    # 变为16的倍数
                    encrypted_data = pad(encrypted_data, 16)
                # 进行解密
                decrypt_data =  cryptor.decrypt(encrypted_data)
                # 将解密后的数据写入对应的解密文件
                ts.write(decrypt_data)
                ts.close()

            i = i + 1
            resp.close()

    print('下载ts文件完毕')
    compositeFile.Compositefile(dirs,all_title,m3u8_fileName,dir_path,audio_url)

