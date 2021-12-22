import os
import sqlite3

import re
dbfile = ''
dbTable = ''

# fileName = ''
# des = ''
# like = ''
# share = ''
# comment = ''
# time = ''


def createDB(path):
    global dbfile
    tableName = 'data.db'

    if not os.path.exists(path):
        os.mkdir(path)
    db_is_new = not os.path.exists(path+tableName)
    if db_is_new:
        print('Need to create schema')
    else:
        print('Database exists, assume schema does, too.')
    conn = sqlite3.connect(path+tableName)
    dbfile = path+tableName

    conn.close()


def createTable(tableName):
    global dbfile
    global dbTable

    dbTable = tableName
    conn = sqlite3.connect(dbfile)
    sql = '''create table if not exists {0}(
    _id integer primary key autoincrement,
    fileName char(360) unique,
    des char(360), 
    like integer,
    share integer,
    comment integer,
    time char(32));'''.format(tableName)

    conn.execute(sql)
    print("Table created successfully")
    conn.close()


def insertDate(videoinfo, videodes, videotime):
    # global fileName
    # global des
    # global like
    # global share
    # global comment
    # global time
    # print("fileName:"+fileName)
    # print("videoinfo:"+videoinfo)
    # print("des:"+des)
    # print("time:"+time)

    global dbfile
    global dbTable

    fileName = videotime + re.sub(r'[\\/:*?"<>|\r\n]+', "_", videodes)

    # like = videoinfo['digg_count']
    # share = videoinfo['share_count']
    # comment = videoinfo['comment_count']
    # time = videotime
    conn = sqlite3.connect(dbfile)
    #print('-------------------------->{0}'.format(videoinfo['digg_count']))

    try:

        selectSql = '''select _id from {0} where fileName = '{1}';'''.format(
            dbTable, fileName)
        #print('---selectSql:{0}'.format(selectSql))

        resoult = conn.execute(selectSql)
        #print('---数据长度{0}'.format(len(resoult.fetchall())))

        #不存在类似数据 再插入
        if len(resoult.fetchall()) == 0:   
            #print('---数据长度{0}'.format(len(resoult.fetchall())))    
            insertSql = '''insert into {0} ('fileName','des','like','share','comment','time') values ('{1}','{2}','{3}','{4}','{5}','{6}');'''.format(
                dbTable, fileName, videodes, videoinfo['digg_count'], videoinfo['share_count'], videoinfo['comment_count'], videotime)

            #print(insertSql)
            conn.execute(insertSql)
            conn.commit()
            #print("Table insert successfully")
            conn.close()    
        else:    
            conn.close()
        
    except Exception as error:
        # print('插入数据错误：'+error)
        print('插入数据错误：{0}'.format(error))
        conn.close()
        pass
