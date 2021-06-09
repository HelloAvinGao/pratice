#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sqlite3,os,sys
    
if os.path.exists('test.db'):
    pass
else:
    try:
        f = open("test.db",'w')
        f.close()
    except:
        print('the test.db created failed')

conn = sqlite3.connect('test.db')
c = conn.cursor()
try:
    create_tb_cmd='''CREATE TABLE IF NOT EXISTS COMMENTS
       (NAME           VARCHAR(50),
       EMAIL          VARCHAR(50),
       COMMENT        VARCHAR(10000),
       PHONE          VARCHAR(11));'''
    c.execute(create_tb_cmd)
    print('table comments created successfully')
except:
    print('table comments created failed')

insert_dt_cmd='''
INSERT INTO COMMENTS (NAME,EMAIL,PHONE,COMMENT) VALUES (\"%s\",\"%s\",\"%s\",\"%s\");
'''%(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])
conn.execute(insert_dt_cmd)
conn.commit()
conn.close()


