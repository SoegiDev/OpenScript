import sys
sys.path.append('./')
from db.BasicConfig import BasicConfig
from config import Database
import json

class CreateDatabase():
    status = ''
    closed = ''
    messages =''
    conn = ''
    cursor = ''
    def __init__(self, **kwargs):
        db = Database()
        self.status , self.closed , self.messages = db.ConnectionToDB()
        if(self.status > -1) and (self.closed == 0):
            self.conn,self.cursor,self.closed,self.status,self.message = db.connect()
        else:
            print("Not Connected",self.messages)
    
    def createUser(self):
        self.cursor.execute('DROP TABLE IF EXISTS users')
        self.cursor.execute('CREATE TABLE users (id serial NOT NULL,'
                                        'firstname varchar (20) NOT NULL,'
                                        'lastname varchar (50) NOT NULL,'
                                        'email varchar(50) NOT NULL UNIQUE,'
                                        'username varchar(20) NOT NULL UNIQUE,'
                                        'created_at timestamp DEFAULT NOW(),'
                                        'updated_at timestamp default current_timestamp,'
                                        'PRIMARY KEY (id));'
                                        )
        newUser = {"firstname":"Fajar","lastname":"Soegi","email":"soegidev.id@gmail.com","username":"soegidev"}
        userInsert = "INSERT INTO users(firstname,lastname,email,username)values(%s,%s,%s,%s);"
        self.cursor.execute(userInsert,[newUser['firstname'],newUser['lastname'],newUser['email'],newUser['username']])
        self.conn.commit()
    def createMigrations(self):
        self.cursor.execute('DROP TABLE IF EXISTS migrations;')
        self.cursor.execute('CREATE TABLE migrations (id serial NOT NULL,'
                                        'name varchar (200) NOT NULL,'
                                        'created_at timestamp DEFAULT NOW(),'
                                        'updated_at timestamp default current_timestamp,'
                                        'PRIMARY KEY (id));'
                                        )
        migrateInsert = "INSERT INTO migrations(name)values(%s);"
        migrationame = "Initial Database With Table"
        self.cursor.execute(migrateInsert,[migrationame])
        self.conn.commit()
    def createConfiguration(self):
        self.cursor.execute('DROP TABLE IF EXISTS configuration;')
        self.cursor.execute('CREATE TABLE configuration (id serial NOT NULL,'
                                        'name varchar (200) NOT NULL,'
                                        'config text default NULL, '
                                        'active boolean default True, '
                                        'created_at timestamp DEFAULT NOW(),'
                                        'updated_at timestamp default current_timestamp,'
                                        'PRIMARY KEY (id));'
                                        )
        nameInsert = "Basic"
        configNew = "INSERT INTO configuration(name,config)values(%s,%s);"
        configinsert = """{"version":"v1.0.0","versioncode":1,"applicationname":"PythonDev","powered_by":"X_blocks","created_by":"Soegidev",\
                        "created_year":"2022","license":"XLicence","github":"Soegidev","version_api":"1",\
                        "version_server":"1","url_api":"http://localhost/api","endpoint":"/api"}"""
        self.cursor.execute(configNew,[nameInsert,configinsert])
        self.conn.commit()
        
    def cursorClose(self):
        return self.cursor.close()
    def connClose(self):
        return self.conn.close()
    def getDataConfig(self):
        name = "Basic"
        ss = str(BasicConfig().getConfig())
        query = f"SELECT {ss} FROM public.configuration WHERE name='{name}'"
        self.cursor.execute(query)
        if(self.cursor.rowcount == 0):
            self.cursor.close()
            self.conn.close()
        row = self.cursor.fetchone()
        parse = json.loads(row[1])
        PreconfigModel = BasicConfig()
        PreconfigModel.parsing(parse)
        print(PreconfigModel.result())
if __name__ == "__main__":
    run = CreateDatabase()
    run.createUser()
    run.createMigrations()
    run.createConfiguration()
    run.getDataConfig()