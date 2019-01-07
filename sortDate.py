from collections import *
# transfer month to related num
def month_string_to_number(string):
    m = {
        'jan': 1,
        'feb': 2,
        'mar': 3,
        'apr': 4,
        'may': 5,
        'jun': 6,
        'jul': 7,
        'aug': 8,
        'sep': 9,
        'oct': 10,
        'nov': 11,
        'dec': 12
    }
    s = string.strip()[:3].lower()

    try:
        out = m[s]
        return out
    except:
        return False


# multiple receiver

def splitReceiver(receiverGroup):
    str=receiverGroup.split(',')
    Receiver=[]
    for receiver in str:
        if receiver.find('@') > 0:
            Receiver.append(receiver.strip("'"))
    return Receiver

def cmpDate(x,y):
    if x[0]<y[0]:
        return -1
    elif x[0]>y[0]:
        return 1
    elif x[1]<y[1]:
        return -1
    elif x[1]>y[1]:
        return 1
    elif x[2]<y[2]:
        return -1
    else:
        return 1


def nothave(str):
    if str.find("@")==-1:
        return False

def extractInfo(line):
    #return a list to store the tuple
    list_return=[]
    # delete the outer parenthesis
    str1 = line[1:-2]
    # divide the string into three groups
    if "\"" not in str1:
        group = str1.split("', ")
        senderGroup=group[0]
        if senderGroup.find("@")<0:
            return False
        receiverGroup=group[1].strip("'")
        if receiverGroup.find("@")<0:
            return False
        Receiver= splitReceiver(receiverGroup)
        timeGroup=group[2].split(' ')
        Sender=senderGroup.strip("'")
        if month_string_to_number(timeGroup[2]) is not False:
            if int(timeGroup[3])>=2000 and int(timeGroup[3])<=2003:
                date=(int(timeGroup[3]), month_string_to_number(timeGroup[2]), int(timeGroup[1]))
            else:
                return False
        else:
            return False
        for i in Receiver:
            list_return.append((date,(Sender,i)))
        return list_return
    else:
        return False

# extract date from D:/PythonFile/result.txt, and transform it to the format (year, month, day)
# for further comparison, using a dict to store the data {(date):(sender, receiver)}

resultDict =defaultdict(list)
result_list=[]
n=0
m=0
with open('D:/PythonFile/result.txt', 'r') as f:
    for i in f:
        a=extractInfo(i)
        if a is not False:
            if a[0][0] not in resultDict:
                resultDict[a[0][0]]=[]
                resultDict[a[0][0]].append(a[0][1])
            else:
                resultDict[a[0][0]].append(a[0][1])
        else:
            n=n+1
        m=m+1

sorted_dates=sorted(resultDict.keys(), cmp=cmpDate)

# for date in sorted_dates:
#     print date
#     print resultDict[date]

print n
with open('D:/PythonFile/resultDict1.txt','a') as f:
    for i in sorted_dates:
        f.write(str(i)+'\n')
        f.write(str(resultDict[i])+'\n')

