


import os
import sys
import mysql.connector

mydb = mysql.connector.connect(
      host = "localhost",
      user = "root",
      passwd = "1234",
      database = "login"
      )

class User:



  def init(self):
    self.name = None
    self.age = None
    self.login = None
    self.passwdord = None
    self.welcome()


def welcome():
  option = ["1", "2"]
  print(""""
  Please choose one of these options:
  Register     [1]
  Log in       [2]
  Exit         [3]
  """)
  reg_log=input("Enter [1 or 2]:  ")
  while reg_log not in option:
      self.clear()
      print("Invalid input")
      reg_log=input("""Please choose one of these options:
                       [1] Register
                       [2] Log in
                       """)
  if reg_log == "1":
      self.register()
  elif  reg_log == "2":
      self.log_in()
  else:
    sys.exit()



  def register(self):
      name = input("enter your name: ").strip().capitalize()
      while name.isdigit():
        self.clear()
        print("You've entered number")
        name = input("enter your name :").strip().capitalize()

      age = input("enter your name: ").strip()
      while age.isalpha():
        print("You've entered alpha")
        age = input("enter your name: ").strip()

      login = input("enter your login: ").strip().lower()
      while login.isdigit():
          print("You've entered numbers")
          login = input("enter your login: ").strip().lower()




     password = input("enter your password: ").strip()
     confirm_password = input("enter confirm password: ").strip()
     while password!=confirm_password:
         print("You've entered different passswords")
         password = input("enter your password: ").strip()
         confirm_password = input("enter confirm password: ").strip()
     self.name=name
     self.age=age
     self.login=login
     self.passwdord=password
     pass











  def log_in(self):
    pass




def write_db(self):
    mycursor=mydb.cursor()
    mycursor = (f"insert into shirin values("{self.name}", "{self.age}", "{self.login}", "{self.password}")")
    mydb.commit()





@staticmethod
	def clear():
		os.system("clear")


a=User()




