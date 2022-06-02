from io import StringIO
from pdfminer.high_level import extract_text
text  = extract_text('./my.pdf', 'rb')
# print(text)

import slate3k as slate
text  = slate.PDF(open('./my.pdf', 'rb')).text()


print(text)