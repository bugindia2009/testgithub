import os,datetime

os.chdir(r'E:\pythoninterviewquestions\newinterviewquestions')
for f in os.listdir():
    if  os.path.isfile(f):
        with open("interviewpython.txt","a",encoding="utf-8") as fl:
            p=os.path.getctime(f)
            k=str(datetime.datetime.fromtimestamp(p)) + "\t" + f + "\n"
            fl.write(k)
    