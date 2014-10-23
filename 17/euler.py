import sys

strList = map(lambda x:str(x), range(1,1001))

#3桁目をパース
headDic = {'1':'one hundred ',
            '2':'two hundred ',
            '3':'three hundred ',
            '4':'four hundred ',
            '5':'five hundred ',
            '6':'six hundred ',
            '7':'seven hundred ',
            '8':'eight hundred ',
            '9':'nine hundred ',
        }
twoDigitDic = {'10':'ten ',
            '11':'eleven ',
            '12':'twelve ',
            '13':'thirteen ',
            '14':'fourteen ',
            '15':'fifteen ',
            '16':'sixteen ',
            '17':'seventeen ',
            '18':'eighteen ',
            '19':'nineteen ',
            '2':'twenty ',
            '3':'thirty ',
            '4':'forty ',
            '5':'fifty ',
            '6':'sixty ',
            '7':'seventy ',
            '8':'eighty ',
            '9':'ninety ',
        }
oneDigitDic = { '1':'one',
        '2':'two',
        '3':'three',
        '4':'four',
        '5':'five',
        '6':'six',
        '7':'seven',
        '8':'eight',
        '9':'nine',
        '0':'',
        }
def headParser(some):
    if len(some) == 3:
        # get head
        key = some[0]
        if headDic.get(key):
            return headDic[key]
    else:
        return ''
def twoDigitParser(some):
    if len(some) == 3 or len(some) == 2: 
        andFix = ''
        if len(some) == 3:
            keyLevel1 = some[1:]
            andFix = 'and '
        elif len(some) == 2:
            keyLevel1 = some

        if keyLevel1[0] == '1':
            return andFix + twoDigitDic.get(keyLevel1)
        elif keyLevel1[0] != '0':
            keyLevel2 = keyLevel1[0]
            res = andFix + twoDigitDic.get(keyLevel2)
            if keyLevel2 != '1':
                res += oneDigitDic.get(keyLevel1[-1])
            return res
        else:
            keyLevel3 = keyLevel1[-1]
            if keyLevel3 == '0':
                andFix = ''
            return andFix + oneDigitDic.get(keyLevel3)
    if len(some) == 1:
        return oneDigitDic.get(some)
    if len(some) == 4:
        return 'one thousand'
    return ''
            
if __name__ == '__main__':
    lengthBuff = 0
    for some in strList:
        result = ''.join( [headParser(some), twoDigitParser(some)] ).strip()
        lengthBuff += len(result.replace(' ',''))
        print result, len(result), lengthBuff
