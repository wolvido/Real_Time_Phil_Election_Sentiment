import os
import threading
# def file_import(file):

#     if os.path.isfile('C:\\Users\\Winzyl\\Desktop\\migrate\\filename.txt'):
#         with open('C:\\Users\\Winzyl\\Desktop\\migrate\\filename.txt', 'a') as f: # able to append data to file
#             f.write(file+"\n") 
#     else:
#         with open('C:\\Users\\Winzyl\\Desktop\\migrate\\filename.txt', 'x') as f:
#             f.write(file+"\n")

# def text_export():
#     with open('C:\\Users\\Winzyl\\Desktop\\migrate\\filename.txt', 'r') as f:
#         return(f.read().splitlines()[-1])

# for line in reversed(list(open('C:\\Users\\Winzyl\\Desktop\\migrate\\filename.csv'))):
#     print(line.rstrip())



# with open('filename', 'a') as f: # able to append data to file
# 	f.write('data') 

# with open('filename', 'r') as f: # able to read data from file ( also is the default mode when opening a file in python)

# with open('filename', 'x') as f: # Creates new file, if it already exists it will cause it to fail

# with open('filename', 't') as f: # opens the file in text mode (also is defualt)


# def ratioPos(pos,neg): #returns the percentage of pos between the two numbers
#     if pos > neg:
#         return round(100 -((neg/pos)*100))
#     else:
#         return round((pos/neg)*100)


# print(ratioPos(600,10))

# print(ratioPos(10,600))


# # with open('C:\\Users\\Winzyl\\Desktop\\migrate\\posLen.csv', 'r') as f:
# #     totalLenPos = [list(f.read())]
# #     print(sum(totalLenPos))


# # def sumCount(file): #sum of all recorded numbers in a file
# #     given_file = open(file, 'r')
# #     lines = given_file.readlines()
# #     sum = 0

# #     for line in lines:
# #         for c in line:
# #             if c.isdigit() == True:
# #                 sum = sum + int(c)
# #     return sum

# # print(sumCount('C:\\Users\\Winzyl\\Desktop\\migrate\\lenPos.csv'))
# # print(sumCount('C:\\Users\\Winzyl\\Desktop\\migrate\\lenNeg.csv'))

# # def file_import(text, file):
# #     if os.path.isfile(f'C:\\Users\\Winzyl\\Desktop\\migrate\\{file}.csv'):
# #         with open(f'C:\\Users\\Winzyl\\Desktop\\migrate\\{file}.csv', 'a') as f: # able to append data to file
# #             f.write(text+"\n") 
# #     else:
# #         with open(f'C:\\Users\\Winzyl\\Desktop\\migrate\\{file}.csv', 'x') as f:
# #             f.write(text+"\n")

# # file_import("brah",'successFile')

# # def counter(sentiment): #records the amount of positive and negative sentiment for each candidate to be used for graphs and returns the original sentiment for use
# #     if "Positive sentiment" in sentiment and "Leni Tag:" in sentiment:
# #         # file_import('1', 'lenPos')
# #         print("plus 1 positive")
# #     if "Negative sentiment" in sentiment and "Leni Tag:" in sentiment:
# #         # file_import('1', 'lenNeg')
# #         print("plus 1 negative")
# #     else:
# #         print("Error counter")

# # counter("Leni Tag: leni robredo negative : Negative sentiment")

# # from datetime import datetime
# # from threading import Timer

# # def print_periodicaly():
# #     Timer(5, print_periodicaly).start()
# #     print("working ertykjghfgdfzghjkkjhgfgkjfhghlikujyhgfglikujyhtgrikujh")

# # print_periodicaly()
# # while True:
# #     print("ongoing")


# # def ratioToCsv(posFile,negFile, file): #stores the ratio result to a csv to be used by frontend
# #     pos = sumCount(posFile)
# #     neg = sumCount(negFile)
# #     posRatio = ratioPos(pos,neg)
# #     print(posRatio)
# #     file_import(str(posRatio), file)

# # posFile = 'C:\\Users\\Winzyl\\Desktop\\migrate\\lenPos.csv'
# # negFile = 'C:\\Users\\Winzyl\\Desktop\\migrate\\lenNeg.csv'
# # file = 'ratio'

# # ratioToCsv(posFile,negFile,file)

# # import threading

# # def printit():
# #   threading.Timer(0.1, printit).start()
# #   print("Hello, World!")


# # printit()

# # while True:
# #     print("vbnbvbshwhdwhwidhiwdihwidh")
# def file_import(text, file): #saves a text in a csv file separated by a nextline, if file doesnt exist; creates one
#     if os.path.isfile(f'C:\\Users\\Winzyl\\Desktop\\migrate\\{file}.csv'):
#         with open(f'C:\\Users\\Winzyl\\Desktop\\migrate\\{file}.csv', 'a') as f: # able to append data to file
#             f.write(text+"\n") 
#     else:
#         with open(f'C:\\Users\\Winzyl\\Desktop\\migrate\\{file}.csv', 'x') as f:
#             f.write(text+"\n")

# # def text_export():
# #     with open('C:\\Users\\Winzyl\\Desktop\\migrate\\filename.csv', 'r') as f:
# #         return(f.read().splitlines()[-1])

# def ratioPos(pos,neg): #returns the percentage of pos between the two numbers
#     if pos > neg:
#         return round(100 -((neg/pos)*100))
#     else:
#         return round((pos/neg)*100)

# def sumCount(file): #sum of all recorded numbers in the file
#     given_file = open(f'C:\\Users\\Winzyl\\Desktop\\migrate\\{file}.csv', 'r')
#     lines = given_file.readlines()
#     sum = 0
#     for line in lines:
#         for c in line:
#             if c.isdigit() == True:
#                 sum = sum + int(c)
#     return sum

# def ratioToCsv(posFile,negFile, file): #stores the ratio result to a csv to be used by frontend
#     threading.Timer(30.0, ratioToCsv, (posFile,negFile,file)).start() #runs code on a separate thread every 30 sec in order to match frontend update cycle
#     pos = sumCount(posFile)
#     neg = sumCount(negFile)
#     posRatio = ratioPos(pos,neg)
#     print(posRatio)
#     file_import(str(posRatio), file)

# posLen = "lenPos"
# negLen = "lenNeg"
# ratioLen = "ratio"
# ratioToCsv(posLen,negLen,ratioLen)

# from datetime import datetime
# now = datetime.now()
# print (now.strftime("%Y-%m-%d %H:%M:%S"))

# def file_import(text, file): #saves a text in a csv file separated by a nextline, if file doesnt exist; creates one
#     if os.path.isfile(f'C:\\Users\\Winzyl\\Desktop\\migrate\\{file}.csv'):
#         with open(f'C:\\Users\\Winzyl\\Desktop\\migrate\\{file}.csv', 'a') as f: # able to append data to file
#             f.write(text+"\n") 
#     else:
#         with open(f'C:\\Users\\Winzyl\\Desktop\\migrate\\{file}.csv', 'x') as f:
#             f.write(text+"\n")

# file_import(now.strftime("%Y-%m-%d %H:%M:%S"), 'test')

def ratioPos(pos,neg): #returns the percentage of pos between the two numbers
    total = pos + neg
    return round(((pos/total)*100))

print(ratioPos(5,20))