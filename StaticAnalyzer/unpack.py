# -*- coding: utf_8 -*-

import os
import re
import shutil
import subprocess
import zipfile
from multiprocessing import Process
from subprocess import Popen, PIPE, STDOUT

import setting

root_dir = setting.get_root_dir()
analysis_dir = setting.get_analysis_home()
save_dir = setting.get_save_home()
error_dir = setting.get_error_home()

def unzip(app_home, path_to_app):
    """
    解压APK
    """
    print("\n开始解压文件： %s" % path_to_app)
    try:
        apkfile = zipfile.ZipFile(path_to_app)
        apkfile.extractall(app_home+'/unzip')
    except:
        print("解压文件失败: %s\n" % path_to_app)

def unzip_manifest(app_home, path_to_app):
    """
    只解压 manifest
    """
    print("\n解压AndroidManifest")
    try:
        apkfile = zipfile.ZipFile(path_to_app)
        apkfile.extract("AndroidManifest.xml", app_home)
    except:
        print("解压AndroidManifest失败")


def dex_2_smali(app_home, path_to_app):
    """
    将 dex 文件转换成 smali 文件
    不能处理多dex
    """
    print("开始转换文件： %s" % path_to_app)
    try:
        d2s = os.path.join(root_dir, "modules/tools/dex2jar/d2j-dex2smali.sh")
        args = [d2s, '-f', path_to_app, '-o', app_home+'/smali_code/']
        subprocess.call(args)
    except:
        print("dex2smali转换失败: %s\n" % path_to_app)


def use_apktool(app_home, path_to_app):
    """
    解压apk并转换资源文件和dex文件
    能处理多dex
    """
    try:
        print("正在使用apktool...")
        apktool = os.path.join(root_dir, "modules/tools/apktool_2.2.2.jar")
        args = ['java', '-jar', apktool, 'd', path_to_app, '-o', app_home+'/apktool', '-f']
        subprocess.call(args)
    except:
        print("apktool转换失败: %s\n" % path_to_app)

    # 当manifest.py使用新方法时使用
    # shutil.move(app_home+'/apktool/AndroidManifest.xml', app_home+'/AndroidManifest.xml')

    smali_path = []
    try:
        print("开始合并smali文件...")
        restored = 0
        for root, _, filenames in os.walk(app_home):
            for filename in filenames:
                if filename.endswith(".smali"):
                    smali_file = os.path.join(root, filename)
                    smali_doc = smali_file.split('/')
                    if smali_doc[8] == "smali":
                        tmp = "/".join(smali_doc[9:-1])
                        if tmp not in smali_path:
                            smali_path.append(tmp)
                    else:
                        tmp = "/".join(smali_doc[9:-1])
                        if tmp in smali_path:
                            smali_doc[8] = "smali"
                            new_path = "/".join(smali_doc[:-1])
                            shutil.move(smali_file, new_path)
                            restored += 1
                        else:
                            print("未合并文件： %s" % smali_file)
        print("共合并文件数： %d" % restored)
    except Exception as e:
        print(e)
        print("合并smali文件失败")
    shutil.move(app_home+'/apktool/smali', app_home+'/smali_code')
    shutil.move(app_home+'/apktool/res/values', app_home+'/unzip/res')
    shutil.rmtree(app_home+'/apktool')


def decompile(app_home, path_to_app, type="d2j"):
    """
    先将 DEX 转为 JAR，然后使用混合使用三种反编译器得到 java 代码
    """
    args = []
    print("\n开始反编译: %s" % path_to_app)
    if type == "d2j":
        print("dex2jar开始转换: %s" % path_to_app)
        try:
            d2j = os.path.join(root_dir, "modules/tools/dex2jar/d2j-dex2jar.sh")
            args = [d2j, '-f', path_to_app, '-o', app_home+'/classes.jar']
            result = Popen(args, stdout=PIPE, stderr=STDOUT, bufsize=1)
            line = result.stdout.readlines()
            if len(line) > 1:
                print("dex2jar转换失败: %s\n开始尝试使用enjarify: %s" % (path_to_app,path_to_app))
                try:
                    enjarify = os.path.join(root_dir, "modules/tools/enjarify/enjarify.sh")
                    process = Popen([enjarify, '-f', '--fast', path_to_app, '-o', app_home + '/classes.jar'],
                                    stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                    process.communicate()
                except:
                    print("enjarify转换失败: %s\n" % path_to_app)
        except:
            print("dex2jar转换失败: %s\n" % path_to_app)
    elif type == "enjarify":
        print("enjarify开始转换: %s" % path_to_app)
        try:
            enjarify = os.path.join(root_dir, "modules/tools/enjarify/enjarify.sh")
            process = Popen([enjarify, '-f', '--fast', path_to_app, '-o', app_home+'/classes.jar'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            process.communicate()
        except:
            print("enjarify转换失败: %s\n", path_to_app)

    path_to_jar = os.path.join(app_home, "classes.jar")
    zf = zipfile.ZipFile(path_to_jar)
    total_files = len(zf.namelist())
    print("jar内文件数为： %s" % total_files)
    class_files = len([s for s in zf.namelist() if ((".class" in s) and ("$" not in s))])
    print("类数为: %s" % class_files)

    thread1 = Process(name="jdcore", target=jdcore, args=(zf.filename, app_home+"/java_code"))
    thread2 = Process(name="procyon", target=procyon, args=(zf.filename, app_home+"/java_code"))
    thread3 = Process(name="cfr", target=cfr, args=(zf.filename, app_home+"/java_code"))

    print(zf.filename)

    thread1.start()
    thread2.start()
    thread3.start()
    thread1.join()
    thread2.join()
    thread3.join()

    if thread1.is_alive():
        thread1.terminate()
    if thread2.is_alive():
        thread2.terminate()
    if thread3.is_alive():
        thread3.terminate()

    result1 = grep_result(app_home+"/java_code", "// Byte code:")
    result2 = grep_result(app_home+"/java_code"+"1", "// This method could not be decompiled.")
    result3 = grep_result(app_home+"/java_code"+"2", "// This method has failed to decompile.")

    print("jdcore反编译失败文件数： " + str(len(result1)))
    print("procyon反编译失败文件数： " + str(len(result2)))
    print("cfr反编译失败文件数： "+ str(len(result3)))

    print("尝试重组反编译结果")
    restored = 0
    try:
        for java_file in result1:
            relative_file = str(java_file).split(app_home+"/java_code")[1]
            if any(relative_file in s for s in result2):
                if any(relative_file in s for s in result3):
                    print("重组失败: %s" % relative_file)
                else:
                    shutil.copy(app_home+"/java_code"+"2"+relative_file, java_file)
                    restored = restored + 1
            else:
                shutil.copy(app_home+"/java_code"+"1"+relative_file, java_file)
                restored = restored + 1
    except Exception as e:
        print(e)
    print("共重组文件 %s 个" % restored)
    try:
        shutil.rmtree(app_home+"/java_code"+"1")
        shutil.rmtree(app_home+"/java_code"+"2")
        os.remove(app_home+"/classes.jar")
    except:
        print("删除冗余文件失败")


def grep_result(path, regex):
    """
    匹配反编译结果
    """
    re_obj = re.compile(regex)
    result = []
    for root, _, filenames in os.walk(path):
        for filename in filenames:
            if not filename.startswith("."):
                with open (root+"/"+filename, "r") as f:
                    data = f.read()
                    if re.search(re_obj, data):
                        result.append(os.path.join(root, filename))
                    f.close()
    return result


def jdcore(path, dirname):
    """
    调用 jdcore 反编译器
    """
    process = Popen(["java", "-jar", root_dir+"modules/tools/jd-core.jar", path, dirname],
                    stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    process.communicate()


def procyon(path, dirname):
    """
    调用 procyon 反编译器
    """
    process = Popen(["java", "-jar", root_dir+"modules/tools/procyon-decompiler-0.5.30.jar", path, "-o", dirname+"1"],
                    stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    process.communicate()


def cfr(path, dirname):
    """
    调用 cfr 反编译器
    """
    process = Popen(["java", "-jar", root_dir+"modules/tools/cfr_0_121.jar", path, "--outputdir", dirname+"2"],
                    stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    process.communicate()
