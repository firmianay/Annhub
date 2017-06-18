# -*- coding: utf_8 -*-
"""
以 json 格式显示分析报告
"""

import os
import json
import shutil

def make_report(file_name, cert_info, manifest_data):
    name = file_name

    package = manifest_data['package']
    min_sdk = manifest_data['min_sdk']
    target_sdk = manifest_data['target_sdk']
    max_sdk = manifest_data['max_sdk']

    owner = cert_info[0]
    issuer = cert_info[1]
    serial_number = cert_info[2]
    valid_from = cert_info[3]
    valid_until = cert_info[4]
    md5 = cert_info[5]
    sha1 = cert_info[6]
    sha256 = cert_info[7]
    algorithm = cert_info[8]
    version = cert_info[9]

    version_code = manifest_data['version_code']
    version_name = manifest_data['version_name']
    uses_permission = manifest_data['uses_permission'].keys()
    custom_permission = manifest_data['custom_permission']
    permission_group = manifest_data['permission_group']

    activity = manifest_data['activity']
    main_activity = manifest_data['main_activity']
    service = manifest_data['service']
    receiver = manifest_data['receiver']
    provider = manifest_data['provider']
    intent_filter = manifest_data['intent_filter']
    uses_library = manifest_data['uses_library']
