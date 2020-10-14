import mysql.connector
from difflib import get_close_matches

con = mysql.connector.connect(
    user = "ardit700_student",
    password = "ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database"
)

cursor = con.cursor()
word = input("enter the word: ")
if word in Dictionary:
    print("loop")
query = cursor.execute("SELECT * FROM Dictionary WHERE expression = '%s'" %word.lower())
results = cursor.fetchall()

if results:
    print("***************************\nthe meanings are:")
    for result in results:
        print("\t",result[1])
    print("***************************")
else:
    print("word does not exist")