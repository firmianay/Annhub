# -*- coding: utf_8 -*-
"""
解析 smali 文件以获取：
    class names
    class properties
    class methods
    method calls
"""

import os
import re
import json
from smalisca.core.smalisca_main import SmaliscaApp
from smalisca.modules.module_smali_parser import SmaliParser

import setting

analysis_dir = setting.get_analysis_home()
save_dir = setting.get_save_home()


def get_className(source):
    regex = "^\.class\s+(.*?)\n\.super\s+(.*?)\n\.source\s+\"(.*?)\"\n"
    re_obj = re.compile(regex)
    class_name = re.findall(re_obj, source)
    return class_name


def get_fieldName(source):
    regex = "[.]field\s+(.*?)\n"
    re_obj = re.compile(regex)
    field_name = re.findall(re_obj, source)
    return field_name


def get_methodName(source):
    regex = "[.]method\s(.*?)\n(.*?)[.]end\s+method"
    re_obj = re.compile(regex)
    method_name = re.findall(re_obj, source)
    return method_name


def do_walk(app_home):
    graph = {}
    for root, _, filenames in os.walk(app_home+"/smali_code"):
        for file in filenames:
            with open(root+"/"+file, "r") as file_handle:
                content = file_handle.read()
                if get_className(content):
                    class_name = get_className(content)[0][0].split(' ')[-1]
                    graph[class_name] = {}
                    graph[class_name]['field'] = get_fieldName(content)
                    graph[class_name]['method'] = []
                    for m in get_methodName(content):
                        ind_meth = {}
                        ind_meth['name'] = m[0].split(' ')[-1]
                        ind_meth['instructions'] = []
                        for i in m[1].split('\n'):
                            if len(i) > 0:
                                ind_meth['instructions'].append(i.lstrip().rstrip())
                        graph[class_name]['method'].append(ind_meth)
    print(graph)


def make_parser(app_home):
    app = SmaliscaApp()
    app.setup()

    location = app_home + '/smali_code'
    suffix = 'smali'

    parser = SmaliParser(location, suffix)
    parser.run()

    results = parser.get_results()
    results_json = json.dumps(results, sort_keys=True, indent=4)
    with open(app_home + "/smali_parser.json", "w") as f:
        f.write(results_json)
        f.close()
    return results
