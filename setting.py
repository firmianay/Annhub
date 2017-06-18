# -*- coding: utf_8 -*-
"""
初始设置
"""

def get_root_dir():
    root_dir = "/home/firmy/PycharmProjects/annhub/"
    return root_dir

def get_download_home():
    download_home = "/home/firmy/Downloads/annhub/DownloadAPKs/"
    return download_home

def get_upload_home():
    upload_home = "/home/firmy/Downloads/annhub/UploadAPKs/"
    return upload_home

def get_analysis_home():
    analysis_home = "/home/firmy/Downloads/annhub/AnalysisAPKs/"
    return analysis_home

def get_reAnalysis_home():
    reAnalysis_home = "/home/firmy/Downloads/annhub/reAnalysis/"
    return reAnalysis_home

def get_save_home():
    save_home = "/home/firmy/Downloads/annhub/SaveAPKs/"
    return save_home

def get_error_home():
    error_home = "/home/firmy/Downloads/annhub/ErrorAPKs/"
    return error_home

def get_java_home():
    java_home = "/usr/"
    return java_home

def get_sdk_home():
    sdk_home = "/home/firmy/Android/Sdk/"
    return sdk_home

def get_mysql_config():
    config = {
        'user': 'annhub',
        'password': 'annhub123',
        'host': '127.0.0.1',
        'port': '3306'
    }
    return config

def get_yara_rules_dir():
    dir = "/home/firmy/PycharmProjects/annhub/modules/yara_rules"
    return dir
