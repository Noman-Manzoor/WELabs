class Time:
    def __init__(self,h,m,s) -> None:
        self.__hours = h
        self.__minutes = m
        self.__seconds = s
        
    @property
    def hours(self):
        return self.__hours    
    @property
    def minutes(self):
        return self.__minutes  
     
    @property
    def seconds(self):
        return self.__seconds
    
    @hours.setter
    def hours(self,h):
        self.__hours = h   
         
    @minutes.setter
    def minutes(self,m):
        self.__minutes = m
        
    @seconds.setter
    def seconds(self,s):
        self.__seconds = s
        
    def __add__(self,obj):
        self.__hours = self.__hours+obj.hours
        self.__minutes = self.__minutes+obj.minutes
        self.__seconds = self.__seconds+obj.seconds
        
        extra_seconds = int(self.__seconds/60)
        self.__seconds = self.__seconds%60 
        self.__minutes = self.__minutes+ int(extra_seconds%60) 
               
        extra_minutes = int(self.__minutes/60)
        self.__minutes = self.__minutes%60 
        self.__hours = self.__minutes+ int(extra_minutes%60) 
                
        self.__hours = self.__hours%24 
        
    def display_time24(self):
        text = "PM" if self.__hours>12 else "AM"
        print(f'{self.__hours}:{self.__minutes}:{self.__seconds} {text}')
        
    def display_time12(self):
        h = self.__hours%12
        text = "PM" if h>12 else "AM"
        print(f'{h}:{self.__minutes}:{self.__seconds} {text}')
         
    def display_minute(self,m):
        h = int(m/60)
        m = int(m%60)  
        s = 0
        print(f'{h}:{m}:{s}')

    def getInteger(self,msg):
        num = input(msg)
        while not num.isnumeric():
            print("Invalid Input")
            num = input(msg)
        return int(num)
        
    def update_time(self):
        m = self.getInteger("Enter Time in Minutes = ")
        return self.display_minute(m)
        
    
time1 = Time(23,56,30)
time2 = Time(4,5,59)

time1.update_time()

