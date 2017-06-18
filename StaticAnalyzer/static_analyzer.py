# -*- coding: utf_8 -*-
"""
静态分析
"""

import os
import shutil
import zipfile

import setting
from StaticAnalyzer import apkid
from StaticAnalyzer import check
from StaticAnalyzer import manifest
from StaticAnalyzer import misc
from StaticAnalyzer import smali_parser
from StaticAnalyzer import unpack
from VulnerabilityAnalyzer import java_scan
from modules import db
from modules import report

root_dir = setting.get_root_dir()
analysis_dir = setting.get_analysis_home()
save_dir = setting.get_save_home()
error_dir = setting.get_error_home()
upload_dir = setting.get_upload_home()
download_dir = setting.get_download_home()
reAnalysis_dir = setting.get_reAnalysis_home()


# 检查数据库中是否已经存在
def checkFile(check_dir):
    # check.py
    # download_dir -> analysis_dir
    print("查找新应用： " + check_dir)
    list = os.listdir(check_dir)
    if len(list) != 0:
        cnx = db.connect_db()
        for l in list:
            path_to_apk = check_dir + l
            try:
                zip = zipfile.ZipFile(path_to_apk)
                if "AndroidManifest.xml" not in zip.namelist():
                    shutil.move(path_to_apk, error_dir)
                else:
                    file_md5 = check.get_md5(path_to_apk)
                    # package_name, version = check.get_apk_info(path_to_apk)
                    # cert_md5 = check.get_cert_md5(path_to_apk)
                    # if db.check(cnx, package_name, version, cert_md5):
                    print(file_md5)
                    if db.check(cnx, file_md5):
                        print("文件已存在")
                        os.remove(path_to_apk)
                    else:
                        if check_dir == download_dir:
                            move_file = os.path.join(analysis_dir, file_md5)
                            os.mkdir(move_file)
                            shutil.move(path_to_apk, move_file + "/" + file_md5 + ".apk")
                        else:
                            move_file = os.path.join(reAnalysis_dir, file_md5)
                            os.mkdir(move_file)
                            shutil.move(path_to_apk, move_file)
            except Exception as e:
                print(e)
                print("该文件不是apk")
                shutil.move(path_to_apk, error_dir)
        db.deconnect_db(cnx)
    else:
        print("文件夹为空")


# 分析应用
def analysis(org_analysis):
    # analysis_dir -> save_dir
    list = os.listdir(org_analysis)
    for l in list:
        try:
            root = org_analysis + l
            move_file = root

            in_apk = os.listdir(root)
            for k in in_apk:
                if k.endswith(".apk"):
                    path_to_apk = root + "/" + k

                    # unpack.py
                    unpack.decompile(root, path_to_apk)
                    unpack.unzip(root, path_to_apk)
                    unpack.unzip_manifest(root, path_to_apk)
                    unpack.use_apktool(root, path_to_apk)
                    # unpack.dex_2_smali(root, path_to_apk)

                    # misc.py
                    file_hash = misc.get_file_hash(path_to_apk)
                    cert_info = misc.get_cert_info(path_to_apk)
                    file_name = misc.file_name(path_to_apk)
                    file_size = misc.file_size(path_to_apk)
                    strings_aapt = misc.strings_aapt(path_to_apk)
                    misc.do_dexdump(root, path_to_apk)
                    # print(misc.strings_ClassyShark(path_to_apk))
                    # print(misc.strings_strings(path_to_apk))

                    # apkid.py
                    # apkid.scan(root, path_to_apk)

            # manifest.py
            manifest_data = manifest.manifest_data(root)

            # smali_parser.py
            smali_parser_result = smali_parser.make_parser(root)

            # java_scan.py
            java_scan_result = java_scan.get_from_java(root)

            # db.py
            # cnx = db.connect_db()
            # db.insert_apk(cnx, file_hash, cert_info, file_name, file_size, manifest_data, strings_aapt)
            # cnx.close()

            # report.py
            report.make_report(file_name, cert_info, manifest_data)

            shutil.move(move_file, save_dir)
            print("静态分析成功: %s" % path_to_apk)
        except Exception as e:
            print("静态分析失败: %s" % path_to_apk)
            with open(move_file+"/ERROR.txt", "w") as f:
                f.write(str(e))
            shutil.move(move_file, error_dir)


# 重新分析应用
def reAnalysis(apk_md5):
    root = save_dir + "/" + apk_md5
    new_root = reAnalysis_dir + "/" + apk_md5
    os.makedirs(new_root)
    list = os.listdir(root)
    for k in list:
        if k.endswith(".apk"):
            shutil.move(root+"/"+k, new_root)
    shutil.rmtree(root)
    analysis(reAnalysis_dir)


# 分析上传应用
def upload_analysis(apk_md5):
    checkFile(upload_dir)
    analysis(reAnalysis_dir)


checkFile(download_dir)
analysis(analysis_dir)
