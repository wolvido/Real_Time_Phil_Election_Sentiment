import threading
from datetime import datetime
import os

######### Leni ratio ###########
posLen = "lenPos"
negLen = "lenNeg"
ratioLen = "ratio"
tweetLen = "lenSum"
################################

######### marcos ratio #########
posMarcos = "marcosPos"
negMarcos = "marcosNeg"
marcosRatio = "marcosRatio"
tweetMar = 'marSum'
################################

######### Isko ratio ###########
posIsko = "iskoPos"
negIsko = "iskoNeg"
iskoRatio = "iskoRatio"
tweetko = 'koSum'
################################

######### Pacqiaou ratio #######
posManny = "pacqiaouPos"
negManny = "pacqiaouNeg"
ratioManny = "mannyRatio"
tweetMan = 'pacSum'
################################

######### Lacson ratio #########
lacPos = "lacPos"
lacNeg = "lacNeg"
laRatio = "lacsonRatio"
################################

def ratioPos(pos,neg): #returns the percentage of pos between the two numbers
    total = pos + neg
    return round(((pos/total)*100))


def sumCount(file): #sum of all recorded numbers in the file
    given_file = open(f'C:\\Users\\Winzyl\\Desktop\\migrate\\data\\{file}.csv', 'r')
    lines = given_file.readlines()
    sum = 0
    for line in lines:
        for c in line:
            if c.isdigit() == True:
                sum = sum + int(c)
    return sum


def ratioToCsv(posFile,negFile, file): #stores the ratio result to a csv to be used by frontend
    threading.Timer(1800.0, ratioToCsv, (posFile,negFile,file)).start() #runs code on a separate thread every 30 sec in order to match frontend update cycle
    pos = sumCount(posFile)
    neg = sumCount(negFile)
    posRatio = ratioPos(pos,neg)
    print(posRatio)
    file_import(str(posRatio), file)

def file_import(text, file): #saves a text in a csv file separated by a nextline, if file doesnt exist; creates one
    if os.path.isfile(f'C:\\Users\\Winzyl\\Desktop\\migrate\\data\\{file}.csv'):
        with open(f'C:\\Users\\Winzyl\\Desktop\\migrate\\data\\{file}.csv', 'a') as f: # able to append data to file
            f.write(text+"\n") 
    else:
        with open(f'C:\\Users\\Winzyl\\Desktop\\migrate\\data\\{file}.csv', 'x') as f:
            f.write(text+"\n")

def tweetCount(posFile,negFile, file): #stores the sum of all tweets result to a csv to be used by frontend
    threading.Timer(1800.0, tweetCount, (posFile,negFile,file)).start() #runs code on a separate thread every 30 sec in order to match frontend update cycle
    pos = sumCount(posFile)
    neg = sumCount(negFile)
    tweetSum = pos + neg
    print(tweetSum)
    file_import(str(tweetSum), file)


def countTimer():   
    threading.Timer(1800.0, countTimer).start()
    now = datetime.now()
    file_import(now.strftime("%Y-%m-%d %H:%M"), 'lenDates')
 


def counter(sentiment): #records the amount of positive and negative sentiment for each candidate to be used for graphs and returns the original sentiment for use
    ###### leni ########
    if "Positive sentiment" in sentiment and "Leni Tag:" in sentiment:
        file_import('1', 'lenPos')
        print("plus 1 positive leni")
    elif "Negative sentiment" in sentiment and "Leni Tag:" in sentiment:
        file_import('1', 'lenNeg')
        print("plus 1 negative leni")

    ###### marcos ########
    elif "Positive sentiment" in sentiment and "Marcos Tag:" in sentiment:
        file_import('1', 'marcosPos')
        print("plus 1 positive marcos")
    elif "Negative sentiment" in sentiment and "Marcos Tag:" in sentiment:
        file_import('1', 'marcosNeg')
        print("plus 1 negative marcos")

    ###### Isko ########
    elif "Positive sentiment" in sentiment and "Isko Tag:" in sentiment:
        file_import('1', 'iskoPos')
        print("plus 1 positive isko")
    elif "Negative sentiment" in sentiment and "Isko Tag:" in sentiment:
        file_import('1', 'iskoNeg')
        print("plus 1 negative isko")  

    ###### Pacqiaou ########
    elif "Positive sentiment" in sentiment and "Pacqiaou Tag:" in sentiment:
        file_import('1', 'pacqiaouPos')
        print("plus 1 positive pacqiaou")
    elif "Negative sentiment" in sentiment and "Pacqiaou Tag:" in sentiment:
        file_import('1', 'pacqiaouNeg')
        print("plus 1 negative pacqiaou")

    ###### Lacson ########
    # elif "Positive sentiment" in sentiment and "Lacson Tag:" in sentiment:
    #     file_import('1', 'lacsonPos')
    #     print("plus 1 positive lacson")
    # elif "Negative sentiment" in sentiment and "Lacson Tag:" in sentiment:
    #     file_import('1', 'lacsonNeg')
    #     print("plus 1 negative lacson")      

    else:
        print("Error counter")

    return sentiment

def main():
    ratioToCsv(posLen,negLen,ratioLen)
    ratioToCsv(posMarcos,negMarcos,marcosRatio)
    ratioToCsv(posIsko,negIsko,iskoRatio)
    ratioToCsv(posManny,negManny,ratioManny)

    tweetCount(posLen,negLen, tweetLen)
    tweetCount(posMarcos,negMarcos, tweetMar)
    tweetCount(posIsko,negIsko, tweetko)
    tweetCount(posManny,negManny, tweetMan)
    countTimer()

if __name__ == "__main__": #means the code will only execute if the module is not imported
    main()