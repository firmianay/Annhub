# -*- coding: utf_8 -*-
"""
数据库操作
"""
import json
import mysql.connector as mariadb
from mysql.connector import errorcode

import setting


def connect_db():
    """
    连接数据库
    """
    config = setting.get_mysql_config()
    try:
        cnx = mariadb.connect(**config)
    except mariadb.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("mysql账号或密码错误")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("mysql数据库不存在")
        else:
            print(err)
    else:
        print("mysql连接成功")
        return cnx


def init_db(cnx):
    """
    初次使用时初始化数据库
    """
    # dvm_permission = dvm_permissions.DVM_PERMISSIONS["MANIFEST_PERMISSION"].keys()
    try:
        cur = cnx.cursor()

        create_database_sql = "CREATE DATABASE annhub"
        cur.execute(create_database_sql)
        cnx.database = "annhub"

        create_apk_table_sql = "CREATE TABLE apk" \
                               "(md5 char(32) PRIMARY KEY NOT NULL," \
                               "sha1 char(225)," \
                               "sha256 char(225)," \
                               "cert char(225)," \
                               "size char(225)," \
                               "name char(225)," \
                               "package char(225)," \
                               "version_code char(225)," \
                               "version_name char(225)," \
                               "uses_permission text," \
                               "custom_permission text," \
                               "permission_group text," \
                               "min_sdk char(225)," \
                               "target_sdk char(225)," \
                               "max_sdk char(225)," \
                               "activity text," \
                               "main_activity text," \
                               "service text," \
                               "receiver text," \
                               "provider text," \
                               "intent_filter text," \
                               "uses_library text," \
                               "strings_aapt longtext," \
                               "virus_total char(225)," \
                               "ml_malware char(225))"
        cur.execute(create_apk_table_sql)

        # create_per_table_sql = "CREATE TABLE permission" \
        #                        "(md5 int PRIMARY KEY NOT NULL)"
        # cur.execute(create_per_table_sql)
        # for perm in dvm_permission:
        #     add_per_table_sql = "ALTER TABLE permission ADD COLUMN %s int" % perm
        #     cur.execute(add_per_table_sql)
    except mariadb.Error as err:
        if err.errno == errorcode.ER_DB_CREATE_EXISTS:
            print("annhub数据库已初始化")
            pass
        else:
            print(err)


def deconnect_db(cnx):
    """
    断开连接数据库
    """
    try:
        cnx.close()
        print("mysql已断开")
    except:
        pass


# def check(cnx, package, version, md5):
#     pass


def check(cnx, md5):
    """
    检查待测apk是否已经存在
    """
    cur = cnx.cursor()
    cnx.database = "annhub"
    check_sql = "SELECT name FROM apk WHERE md5 = \"%s\"" % md5
    cur.execute(check_sql)
    if len(cur.fetchall()) == 0:
        cur.close()
        return 0
    else:
        cur.close()
        return 1


def insert_apk(cnx, file_hash, cert_info, file_name, file_size, manifest_data, strings_aapt):
    cur = cnx.cursor()
    cnx.database = "annhub"

    package = manifest_data['package']
    version_code = manifest_data['version_code']
    version_name = manifest_data['version_name']
    uses_permission = manifest_data['uses_permission'].keys()
    custom_permission = manifest_data['custom_permission']
    permission_group = manifest_data['permission_group']
    min_sdk = manifest_data['min_sdk']
    target_sdk = manifest_data['target_sdk']
    max_sdk = manifest_data['max_sdk']
    activity = manifest_data['activity']
    main_activity = manifest_data['main_activity']
    service = manifest_data['service']
    receiver = manifest_data['receiver']
    provider = manifest_data['provider']
    intent_filter = json.dumps(manifest_data['intent_filter'])
    uses_library = manifest_data['uses_library']

    insert_sql = "INSERT INTO apk (md5, sha1, sha256, " \
                 "cert, " \
                 "size, " \
                 "name, " \
                 "package, version_code, version_name, uses_permission, custom_permission, permission_group, min_sdk, target_sdk, max_sdk, activity, main_activity, service, receiver, provider, intent_filter, uses_library, " \
                 "strings_aapt" \
                 ") VALUES (" \
                 "\"%s\", \"%s\", \"%s\", " \
                 "\"%s\", " \
                 "\"%s\", " \
                 "\"%s\", " \
                 "\"%s\", \"%s\", \"%s\", \"%s\", \"%s\", \"%s\", \"%s\", \"%s\", \"%s\", \"%s\", \"%s\", \"%s\", \"%s\", \"%s\", \"%s\", \"%s\"," \
                 "\"%s\")"\
                 % (file_hash[0], file_hash[1], file_hash[2],
                    cert_info,
                    file_size,
                    file_name,
                    package,version_code,version_name,uses_permission,custom_permission,permission_group,min_sdk,target_sdk,max_sdk,activity,main_activity,service,receiver,provider,intent_filter,uses_library,
                    strings_aapt)

    cur.execute(insert_sql)
    cur.close()
    cnx.commit()


def virus_total(cnx, score):
    cur = cnx.cursor()
    cnx.database = "annhub"

    sql = "INSERT INTO apk virus_total VALUES %s" % score
    cur.execute(sql)
    cur.close()
    cnx.commit()


def ml_insert_apk(cnx, is_malware):
    cur = cnx.cursor()
    cnx.database = "annhub"

    sql = "INSERT INTO apk ml_malware VALUES %s" % is_malware
    cur.execute(sql)
    cur.close()
    cnx.commit()


# cnx = connect_db()
# init_db(cnx)
# deconnect_db(cnx)
