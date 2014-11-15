import re,sys

rows = open('./p089_roman.txt').read()
print len(rows) - len(re.sub('DCCCC|LXXXX|VIIII|CCCC|XXXX|IIII', '**', rows))
