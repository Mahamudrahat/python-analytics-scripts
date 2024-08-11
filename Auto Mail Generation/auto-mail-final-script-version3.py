import smtplib
import pandas as pd 
from tabulate import tabulate
import time
import mail_id_config
import mysql.connector
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime, timedelta
mydb = mysql.connector.connect(
   host="",
   user="",
   passwd="Please use password",
   database=''
  )
mycursor = mydb.cursor()
x=datetime.today()-timedelta(days=1)
date=x.strftime('%Y-%m-%d')
d=datetime.today() - timedelta(days=1)
y=x.strftime('%Y-%m-%d')+' 00:00:00'
#print(y)

z=d.strftime ('%Y-%m-%d')+' 23:59:59'

#print(z)
w='PROCESSED'
p='MOBILE_TOPUP'
q='INTERBANK_MOBILE_TOPUP_CR'
#r='SSD'

mycursor.execute("SELECT SUBSTRING(note1, 1, 3) AS operator,SUM(amount) AS total_amount,COUNT(note1) AS Total_recharge_count   FROM table_Name  where condition" % (y,z,w,p,q))

myresult = mycursor.fetchall()
#print(myresult)

mycursor.execute("SELECT note2 AS Vendor,FORMAT(SUM(amount),0) AS total_amount,COUNT(note1) AS Total_recharge_count   FROM table_Name  WHERE Condition" % (y,z,w,p,q))
myresult1 = mycursor.fetchall()
list_size=len(myresult1)
#print(list_size)


datas=[]
datas1=[]
datas2=[]
st=0
en=3
r=0
s=0
t=0
q=0
count=0
count1=0
#print(myresult[0][2])
for i in range(7) :
    
    for j in range(3):
        
        data=(myresult[i][j])
        if(myresult[i][j]=='017' or myresult[i][j]=='013'):
            t=t+1
            r=r+int(myresult[i][j+1]) #Sum of recharge amount
            count=count+int(myresult[i][j+2])#Sum of recharge count
            if(t==2):
              data='GP'
              datas.append(str(data)) # Operator entered into list
              data=r                  # Summation recharge amount
              datas.append(str(data)) 
              data=count              #Summation of recharge count
              datas.append(str(data))


            #print("r",r)
        if(myresult[i][j]=='019' or myresult[i][j]=='014'):
            data='Banglalink'
            q=q+1
            s=s+int(myresult[i][j+1])
            count1=count1+int(myresult[i][j+2])
            if(q==2):
              data='Banglalink'
              datas.append(str(data))
              data=s
              datas.append(str(data))
              data=count1
              datas.append(str(data))
            #print(s)
        if(myresult[i][j]=='015'):
            data="TeleTalk"
            datas.append(str(data))
            n=1
            if(n==1):
                data=int(myresult[i][j+1])
                datas.append(str(data))
                sumTEL=int(data)
                data=myresult[i][j+2]
                countTel=int(data)
                datas.append(str(data))
        if(myresult[i][j]=='018'):
            data="Robi"
            datas.append(str(data))
            n=1
            if(n==1):
                data=int(myresult[i][j+1])
                sumRobi=int(data)
                datas.append(str(data))
                data=data=myresult[i][j+2]
                countRobi=int(data)
                datas.append(str(data))
        if(myresult[i][j]=='016'):
            data="Airtel"
            datas.append(str(data))
            n=1
            if(n==1):
                data=int(myresult[i][j+1])
                sumAirtel=int(data)
                datas.append(str(data))
                data=data=myresult[i][j+2]
                countAirtel=int(data)
                datas.append(str(data))
        #datas.append(str(data)
TotalAmount=r+s+sumTEL+sumRobi+sumAirtel
TotalCount=count+count1+countTel+countRobi+countAirtel
datas.append('Total')
datas.append(TotalAmount)
datas.append(TotalCount)

for k in range(6):
    #print(datas)
    datas1.append(datas[st:en])
    #datas2.append(datas1[st:en])
    st=st+3
    en=en+3
   

    #x="\n".join(datas1)
    print("Hello",x)

#print(datas1)
df = pd.DataFrame(datas1, columns =['Operator', 'Amount','Count'],index=[1,2,3,4,5,6]) 
#print(df)

st1=0
en1=3
vendor=[]
vendor1=[]
indexlist=[]
index1=0
for ven in range(list_size):
    index1=index1+1
    indexlist.append(str(index1))
    for item in range(3):
        datavendor=(myresult1[ven] [item])
        vendor.append(str(datavendor))
    vendor1.append(vendor[st1:en1])
    st1=st1+3
    en1=en1+3
df1=pd.DataFrame(vendor1,columns=['Vendor', 'Amount','Count'],index=indexlist[0:index1])
#print(df1)    
   

sent_from = Hello.gmailaddress  
to = []

subject = 'Operatorwise Recharge Report of'+" "+date  
#body = "Dear All, "+'\n'+"Please find the recharge report of"+'\n'
t="to"

msg=MIMEMultipart("alternative")
msg['Subject'] = subject
msg['From'] = sent_from
msg['To'] = ','.join(to)

html = """\
    
    <html>
        <body>
           <p>Dear All,</p>

           <p style="color:Black; padding-bottom:5px; padding-top:5px; font-style: normal;font-size: 14px;font-weight: bold"> Greetings from Team IT Operations of SureCash.</p>

            <p style="color:Black; padding-bottom:5px; padding-top:5px; font-style: normal;font-size: 20px;font-weight: bold">Please find the Telco-wise Total Mobile Recharge Report of {0}</p> 

            {1} 

            <p style="color:Black; padding-bottom:5px; padding-top:5px; font-style: normal;font-size: 20px;font-weight: bold">Please find the Vendor-wise Total Mobile Recharge Report of {2}</p>

            {3}
             

             
             <p style="color:Black; padding-bottom:5px; padding-top:5px; font-style: normal;font-size: 14px;font-weight: bold"> Vendor Contact Number:</p>
             <p style="color:Black; padding-bottom:5px; padding-top:5px; font-style: normal;font-size: 14px;font-weight: bold"> SSD Suport: Support NUmber</p>
             <p style="color:Black; padding-bottom:5px; padding-top:5px; font-style: normal;font-size: 14px;font-weight: bold"> PortWallet: Support NUmber</p>
             <p style="color:Black; padding-bottom:5px; padding-top:5px; font-style: normal;font-size: 14px;font-weight: bold"> PranRFL: Support NUmber</p>
             <p style="color:Black; padding-bottom:5px; padding-top:5px; font-style: normal;font-size: 14px;font-weight: bold">This is auto generated mail</p> 

         </body>
    </html>
    """.format(date,df.to_html(),date,df1.to_html())







#part1 = MIMEText(email_text,'plain')
part2 = MIMEText(html, 'html')

    
    

#msg.attach(part1)
msg.attach(part2)



try:  
    server = smtplib.SMTP_SSL('Using SMTP', PORT NUMBER)
    server.ehlo()
    server.login(Hello.gmailaddress, Hello.gmailpassword)
    server.sendmail(sent_from, to, msg.as_string())
    server.close()

    print ('Email sent!')
except:  
    print ('Something went wrong...')