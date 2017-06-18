# -*- coding: utf_8 -*-
"""
yara初始化
"""

import os
import yara

import setting

rules_dir = setting.get_yara_rules_dir()
compiled_rules_path = os.path.join(rules_dir, 'rules.yarc')

yara_files = {}
try:
    for root, _, filenames in os.walk(rules_dir):
        for file in filenames:
            if file.endswith(".yara"):
                path = os.path.join(root, file)
                yara_files[path] = path

    rules = yara.compile(filepaths = yara_files)
    rules.save(compiled_rules_path)

    print("yara规则编译成功。")
except Exception as e:
    print(e)
    print("yara规则编译失败。")