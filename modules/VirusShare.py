# -*- coding: utf_8 -*-
"""
清洗VirusShare样本库
"""

import os
import shutil
import zipfile

import setting

virus_dir = "/home/firmy/Downloads/VirusShare"
error_dir = setting.get_error_home()

error_num = 0
fine_num = 0

for _, _, filenames in os.walk(virus_dir):
    for file in filenames:
        path = os.path.join(virus_dir, file)
        try:
            zip = zipfile.ZipFile(path)
            multi_flag = 0
            for f in zip.namelist():
                if f == "AndroidManifest.xml":
                    multi_flag += 1
                    if multi_flag > 1:
                        error_num += 1
                        shutil.move(path, error_dir)
            if multi_flag == 0:
                error_num += 1
                shutil.move(path, error_dir)
            else:
                fine_num += 1
        except:
            error_num += 1
            shutil.move(path, error_dir)

print("有效APK数量: " + str(fine_num))
print("无效APK数量: " + str(error_num))
