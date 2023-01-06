import json
import pymysql
json_data=open("project3.json").read()
json_obj=json.loads(json_data)
con=pymysql.connect(host="localhost",user="root",password="2002",db="json")

cursor=con.cursor()

for item in json_obj:
    person=item.get("person")
    year=item.get("year")
    company=item.get("company")
    cursor.execute("insert into json_file(person, year, company) VALUES(%s, %s, %s)", (person, year, company))
    con.commit()

