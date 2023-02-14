from db import DBHandler


_db = DBHandler(host="localhost",user="root",passwd="",database="test")


class ContactController:
    def __init__(self) -> None:
        pass
    
    def getAllContacts(self):
        return _db.getAllContacts()
    
    def insertConatct(self,contact):
        return _db.insertContact(contact)