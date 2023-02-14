import pymysql

 
connection = pymysql.connect(host="localhost",user="root",passwd="",database="test")
cursor = connection.cursor()


class User:
    def __init__(self) -> None:
        self.__account_number = ''
        self.__password = ''
        self.__account_balance = ''
    
    @property
    def account_number(self):
        return self.__account_number    
    @property
    def password(self):
        return self.__password    
    
    @property
    def account_balance(self):
        return self.__account_balance
    
    
    @account_number.setter
    def account_number(self,new_account_number):
        if new_account_number  and len(str(new_account_number))>0:
            self.__account_number = new_account_number
    
    def getUserData(self,account_number=None):
        account_number = account_number if account_number else self.__account_number
        cursor.execute(f"SELECT * FROM users WHERE account_no='{account_number}' ")
        data = cursor.fetchone() 
        if data:
            return data
        
        return None
    
user = User()
user.account_number = '756756555'
user.getUserData()

class ATM(User):
    def __init__(self) -> None:
        super().__init__() 
        self.LOGGED_IN_USER_RECORD = None
        
    def getAllAccountsData(self):
        cursor.execute("SELECT * FROM users")
        return cursor.fetchall()
    
    def registerAccount(self,account_number,password,balance):
        users = self.getAllAccountsData()
        required_user = [x for x in users if str(x[1]) == str(account_number)] 
        if required_user:
            return None
        
        query =  f"""INSERT INTO `users` ( `account_no`, `account_balance`, `password`) VALUES ('{account_number}', '{password}', '{balance}');"""
        cursor.execute(query)
        connection.commit()
        return cursor.rowcount
        
    def login(self,account_number,password):
        users = self.getAllAccountsData()
        required_user = [x for x in users if str(x[1]) == str(account_number) and str(x[3])==str(password)] 
        if required_user:
            required_user = required_user[0]
            self.LOGGED_IN_USER_RECORD = required_user
        
    
    def checkBalance(self):
        if self.LOGGED_IN_USER_RECORD:
            return self.LOGGED_IN_USER_RECORD[-1]
        else:
            return "Please Login to Check Balance"
        
    def deposit(self,amount):
        if self.LOGGED_IN_USER_RECORD:
            if str(amount).isnumeric(): 
                user_id = int(self.LOGGED_IN_USER_RECORD[0])
                new_balance = int(self.LOGGED_IN_USER_RECORD[2])+int(amount)
                sql = f"""UPDATE `users` SET `account_balance` = '{new_balance}' WHERE `users`.`user_id` =  {user_id};"""
                cursor.execute(sql)
                connection.commit()
                return new_balance
            else:
                return "Amount must be Numeric"
        else:
            return "Please Login to Deposit"
        
    def withdraw(self,amount):
        if self.LOGGED_IN_USER_RECORD:
            if str(amount).isnumeric():
                user_id = int(self.LOGGED_IN_USER_RECORD[0])
                new_balance = int(self.LOGGED_IN_USER_RECORD[2]) - int(amount)
                if new_balance >=0:
                    print(amount)
                    sql = f"""UPDATE `users` SET `account_balance` = '{new_balance}' WHERE `users`.`user_id` =  {user_id};"""
                    cursor.execute(sql)
                    connection.commit()
                else:
                    return "Invalid Balance"
            else:
                return "Amount must be Numeric"
        else:
            return "Please Login to Withdraw"
        
atm = ATM()

atm.login("4125","483",)

atm.deposit(1000)
    