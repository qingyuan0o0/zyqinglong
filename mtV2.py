# -*- coding:utf-8 -*-
"""
美团 外卖红包
自行捉包把meituan.com里面的token(一般在请求头里)填到变量 meituanCookie 中,
多账号换行或&隔开
export meituanCookie="AgGZIgsYHyxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

cron: 0 0,6 * * *
const $ = new Env("美团领杂券");
"""
import requests,re,json,time,os
from urllib.parse import urlparse, quote
#最好设置meituanuserId,未测试未设置是否可用
#分割变量
if 'meituanCookie' in os.environ:
    meituanCookie = re.split("@|&",os.environ.get("meituanCookie"))
    print(f'查找到{len(meituanCookie)}个账号')
else:
    meituanCookie = ['']
    print('无meituanCookie变量')
if 'meituanjingweidu' in os.environ:
    meituanjingweidu = re.split("@|&",os.environ.get("meituanjingweidu"))
else:
    meituanjingweidu = ['']
    print('无meituan经纬度变量,可以去https://lbs.amap.com/tools/picker获取')

def grab_red_packet(token):
    session = requests.Session()
    headers = {
    "Host": "mediacps.meituan.com",
    "Connection": "keep-alive",
    "Content-Length": "3774",
    "Accept": "application/json, text/plain, */*",
    "mtgsig": '{"a1":"1.1","a2":1731292525105,"a3":"89138114w5835y05yu63wx89wuv9057w806951z9wv4979581236z2yw","a5":"xyZwkFw5yqP0UAfLnjHKRO8YVhAJCRJAIc==","a6":"h1.5HRU1oqS5D37XBQVIU//w7cWodbE5xVYKYCWrCnviHzEO9agDQSDIxEKRf0JSxkcslCTYphlWUBvLz+lKYIFYIIoEk97z5mda2f6o/Q7ODR92bndlhJ4VP+OMydprLklEbwm4AuziiwPGaW8nqzyJ52YUF0tRWgeKnvvhfE/EZOsz2UiXXDPFrVHwiNgyK9RMJaVlQfQGyKrDWJVOw5rLN6ceqDBRsHQ/xVvblZEDMCJG7bMxiv40nSYm+vDFdf8zoVG42Dv6F1K7PzXQwf7XtjfrN6qrB8jl+Bp4hP7++gNJmOZIdFg4ZlhT5etaL5OkDdHZRFkTPCugtDmA1XX7BCcvyN5/IsBWP8+HqDeQZOy1l5RMV5S5M4ssK541N3u7","x0":4,"d1":"d55e010f1365b83549a3830dc63bb920"}'，
    "User-Agent": "Mozilla/5.0 (Linux; Android 14; MAG-AN00 Build/HONORMAG-AN00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",
    "Content-Type": "application/json;charset=UTF-8",
    "Origin": "https://market.waimai.meituan.com",
    "Sec-Fetch-Site": "same-site",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://market.waimai.meituan.com/",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    }

    data = {"gundamId":531693,"instanceId":"17211892932540.47486483758713405","actualLongitude":"jingdu","actualLatitude":"weidu","needTj":False,"couponConfigIdOrderCommaString":"620969479,2189245219456,4298495230601,19537962926729,18884585587337,18276698358409,16307505791625,62530784070180,18774632104585,15298586739337,14306960212617,14314041377417,14316668846729,14315327914633,14306048017033,19404857475721,19699208618633,17136646619785,19202122187401,17260211208841,14673728045705,29350343345426,19531471061641,19201180107401,19695138112137,5513815065225,603844019,11983002534537,14684898984585,14686298178185,14407293272713,14686779867785,8650758750857,9285949325961,7458408104585,11980394594953，19483472822921,10385596023433,14578173543049,9137512120969,17800681685641,17802094051977,11131204469385,18416437363337,19473339646601,20046921138825,19737894257289,19713633550985,20446261150345,20501582447241,20101111087753,6080193102473,2430972598746,21425205740169,21421333283465,20326355698313,21792222151305,21792985055881,21794667037321,21792343196297,21792343130761,21792985449097,21792222282377,21792985383","couponAllConfigIdOrderString":"620969479,2189245219456,4298495230601,19537962926729,18884585587337,18276698358409,16307505791625,62530784070180,18774632104585,15298586739337,14306960212617,14314041377417,14316668846729,14315327914633,14306048017033,19404857475721,19699208618633,17136646619785,19202122187401,17260211208841,14673728045705,29350343345426,19531471061641,19201180107401,19695138112137,5513815065225,603844019,11983002534537,14684898984585,14686298178185,14407293272713,14686779867785,8650758750857,9285949325961,7458408104585,11980394594953,19483472822921,10385596023433,14578173543049,9137512120969,17800681685641,17802094051977,11131204469385,18416437363337,19473339646601,20046921138825,19737894257289,19713633550985,20446261150345,20501582447241,20101111087753,6080193102473,2430972598746,21425205740169,21421333283465,20326355698313,21792222151305,21792985055881,21794667037321,21792343196297,21792343130761,21792985449097,21792222282377,21792985383","ctype":"wxapp","platform":11,"app":-1,"h5Fingerprint":"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"，"appletAppid":""，"appletExpoid":""}
    jingdu_str, weidu_str = meituanjingweidu.split(',')
    jingdu = jingdu_str.replace('.', '')  # 去掉小数点
    weidu = weidu_str.replace('.', '')  # 去掉小数点
    jingdu = jingdu.ljust(8, '0')  # 经度补齐到8位
    weidu = weidu.ljust(8, '0')  # 纬度补齐到8位
    data["actualLongitude"] = jingdu
    data["actualLatitude"] = weidu
    m = requests.get('https://mtck.iw.mk/get_cookies').json() #获取最新ck提升稳定性
    m['latlng'] = "%s,1731292506722" % meituanjingweidu,int(round(time.time() * 1000))
    m['_lxsdk'] = m['_lxsdk_cuid']
    m['userId'] = meituanuserId
    m['token'] = token
    # 将 Cookies 转换为字符串
    cookie_str = "; ".join([f"{key}={value}" for key, value in m.items()])
    headers["Cookie"] = cookie_str
#    print(cookie_str)

    # 发送请求
    url = "https://mediacps.meituan.com/gundam/gundamGrabV4?gdBs=&pageVersion=1731060831622&yodaReady=h5&csecplatform=4&csecversion=2.4.0"
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        print("领取成功:")
        b = response.json()
#        print(b)
        print(f"获得{len(b['data']['allCoupons'])}张优惠券")
        for sj in b['data']['allCoupons']:
             print(f"{sj['couponName']}-{sj['amountLimit']}-{sj['couponAmount']}元-{sj['amountLimit']}-{sj['etime']}")
    else:
        print("请求失败:", response.status_code, response.text)


if __name__ == "__main__":
    z = 1
    for ck in meituanCookie:
        try:
            print(f'登录第{z}个账号')
            print('----------------------')
            try:
                print('-----外卖-----')
                grab_red_packet(ck)
                print('-------------')
            except Exception as e:
                print('错误')
