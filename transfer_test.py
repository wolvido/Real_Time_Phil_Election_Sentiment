import os
def file_import(file):

    if os.path.isfile('C:\\Users\\Winzyl\\Desktop\\migrate\\filename.txt'):
        with open('C:\\Users\\Winzyl\\Desktop\\migrate\\filename.txt', 'a') as f: # able to append data to file
            f.write(file+"\n") 
    else:
        with open('C:\\Users\\Winzyl\\Desktop\\migrate\\filename.txt', 'x') as f:
            f.write(file+"\n")

def text_export():
    with open('C:\\Users\\Winzyl\\Desktop\\migrate\\filename.txt', 'r') as f:
        return(f.read().splitlines()[-1])

for line in reversed(list(open('C:\\Users\\Winzyl\\Desktop\\migrate\\filename.csv'))):
    print(line.rstrip())



# with open('filename', 'a') as f: # able to append data to file
# 	f.write('data') 

# with open('filename', 'r') as f: # able to read data from file ( also is the default mode when opening a file in python)

# with open('filename', 'x') as f: # Creates new file, if it already exists it will cause it to fail

# with open('filename', 't') as f: # opens the file in text mode (also is defualt)
