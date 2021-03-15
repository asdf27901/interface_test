
# coding:utf-8

from config import get_authorization
import os,sys,json
sys.path.append(os.path.dirname(os.path.dirname(__file__)))


class SendRequests():
    """发送请求数据"""
    def sendRequests(self,s,apiData):
        try:
            #从读取的表格中获取响应的参数作为传递
            method = apiData["method"]
            url = apiData["url"]
            if apiData["params"] == "" and apiData["token"] == 0:
                par = None

            elif apiData["params"] != "" and apiData["token"] == 0:
                par = eval(apiData["params"])

            elif apiData["token"] == 1 :
                tok = get_authorization.get_Authorization()
                par = eval(apiData["params"])
                par['token'] = tok


            if apiData["headers"] == "":
                h = None
            else:
                h = eval(apiData["headers"])
            if apiData["body"] == "":
                body_data = None
            else:
                body_data = eval(apiData["body"])
            type = apiData["type"]
            v = False
            if type == "data":
                body = body_data
            elif type == "json":
                body = json.dumps(body_data)
            else:
                body = body_data

            #发送请求
            re = s.request(method=method,url=url,headers=h,params= par,data=body,verify=v)
            return re
        except Exception as e:
            print(e)
