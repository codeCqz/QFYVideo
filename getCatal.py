import json
from hyper import HTTPConnection
import getList



url = "https://appd8lwrtt98427.pc.xiaoe-tech.com/api/xe.goods.relation.get/1.0.0"

headers = {
    ":authority":"appd8lwrtt98427.pc.xiaoe-tech.com",
    ":method":"POST",
    ":path":"/api/xe.goods.relation.get/1.0.0?app_id=appd8lwrtt98427",
    ":scheme":"https",
    "accept": "application/json, text/plain, */*",
    "accept-encoding":"gzip,deflate,br",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "app-id":"appd8lwrtt98427",

    "content-type": "application/json;charset=UTF-8",

    "cookie": 'XIAOEID=eea90c0e30b2fcf5c62458ef03afdb09; cookie_referer=https%3A%2F%2Fappd8lwrtt98427.h5.xiaoeknow.com%2F; cookie_channel=xiaoeh5; anonymous_user_key=dV9hbm9ueW1vdXNfNjMwMzkzMDNhM2MwN19rY09RcktSQTcw; sensorsdata2015jssdkcross=%7B%22%24device_id%22%3A%22182c5f64c03c9e-0d53cd09225de2-26021c51-1296000-182c5f64c04721%22%7D; channel=homepage; sa_jssdk_2015_appd8lwrtt98427_pc_xiaoe-tech_com=%7B%22distinct_id%22%3A%22u_6305f5f363dba_XbDYtEDuxM%22%2C%22first_id%22%3A%22182c5f64c03c9e-0d53cd09225de2-26021c51-1296000-182c5f64c04721%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%7D; pc_user_key=a35ab5ee6d5ac5dbd2dbf023862f8423; xenbyfpfUnhLsdkZbX=0; cookie_session_id=LqJQuO6hd5CxYcEQxxP3XIgT5BdtVo03; shop_version_type=8; LANGUAGE_appd8lwrtt98427=cn; dataUpJssdkCookie={"wxver":"","net":"","sid":""}; userInfo={"app_id":"appd8lwrtt98427","user_id":"u_6305f5f363dba_XbDYtEDuxM","wx_avatar":"https://wechatapppro-1252524126.cos.ap-shanghai.myqcloud.com/1252524126/wechatapppro/appd8lwrtt98427/image/913216e14fb50907683e3a93ec626f94.jpeg?","wx_gender":1,"birth":null,"address":null,"job":null,"company":null,"wx_account":null,"universal_union_id":null,"can_modify_phone":true,"phone":"17354605625","pc_user_key":"a35ab5ee6d5ac5dbd2dbf023862f8423","permission_visit":0,"permission_comment":0,"permission_buy":0,"pwd_isset":false,"channels":[{"type":"wechat","active":0},{"type":"qq","active":0}],"area_code":"86"}; app_id="appd8lwrtt98427"',



    "origin":"https://appd8lwrtt98427.pc.xiaoe-tech.com",
    "referer":"https://appd8lwrtt98427.pc.xiaoe-tech.com/detail/p_62b29c7de4b0ba331dcb676c/8",
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}

payload = {
    "goods_id": "p_62b29c7de4b0ba331dcb676c",
    "goods_type": 8,
    "last_id":"",
    "page_size":20,
    "resource_type": [6]
}

data = json.dumps(payload).encode()

conn = HTTPConnection('appd8lwrtt98427.pc.xiaoe-tech.com',443)

conn.request('POST', '/api/xe.goods.relation.get/1.0.0?app_id=appd8lwrtt98427', body=data, headers=headers)
resp = conn.get_response()

goods_list = json.loads(resp.read())
resp.close()

goods_list = goods_list['data']['goods_list']

for good in goods_list:
    good_title =  good['title']
    good_resource_id = good['resource_id']
    redirect_url = good['redirect_url']
    print("课程:"+good_title)
    getList.getList(good_resource_id,good_title)
