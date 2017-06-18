# -*- coding: utf_8 -*-
"""
从数据库中获取样本
"""

from modules import db

cnx = db.connect_db()

def get_samples(cnx):
    cur = cnx.cursor()
    cnx.database = "annhub"

    sql = "SELECT md5,uses_permission FROM apk"
    cur.execute(sql)

    for row in cur.fetchall():
        md5 = row[0]
        permission = row[1].split("\', \'")[:]
        print(md5)
        print(permission)

    cur.close()

get_samples(cnx)
cnx.close()