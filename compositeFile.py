from hyper import HTTPConnection
import os

def Compositefile(dirs,all_title,m3u8_fileName,dir_path,audio_url):
    print("合并ts文件中=======>")
    mp4_path = "./"+all_title+"/"
    if not os.path.exists(mp4_path):
        os.makedirs(mp4_path)

    mp4_file_name = m3u8_fileName+".mp4"
    mp4_output_path = "../" + all_title + "/"+mp4_file_name
    dir_path=dir_path+"/"
    mp4_file_path = "./"+ mp4_file_name
    mp4cmd = "cd "+dir_path+" && ffmpeg -y -f concat -i file_list.txt -c copy "+ mp4_file_path
    os.system(mp4cmd)
    print("合并MP4成功！")

    dowloadAudio(audio_url,dir_path,m3u8_fileName,mp4_file_path, mp4_output_path)

def dowloadAudio(audio_url,dir_path,m3u8_fileName,mp4_file_path, mp4_output_path):
    url = "encrypt-k-vod.xet.tech"
    path = audio_url.replace("https://encrypt-k-vod.xet.tech","")
    conn = HTTPConnection(url, 443)

    conn.request('GET', path)
    resp = conn.get_response()
    fileName =dir_path+m3u8_fileName+".mp3"
    with open(fileName, 'ab') as f:
        f.write(resp.read())
        f.close()
    mp3_file = "./"+m3u8_fileName+".mp3"
    merge(dir_path,mp4_file_path,mp3_file, mp4_output_path)

def merge(dir_path,mp4_file_path,mp3_file, mp4_output_path):
    mp3_mp4_merge = "cd "+dir_path+" && ffmpeg -i "+mp4_file_path+" -i "+mp3_file+" -c:v copy -c:a aac -strict experimental "+ mp4_output_path
    os.system(mp3_mp4_merge)
