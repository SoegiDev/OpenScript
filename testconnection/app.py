from config import Database

def connection():
    db = Database()
    status , closed , messages = db.ConnectionToDB()
    if(status > -1) and (closed == 0):
        conn,cursor,closed,status,message = db.connect()
        print(conn)
    else:
        print("Not Connected",messages)
        

if __name__ == "__main__":
    connection()