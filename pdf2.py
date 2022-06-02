import datetime
from pdfminer.high_level import extract_text
import re
# import pandas as pd

def find_date(string):
    result = re.search('(.*)For electricity', string)
    result = result.group(1).replace('th', '').replace('rd', '').replace('st', '').replace('nd', '')
    result = datetime.datetime.strptime(result, '%d %B %Y')
    return result

# print(datetime.strptime('11 April 2022', '%d %b %Y'))
today = datetime.datetime.now()


# print(today + one_week) # 2019-12-30 11:58:52.073407

text  = extract_text('./my.pdf', 'rb')
lines = text.splitlines()

count = 0
for line in lines:
    count += 1
    if re.search("For electricity", line): #filter meter lines
        dates = find_date(line)
        print(f'***line {count}: {dates}')
        result = line.split('kWhCost p')
        word = re.findall(r'\S+',  line)
        for data in word:
            # if re.search(":", data):
                try:
                    # newtime = datetime.strptime(data[0:5], '%H:%M')
                    hours = datetime.timedelta(hours=int(data[0:2]))
                    mins = datetime.timedelta(minutes=int(data[3:5]))
                    times = dates + hours + mins
                    print(f'{dates + hours + mins}, {data[5:10]}') #  {data[5:9]},
                except:
                    print("An exception occurred")

                
                # print(dates + one_week)
        print(result[1])

'''23:00
 - 23:30
 15.27
 0.09
 1.313
23:30
 - 00:00
 15.27
 0.10
 1.466'''