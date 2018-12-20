import os
import fileinput


rootDir="C:/data/enron_mail_20150507/maildir"
def iter_files(rootDir):
    for root, dirs, files in os.walk(rootDir):
        for file in files:
            file_name = os.path.join(root, file)
            yield file_name
        for dirname in dirs:
            iter_files(dirname)

def isTupleFull(tuple):
    if tuple[0]!='' and tuple[1]!='' and tuple[2]!='':
        return True


def infoEx(rootDir):
    a=[]
    for file_name in iter_files(rootDir):
        Sender = ''
        Receiver = ''
        Time = ''
        for line in fileinput.input(file_name):
            line = line.rstrip()
            if line.startswith('Date:'):
                Time = line[6:]
            if line.startswith('From:'):
                Sender = line[6:]
            if line.startswith('To:'):
                Receiver = line[4:]

            if isTupleFull((Sender,Receiver,Time)):
                a.append((Sender, Receiver, Time))
                fileinput.close()
                break

    return a

result_file=open('D:/PythonFile/result.txt','a')
for i in infoEx(rootDir):
    result_file.write(str(i)+'\n')

# data = []
#
# for file in files:
#     if not os.path.isdir(file):
#         f = open(path + '/' + file)
#         print f
#         iter_f = iter(f)
#         for line in iter_f:
#             line = line.rstrip()
#             if line.startswith('From:'):
#                 Sender = line[6:]
#             if line.startswith('To:'):
#                 Receiver = line[4:]
#             if line.startswith('Date:'):
#                 Time = line[6:]
#                 data.append((Sender, Receiver, Time))
#
# print data

# file='D:/ttt/documents/a/1'
# def file2read(file):
#     for line in fileinput.input(file):
#         print line
#         break
#
# file2read(file)
