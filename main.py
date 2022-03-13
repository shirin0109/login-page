


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

      pass




  def log_in(self):
    pass






  def user_exists(self, login):
      mycursor=mydb.cursor()
      mycursor.execute(f"select login from shirin where login = '{login}'")
      a=mycursor.fetchall()
      return bool(a)





@staticmethod
	def clear():
		os.system("clear")


a=User()




