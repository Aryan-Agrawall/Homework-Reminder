import ezgmail
import datetime
from _datetime import date, timedelta
notification_sent = []
# put all the email ids in the below list
people = ["samplegmail1@gmail.com",
          "samplegmail2@gmail.com",
          ]
while True:
    reader = open("sample_hw.txt","r") # put your text file name here
    already = []
    read = reader.readlines()
    for item in read:
        if item not in already:
            already.append(item)
    now = datetime.datetime.now()
    
    for item in already:
        condition = False
        heading , work , deadline = item.split(" -- ")
        deadline_date ,deadline_month,deadline_year = map(int,deadline.split("/"))
        last_date = datetime.datetime(deadline_year,deadline_month,deadline_date)
        t1 = last_date-now
        t1 = str(t1)
        try:
            days,hours = t1.split(", ")
            days = days.strip(" days")
            days = int(days)
            if days == 1:
                condition = True
        except:
            condition = True
        if condition and work not in notification_sent:
            print("found")
            for jtem in people:
                content = "Dear "+jtem+"\n"+"work is : "+work+"\n"+"deadline is approaching!"+"\n"+"\n"+"Regards:"+"\n"+"hwreminder.py" # you can customize the content of the email
                subject = heading
                ezgmail.send(jtem, subject, content)
            notification_sent.append(work)
