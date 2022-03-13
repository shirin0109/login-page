
import os
import sys
import mysql.connector

class User:
  def init(self):
    self.mydb = mysql.connector.connect(
      host = "localhost",
      user = "root",
      passwd = "1234",
      database = "login"
      )
    self.name = None
    self.age = None
    self.login = None
    self.passwd = None
    self.mycoursor = self.mydb.cursor()

a=User()