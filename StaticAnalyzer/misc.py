# -*- coding: utf_8 -*-

import hashlib
import os
from subprocess import Popen, PIPE, STDOUT

import setting

java_dir = setting.get_java_home()
sdk_dir = setting.get_sdk_home()
analysis_dir = setting.get_analysis_home()


def file_size(path_to_app):
    """
    计算apk大小
    """
    size = round(float(os.path.getsize(path_to_app)) / (1024 * 1024), 2)
    size_str = str(size)
    return size_str


def file_name(path_to_app):
    """
    获取apk应用名称 
    """
    aapt_dir = os.path.join(sdk_dir, "build-tools/25.0.2/aapt")
    aapt = Popen([aapt_dir, 'dump', 'badging', path_to_app],
                 stdout=PIPE,stdin=PIPE, stderr=STDOUT, bufsize=1)
    flag = 0
    for line in aapt.stdout:
        line = line.decode('utf-8', 'ignore')
        if line.startswith("package:"):
            package = line.split(" ")[1].split("'")[1]
        if line.startswith("launchable-activity"):
            name = ''.join(line.split("=")[2].split("'")[1])
            if name != "":
                flag = 1
    if flag == 0:
        name = package
        return name
    else:
        return name


def strings_aapt(path_to_app):
    """
    使用 aapt 获取app里的字符串
    数据量较少
    """
    print("开始扫描字符串: %s" % path_to_app)
    try:
        lines = []
        strings_dic = []
        aapt = os.path.join(sdk_dir, "build-tools/25.0.2/aapt")
        aapt_xmls = Popen([aapt, 'dump', 'strings', path_to_app], stdout=PIPE, stderr=STDOUT)
        for line in aapt_xmls.stdout:
            line = line.decode('utf-8', "ignore").replace("\n", "").split(" ")[-1]
            if line.endswith(".xml"):
                lines.append(line)
        for line in lines:
            aapt_strings = Popen([aapt, 'dump', 'xmlstrings', path_to_app, line], stdout=PIPE, stderr=STDOUT)
            for string in aapt_strings.stdout:
                string = string.decode('utf-8', 'ignore').replace("\n", "").split(" ")[-1]
                if string != "" and string != "\"" and string != "\'":
                    strings_dic.append(string)
        strings = list(set(strings_dic))
        print("字符串扫描完成")
        return strings
    except:
        print("字符串扫描失败")


# TODO
def strings_ClassyShark():
    """
    使用 ClassyShark 获取字符串
    数据量较多
    """
    pass


def strings_strings(path_to_app):
    """
    利用 Linux 命令 strings 获取字符串
    """
    strings = os.popen('strings %s' % path_to_app)
    return strings


def get_file_hash(path_to_app):
    """
    计算文件的md5,sha1和sha256
    """
    print("计算文件md5,sha1和sha256: %s" % path_to_app)
    try:
        md5 = hashlib.md5()
        sha1 = hashlib.sha1()
        sha256 = hashlib.sha256()
        with open(path_to_app, 'rb') as afile:
            buf = afile.read(65536)
            while buf:
                md5.update(buf)
                sha1.update(buf)
                sha256.update(buf)
                buf = afile.read(65536)
        file_hash = [md5.hexdigest(), sha1.hexdigest(), sha256.hexdigest()]
        return file_hash
    except:
        print("计算失败")


def get_cert_info(path_to_app):
    """
    获取证书信息
    """
    print("获取证书信息 %s" % path_to_app)
    try:
        owner = ""
        issuer = ""
        serial_number = ""
        valid_from = ""
        valid_until = ""
        md5 = ""
        sha1 = ""
        sha256 = ""
        algorithm = ""
        version = ""

        keytool = os.path.join(java_dir, 'bin/keytool')
        args = [keytool, '-printcert', '-jarfile', path_to_app]
        keytool_info = Popen(args, stdout=PIPE, stdin=PIPE, stderr=STDOUT, bufsize=1)
        for line in keytool_info.stdout:
            line = line.decode('utf-8')
            if line.startswith("Owner"):
                owner = line.split(": ")[1].replace("\n", "")
            if line.startswith("Issuer"):
                issuer = line.split(": ")[1].replace("\n", "")
            if line.startswith("Serial"):
                serial_number = line.split(": ")[1].replace("\n", "")
            if line.startswith("Valid"):
                valid_from = ' '.join(line.split(" ")[2:8])
                valid_until = ' '.join(line.split(" ")[9:15]).replace("\n", "")
            if line.startswith("\t MD5"):
                md5 = ''.join(line.split(" ")[3].split(":")[:]).replace("\n", "")
            if line.startswith("\t SHA1"):
                sha1 = ''.join(line.split(" ")[2].split(":")[:]).replace("\n", "")
            if line.startswith("\t SHA256"):
                sha256 = ''.join(line.split(" ")[2].split(":")[:]).replace("\n", "")
            if line.startswith("\t Signature"):
                algorithm = line.split(" ")[-1].replace("\n", "")
            if line.startswith("\t Version"):
                version = line.split(" ")[-1].replace("\n", "")

        cert_info = [owner, issuer, serial_number, valid_from, valid_until, md5, sha1, sha256, algorithm, version]
        return cert_info
    except:
        print("获取证书信息失败")


def do_dexdump(app_home, path_to_app):
    """
    将 dex 文件转换成 txt 和 xml 
    """
    print("将dex转换为txt和xml: %s" % path_to_app)
    dexdump = os.path.join(sdk_dir, "build-tools/25.0.2/dexdump")
    txt = os.popen("%s -l plain %s" % (dexdump, path_to_app)).read()
    with open(app_home+'/dex.txt', 'w') as f:
        f.write(txt)
    xml = os.popen("%s -l xml %s" % (dexdump, path_to_app)).read()
    with open(app_home+'/dex.xml', 'w') as f:
        f.write(xml)
