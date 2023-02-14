import pymysql
from exceptions import *
from contact import Contact

class DBHandler:
    #  Static attrs
    users = []
    students = []
    faculties = [] 
    
    def __init__(self,host,user,passwd,database) -> None:
        try:
            self.connection = pymysql.connect(host=host,user=user,passwd=passwd,database=database)
            self.cursor = self.connection.cursor(pymysql.cursors.DictCursor)
            self.refreshDatabase()
        except:
            try: 
                raise DatabaseConnectivityError
            except DatabaseConnectivityError:
                return
    
    
    def getAllContacts(self):
        sql = "SELECT * FROM `contacts`"
        self.cursor.execute(sql)
        return self.cursor.fetchall()
    
    
    def insertContact(self,contact:Contact): 
        try:
            sql = f"INSERT INTO `contacts` (`id`, `name`, `mobileno`, `city`, `profession`) VALUES (NULL, '{contact.name}', '{contact.mobileno}', '{contact.city}', '{contact.profession}');"
            self.cursor.execute(sql)
            self.connection.commit()
            return True
        except:
            try:
                raise contactInsertionError
            except contactInsertionError:
                return False
        
        
        
if __name__=="__main__": 
    db = DBHandler(host="localhost",user="root",passwd="",database="test")
    
    print(db.getAllContacts())
    