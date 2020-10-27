import MySQLdb

connector = MySQLdb.connect(host="<hostaddr>", user="<username>", passwd="<password>", db="<database>")

pointer = connector.cursor()

pointer.execute("<sql commands>")

datas = pointer.fetchall()

for data in datas:
    print(data)

connector.close()

