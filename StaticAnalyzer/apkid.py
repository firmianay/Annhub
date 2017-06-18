# -*- coding: utf_8 -*-
"""
使用yara规则进行恶意代码匹配
"""

import json
import os
import shutil
import tempfile
import yara
import zipfile

import setting

ZIP_MAGIC = [b'PK\x03\x04', b'PK\x05\x06', b'PK\x07\x08']
DEX_MAGIC = [b'dex\n', b'dey\n']
ELF_MAGIC = [b'\x7fELF']


def get_file_type(file_path):
    with open(file_path, 'rb') as f:
        magic = f.read(4)
    if magic in ZIP_MAGIC:
        return 'apk'
    elif magic in DEX_MAGIC:
        return 'dex'
    elif magic in ELF_MAGIC:
        return 'elf'
    return 'invalid'


def collect_files(input):
    if os.path.isfile(input):
        file_type = get_file_type(input)
        if file_type != 'invalid':
            yield (file_type, input)
    else:
        for root, _, filenames in os.walk(input):
            for filename in filenames:
                file_path = os.path.join(root, filename)
                file_type = get_file_type(file_path)
                if file_type != 'invalid':
                    yield (file_type, file_path)


def do_yara(path_to_app, rules):
    matches = rules.match(path_to_app)
    results = {}
    for match in matches:
        tags = ', '.join(sorted(match.tags))
        value = match.meta.get('description', match)
        if tags in results:
            if value not in results[tags]:
                results[tags].append(value)
        else:
            results[tags] = [value]
    return results


def scan(app_home, path_to_app):
    rules_path = os.path.join(setting.get_yara_rules_dir(), "rules.yarc")
    rules = yara.load(rules_path)

    results = {}
    try:
        zf = zipfile.ZipFile(path_to_app, 'r')
        target_member = filter(lambda n: n.startswith('classes'), zf.namelist())
        td = tempfile.mkdtemp()
        zf.extractall(td, members=target_member)
        zf.close()
        for file_type, file_path in collect_files(td):
            entry_name = file_path.replace('{}/'.format(td), '')
            key_path = '{}!{}'.format(path_to_app, entry_name)
            match_dic = do_yara(file_path, rules)
            if len(match_dic) > 0:
                results[key_path] = match_dic
                results_json = json.dumps(results, sort_keys=True, indent=4)
                with open(app_home+"/apkid.json", "w") as f:
                    f.write(results_json)
                    f.close()
        shutil.rmtree(td)
    except Exception as e:
        print(e)
        print("yara规则匹配失败。")
