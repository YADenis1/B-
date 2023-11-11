import argparse
import os
from subprocess import call
test = False
def addS(key, mean):
    translateDict[str(key)] = str(mean)
translateDict = {}
loadpath = os.getcwd()
if not test:
    parser = argparse.ArgumentParser(description='Input path.')
    parser.add_argument('path', metavar='N', type=str, nargs='+',
                        help='path to your Vkk program')
    args = parser.parse_args()
    pathtoPO = args.path[0]

    print(pathtoPO)
else:
    pathtoPO = os.getcwd()+"\\"+"программушка.ВКК"

rusSimv = list("ёйцукенгшщзхъфывапролджэячсмитьбю") + list("ёйцукенгшщзхъфывапролджэячсмитьбю".upper())
nerusSimv = ["'", '"']
with open("знанья.txt", 'r') as file:
    for i in file:
        addS(i.split()[0], i.split()[1])
    
with open("знанья.txt", 'w') as file:
    for key in translateDict:
        print(key + " " + translateDict[key], file=file)
data = []
with open(pathtoPO, 'r', encoding="utf-8") as file:
    newVars = 0
    openedApostr = [0, 0]
    for i in file:
        tempstring = str(i)
        for key in translateDict:
            tempstring = tempstring.replace(key, translateDict[key])
        openedScope = False
        for j in tempstring.split():
            isRusSimv = False
            for symv in list(j):
                if symv in nerusSimv:
                    if symv == "'" or symv == '"':
                        openedScope = not openedScope
                    break
                if symv in rusSimv:
                    isRusSimv = True
                if openedScope:
                    isRusSimv = False
            if isRusSimv:
                addS(j, "Var"+str(newVars))
                newVars+=1
                tempstring = tempstring.replace(j, translateDict[j])
        data.append(tempstring)
data.append("\ninput('Ведай любую кнопушку')")
with open(loadpath+"\\"+pathtoPO.split('\\')[-1:][0][:-4]+".py", 'w', encoding="utf-8") as filewrite:
    for i in data:
        filewrite.write(i)
    filewrite.close()
call("python "+loadpath+"\\"+pathtoPO.split('\\')[-1:][0][:-4]+".py")
if test:
    input("Ведай любую кнопушку")
    print(translateDict)
