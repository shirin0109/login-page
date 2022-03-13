


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
    self.options=["1", "2", "3", "4"]


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
      os.system("cls")
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
    pass

  def log_in(self):
    pass

a=User()




