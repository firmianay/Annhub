# -*- coding: utf_8 -*-

import hashlib
import os
from subprocess import Popen, PIPE, STDOUT

import setting

download_dir = setting.get_download_home()
analysis_dir = setting.get_analysis_home()
sdk_dir = setting.get_sdk_home()
java_dir = setting.get_java_home()

def get_apk_info(path_to_app):
    """
    获取app包名和版本号
    """
    try:
        aapt_dir = os.path.join(sdk_dir, "build-tools/25.0.2/aapt")
        aapt = Popen([aapt_dir, 'dump', 'badging', path_to_app],
                     stdout=PIPE, stdin=PIPE, stderr=STDOUT, bufsize=1)
        line = aapt.stdout.readline().decode('utf-8')
        package = line.split(" ")[1].split("'")[1]
        extension = line.split(" ")[3].split("'")[1]
        print(line)
        return package, extension
    except:
        print("获取包名和版本号失败")

def get_cert_md5(path_to_app):
    """
    获取证书md5
    """
    try:
        md5 = ""
        keytool = os.path.join(java_dir, 'bin/keytool')
        args = [keytool, '-printcert', '-jarfile', path_to_app]
        keytool_info = Popen(args, stdout=PIPE, stdin=PIPE, stderr=STDOUT, bufsize=1)
        for line in keytool_info.stdout:
            line = line.decode('utf-8', 'ignore')
            if line.startswith("\t MD5"):
                md5 = ''.join(line.split(" ")[3].split(":")[:]).replace("\n", "")
        return md5
    except:
        print("获取证书md5失败")

def get_md5(app):
    """
    计算文件md5
    """
    try:
        m = hashlib.md5()
        with open(app, 'rb') as afile:
            buf = afile.read(65536)
            while buf:
                m.update(buf)
                buf = afile.read(65536)
        return m.hexdigest()
    except:
        print("计算文件md5失败")
