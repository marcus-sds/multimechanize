import urllib2
import time
import os, time, datetime
from datetime import datetime
import sys
import json
import psycopg2
import random

data={}

# initial configuration
json_config=open("/app/postbench/config.json")
configs=json.load(json_config)

now = datetime.today()
dirname = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

class Transaction(object):
        def __init__(self):
                self.custom_timers = {}
                try:
                        cs = "dbname=%s user=%s password=%s host=%s port=%s" % (configs['moray1'].get('dbname'), configs['moray1'].get('user'), configs['moray1'].get('passwd'), configs['moray1'].get('addr'), configs['moray1'].get('port'))
                        self.conn = psycopg2.connect(cs)
                except Exception as e:
                        print "unable to connect to the database."+str(e)
                        sys.exit(0)

        def run(self):
                sql = """insert into a values('a')"""
                start_timer = time.time()
                self.updatedb(self.conn, sql)
                latency = time.time() - start_timer
                self.custom_timers['Example'] = latency

        def updatedb(self,conn,sql):
                cur = self.conn.cursor()
                try:
                        dir = random.choice(dirname)
                        obj = datetime.today().strftime("%y%m%d_%H%M%S%f")
                        xxx = """ INSERT INTO manta (_key, _value, _etag, dirname, name, owner, type) VALUES ('/63ff73bc-dbbd-cc04-bbe3-b09906f154d5/stor/#DIR#/#OBJ#.obj', '{dirname:/63ff73bc-dbbd-cc04-bbe3-b09906f154d5/stor/#DIR#,key:/63ff73bc-dbbd-cc04-bbe3-b09906f154d5/stor/#DIR#/#OBJ#.obj,headers:{},mtime:1479214416238,name:#OBJ#.obj,creator:63ff73bc-dbbd-cc04-bbe3-b09906f154d5,owner:63ff73bc-dbbd-cc04-bbe3-b09906f154d5,roles:[],type:object}', 'A240AD0F', '/63ff73bc-dbbd-cc04-bbe3-b09906f154d5/stor/#DIR#', '#OBJ#.obj', '63ff73bc-dbbd-cc04-bbe3-b09906f154d5', 'object') """
                        xxx = xxx.replace('#DIR#', dir)
                        xxx = xxx.replace('#OBJ#', obj)
                        cur.execute(xxx)
                        conn.commit()
                except Exception as e:
                        print "I can't update " + str(e) + xxx
                        self.conn.rollback()
                        pass
                cur.close()
                #self.conn.close()


if __name__ == '__main__':
        trans = Transaction()
        trans.run()
        print trans.custom_timers

