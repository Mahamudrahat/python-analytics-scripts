import datetime
import requests
import mysql.connector
import threading
import time
import json
from decimal import Decimal
#Mysql_Connect
mydbrbl = mysql.connector.connect(host="",user="",passwd="",database='')
mydbfsibl = mysql.connector.connect(host="",user="",passwd="",database='')
mydbjbl = mysql.connector.connect(host="",user="",passwd="",database='')
mydbbcbl = mysql.connector.connect(host="",user="",passwd="",database='')

# prepare a cursor object using cursor() method
#Bankwise_connection_Dictionary
if __name__ == '__main__':
    BankwiseUrl = {
    'RBL' : mydbrbl.cursor(),
    'FSIBL' : mydbfsibl.cursor(),
    'JBL' : mydbjbl.cursor(),
    'BCBL' : mydbbcbl.cursor()}
    text_file = open("t_payment.txt", "r")
    lines = text_file.read().split('\n')
    # print lines
    text_file.close()
    list_size = len(lines)
    print (str(list_size))
	
    for i in range(list_size):
        print (lines[i])
        sub_lines = lines[i].split(',')
        mycursor=BankwiseUrl.get(sub_lines[0])
        mycursor.execute("SELECT from_account_id,to_account_id FROM table1 s WHERE '"%(sub_lines[2]))
        data_list_main = mycursor.fetchall()
        mycursor.execute("SELECT owner_name FROM table2 s WHERE s.id = '%s'"% (str(data_list_main[0][0]))) 
        data_list_sec = mycursor.fetchone()
        # print data_list_sec[0]
        url = "API URL"+ data_list_sec[0]
        r = requests.get(url)
        jsonData = r.json()
        if jsonData['userType'] == 'agent':
            with open('result.txt', 'a') as the_file:
               the_file.write(sub_lines[2] + "," + jsonData['distributorWallet'] + "," + str(sub_lines[3]) + "\n")
        else:
            mycursor.execute("SELECT owner_name FROM table3 s WHERE s.id = '%s'"% (str(data_list_main[0][1]))) 
            data_list_sec2 = mycursor.fetchone()
            # print data_list_sec[0]
            url = "API URL" + data_list_sec2[0]
            r = requests.get(url)
            jsonData = r.json()
            if jsonData['userType'] =='agent':
                with open('result.txt', 'a') as the_file:
                  the_file.write(sub_lines[2] + "," + jsonData['distributorWallet'] + "," + str(sub_lines[3]) + "\n")

    
    mydbrbl.close()
    mydbfsibl.close()
    mydbjbl.close()
    mydbbcbl.close()