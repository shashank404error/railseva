import mysql.connector
import uuid
import config

mydb = mysql.connector.connect(
  host=config.mysql_config["host"],
  user=config.mysql_config["user"],
  password=config.mysql_config["password"],
  database=config.mysql_config["db"]
)

def save_setting_to_db(userID,showNumber,language):
  mycursor = mydb.cursor()
  mycursor.execute("INSERT INTO settings (userID, showNumber, language) VALUES('"+userID+"', '"+showNumber+"', '"+language+"') ON DUPLICATE KEY UPDATE showNumber='"+showNumber+"', language='"+language+"';")
  mydb.commit()

def get_data_from_db(userID):
  mycursor = mydb.cursor()
  mycursor.execute("SELECT * FROM settings where userID='"+userID+"';")
  myresult = mycursor.fetchall()
  res = []
  for x in myresult:
    res = x
  return res  