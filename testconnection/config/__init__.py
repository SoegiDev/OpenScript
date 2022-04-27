import uuid
import datetime
import os
import psycopg2
from psycopg2.extensions import STATUS_BEGIN, STATUS_READY,STATUS_ASYNC,STATUS_SETUP,STATUS_PREPARED,STATUS_SYNC
from dotenv import load_dotenv
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '../.env'))

class Database():
    HOST = None
    DATABASE = None
    USER = None
    PASSWORD =None
    PORT = None
    conn = None
    cursor = None
    status = None
    message = None
    closed = 1
    def __init__(self, **kwargs):
        if os.getenv('FLASK_ENV') =='development':
            self.HOST = os.environ['DEV_HOST']
            self.DATABASE = os.environ['DEV_DB']
            self.USER = os.environ['DEV_USER']
            self.PASSWORD = os.environ['DEV_PWD']
            self.PORT = os.environ['DEV_PORT']
        elif os.getenv('FLASK_ENV') =='test':
            self.HOST = os.environ.get('TEST_HOST')
            self.DATABASE = os.environ.get('TEST_DB')
            self.USER = os.environ.get('TEST_USER')
            self.PASSWORD = os.environ.get('TEST_PWD')
            self.PORT = os.environ.get('TEST_PORT')    
        elif os.getenv('FLASK_ENV') =='prd':
            self.HOST = os.environ.get('PRD_HOST')
            self.DATABASE = os.environ.get('PRD_DB')
            self.USER = os.environ.get('PRD_USER')
            self.PASSWORD = os.environ.get('PRD_PWD')
            self.PORT = os.environ.get('PRD_PORT')
            
    def ConnectionToDB(self):
        try:
            conn = psycopg2.connect(host=self.HOST,
                                    database=self.DATABASE,
                                    user=self.USER,
                                    password=self.PASSWORD,
                                    port = self.PORT)
            cursor = conn.cursor()
            status = 1
            # print({"Hasil":True,"conn":conn,"cursor":cursor}) 
            if conn.status == STATUS_SETUP:
                print({"status":STATUS_SETUP,"message":"A connection Setup"})
                self.status = STATUS_SETUP
                self.message = "A connection Setup"
            elif conn.status == STATUS_READY:
                print({"status":STATUS_READY,"message":"A connection Ready"})
                self.status = STATUS_READY
                self.message = "A connection Ready"
            elif conn.status == STATUS_BEGIN:
                print({"status":STATUS_BEGIN,"message":"A connection BEGIN"})
                self.status = STATUS_BEGIN
                self.message = "A connection Begin"
            elif conn.status == STATUS_SYNC:
                print({"status":STATUS_SYNC,"message":"A connection SYNC"})
                self.status = STATUS_SYNC
                self.message = "A connection Sync"
            elif conn.status == STATUS_ASYNC:
                print({"status":STATUS_ASYNC,"message":"A connection ASYNC"})
                self.status = STATUS_ASYNC
                self.message = "A connection Async"
            elif conn.status == STATUS_PREPARED:
                print({"status":STATUS_PREPARED,"message":"A connection PREPARED"})
                self.status = STATUS_PREPARED
                self.message = "A connection Prepared"
            self.conn = conn
            self.cursor = cursor
            self.closed = conn.closed
            return self.status,self.closed,self.message
        except (Exception, psycopg2.DatabaseError) as error:
            print({"status":error})
            self.status = -1
            self.closed = 1
            self.message = error
            return self.status,self.closed,self.message
            
    def connect(self):
        return self.conn,self.cursor,self.closed,self.status,self.message
    
    def closeConnection(self):
        self.conn.close()
        self.closed = self.conn.closed
        return self.conn,self.closed