# -*- coding: utf_8 -*-

import os
import subprocess
from xml.dom import minidom

import setting
from modules import dvm_permissions

root_dir = setting.get_root_dir()

def manifest_data(app_home):
    """
    定义manifest中各元素
    """
    manifest_text = parse_manifest(app_home)
    manifest_xml = minidom.parseString(manifest_text)

    uses_permission = {}
    custom_permission = {}
    permission_group = {}
    min_sdk = ''
    target_sdk = ''
    max_sdk = ''
    main_activity = ''
    activity = []
    service = []
    receiver = []
    provider = []
    intent_filter = []
    uses_library = []

    manifest = manifest_xml.documentElement
    applications = manifest_xml.getElementsByTagName("application")
    uses_permissions = manifest_xml.getElementsByTagName("uses-permission")
    custom_permissions = manifest_xml.getElementsByTagName("permission")
    permission_groups = manifest_xml.getElementsByTagName("permission-group")
    uses_sdks = manifest_xml.getElementsByTagName("uses-sdk")
    activities = manifest_xml.getElementsByTagName("activity")
    services = manifest_xml.getElementsByTagName("service")
    receivers = manifest_xml.getElementsByTagName("receiver")
    providers = manifest_xml.getElementsByTagName("provider")
    intent_filters = manifest_xml.getElementsByTagName("intent-filter")
    uses_librarys = manifest_xml.getElementsByTagName("uses-library")

    package = manifest.getAttribute("package")
    version_code = manifest.getAttribute("android:versionCode")
    version_name = manifest.getAttribute("android:versionName")

    for node in uses_permissions:
        key = node.getAttribute("android:name")
        try:
            perm = key.split('.')[-1]
            value = dvm_permissions.DVM_PERMISSIONS["MANIFEST_PERMISSION"][perm]
            uses_permission[key] = value
        except KeyError:
            uses_permission[key] = [
                "危险",
                "未知权限",
                "未知权限"
            ]

    for node in custom_permissions:
        key = node.getAttribute("android:name")
        label = node.getAttribute("android:label")
        description = node.getAttribute("android:description")
        group = node.getAttribute("android:permissionGroup")
        protect_level = node.getAttribute("android:protectionLevel")
        if protect_level == "0x00000000":
            protect_level = "normal"
        elif protect_level == "0x00000001":
            protect_level = "dangerous"
        elif protect_level == "0x00000002":
            protect_level = "signature"
        elif protect_level == "0x00000003":
            protect_level = "signatureOrSystem"
        custom_permission[key] = [label, description, group, protect_level]

    for node in permission_groups:
        key = node.getAttribute("android:name")
        try:
            perm = key.split(".")[-1]
            value = dvm_permissions.DVM_PERMISSIONS["MANIFEST_PERMISSION_GROUP"][perm]
            permission_group[key] = value
        except KeyError:
            permission_group[key] = "未知权限组"

    for node in uses_sdks:
        min_sdk = node.getAttribute("android:minSdkVersion")
        target_sdk = node.getAttribute("android:targetSdkVersion")
        max_sdk = node.getAttribute("android:maxSdkVersion")

    for node in activities:
        activity.append(node.getAttribute("android:name"))
        if len(main_activity) < 1:
            for item in node.getElementsByTagName("action"):
                val = item.getAttribute("android:name")
                if val == "android.intent.action.MAIN":
                    main_activity = key
            if main_activity == '':
                for item in node.getElementsByTagName("category"):
                    val = item.getAttribute("android:name")
                    if val == "android:intent.category.LAUNCHER":
                        main_activity = key

    for node in services:
        service.append(node.getAttribute("android:name"))

    for node in receivers:
        receiver.append(node.getAttribute("android:name"))

    for node in providers:
        provider.append(node.getAttribute("android:name"))

    nodes = []
    for i in intent_filters:
        action = i.getElementsByTagName("action")
        for node in action:
            nodes.append(node.getAttribute("android:name"))
        category = i.getElementsByTagName("category")
        for node in category:
            nodes.append(node.getAttribute("android:name"))
    intent_filter = list(set(nodes))

    for node in uses_librarys:
        uses_library.append(node.getAttribute("android:name"))

    manifest_dic = {
        'package' : package,
        'version_code' : version_code,
        'version_name' : version_name,
        'uses_permission' : uses_permission,
        'custom_permission' : custom_permission,
        'permission_group' : permission_group,
        'min_sdk' : min_sdk,
        'target_sdk' : target_sdk,
        'max_sdk' : max_sdk,
        'activity' : activity,
        'main_activity' : main_activity,
        'service' : service,
        'receiver' : receiver,
        'provider' : provider,
        'intent_filter' : intent_filter,
        'uses_library' : uses_library
    }

    return manifest_dic

def parse_manifest(app_home):
    """
    将 manifest 文件转为文本格式
    老方案
    """
    print("\n开始反编译manifest: %s" % app_home)
    try:
        manifest = os.path.join(app_home, "AndroidManifest.xml")
        axmlprinter = os.path.join(root_dir, "modules/tools/AXMLPrinter2.jar")
        args = ['java', '-jar', axmlprinter, manifest,]
        bin2txt = "java -jar %s %s > %s" % (axmlprinter,manifest,app_home+'/AndroidManifest_ascii.xml')
        os.system(bin2txt)
        manifest_text = subprocess.check_output(args)
        print("反编译manifest成功")
        return manifest_text
    except:
        print("反编译manifest失败")

# # TODO 新方案
# def parse_manifest(app_home):
#     """
#     读取文本格式的 manifest
#     新方案
#     """
#     f = open(app_home + "/AndroidManifest.xml")
#     source = f.read()
#     return source
