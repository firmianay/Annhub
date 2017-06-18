# -*- coding: utf_8 -*-
"""
通过文件 md5 查询 APP 在 virus total 的检测情况
"""

import os
import hashlib
import requests
import time
import json


apikey = "8be485b9a47980b5288c74440c0a81c7507dd50502638a878b96fe2143c10480"
URL_BASE = "https://www.virustotal.com/vtapi/v2/"
HTTP_OK = 200


def md5(filename):
    md5 = hashlib.md5()
    with open(filename, 'rb') as f:
        buf = f.read(65536)
        while buf:
            md5.update(buf)
            buf = f.read(65536)
    md5 = md5.hexdigest()
    return md5

def retrieve_files_reports(path):
    file_list = []
    for i in range(1000):
        print("开始")
        try:
            has_sent_retrieve_req = False
            file_list[:] = []
            for root, _, filenames in os.walk(path):
                for filename in filenames:
                    if not filename.endswith(".apk"):
                        file_list.append(filename)
                if len(file_list) != 0:
                    print(len(file_list))
                    for filename in file_list:
                        filename = os.path.join(root, filename)
                        md5_name = md5(filename)
                        if has_sent_retrieve_req:
                            time.sleep(20)
                        url = URL_BASE + "file/report"
                        params = {"apikey": apikey, "resource": md5_name}
                        res = requests.post(url, data=params)
                        res_json = res.json()
                        has_sent_retrieve_req = True

                        if res.status_code == HTTP_OK:
                            with open("/home/firmy/Downloads/VirusShare/report"+"/%s.json" % md5_name, "w") as f:
                                json.dump(res_json, f)
                                f.close()
                                os.rename(filename, (root+"/%s.apk" % md5_name))
                        else:
                            print("[ERROR]: %s, HTTP: %d", md5_name, res.status_code)
                else:
                    return
        except:
            print("[ERROR] 十秒后重试：")
            time.sleep(20)
            continue

def load_result(file):
    with open(file, 'r') as f:
        i = json.load(f)
        i = json.dumps(i, indent=2)
        print(i)

retrieve_files_reports("/home/firmy/Downloads/VirusShare/2")
# load_result("/home/firmy/Downloads/annhub/DownloadAPKs/virus_total_report1.json")
