from datetime import datetime
from pdfminer.high_level import extract_text
import re
import pandas as pd






text  = extract_text('./my.pdf', 'rb')


lines = text.splitlines()

count = 0
for line in lines:
    count += 1
    if re.search("electricity meter 19L3278767", line):
        # datetime_object = datetime.strptime(line[0:25
        # ]  , '%d   %b %Y')
        print(f'***line {count}: {line[0:30]}')

        word = re.findall(r'\S+',  line)
        for data in word:
            iftime = data[0:5]




            # print(f'{data[0:5]}, {data[10:-4]} ') #  {data[5:9]},





