import requests
import json
import os
from model import freqs,theta,predict_tweet
import threading
from datetime import datetime

# To set your enviornment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
# for windows $env:BEARER_TOKEN="xxx"
# $env:BEARER_TOKEN="AAAAAAAAAAAAAAAAAAAAANWTYgEAAAAA0FRIAvdNbnm8q69lTrOF%2BxXpdm8%3DJrqiRxj96oZ8RFEpb6yVqKYmo4rhzrtPB8nswLJZKf0vAUdzPs"

bearer_token = "AAAAAAAAAAAAAAAAAAAAAEoLZwEAAAAAsmwKH7vShh0Prf6J2Qugorw5kuc%3D5kjnuSBFoqigZ420KdVmOrpQkI1aK7ii9BFDP67CHx0S8BsSdl"
# bearer_token = "AAAAAAAAAAAAAAAAAAAAANWTYgEAAAAA0FRIAvdNbnm8q69lTrOF%2BxXpdm8%3DJrqiRxj96oZ8RFEpb6yVqKYmo4rhzrtPB8nswLJZKf0vAUdzPs"

def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2FilteredStreamPython"
    return r


def get_rules():
    response = requests.get(
        "https://api.twitter.com/2/tweets/search/stream/rules", auth=bearer_oauth
    )
    if response.status_code != 200:
        raise Exception(
            "Cannot get rules (HTTP {}): {}".format(response.status_code, response.text)
        )
    print(json.dumps(response.json()))
    return response.json()


def delete_all_rules(rules):
    if rules is None or "data" not in rules:
        return None

    ids = list(map(lambda rule: rule["id"], rules["data"]))
    payload = {"delete": {"ids": ids}}
    response = requests.post(
        "https://api.twitter.com/2/tweets/search/stream/rules",
        auth=bearer_oauth,
        json=payload
    )
    if response.status_code != 200:
        raise Exception(
            "Cannot delete rules (HTTP {}): {}".format(
                response.status_code, response.text
            )
        )
    print(json.dumps(response.json()))


def set_rules(delete):
    # You can adjust the rules if needed
    sample_rules = [
        # {"value": "dog has:images", "tag": "dog pictures"},
        # {"value": "cat has:images -grumpy", "tag": "cat pictures"},
        # {"value": "cat has:images -grumpy"},
        # {"value": "dog has:images"},

        {"value": "(#Kakampink OR #kakampink OR #LeniWanagSaDilim OR #LeniRobredo2022 OR #LeniKiko2022 OR Leni Robredo OR leni robredo) -is:retweet -is:reply -has:links", "tag":"Leni"},

        {"value": "(#BBMForPresident2022 OR #BBMDuwag OR #BBMSara2022 OR #BBMSaraUniteam OR Bong Bong Marcos OR bong bong marcos OR bbm OR BBM) -is:retweet -is:reply -has:links", "tag":"Marcos"},

        {"value": "(Ping Lacson OR #PingLacsonTayo OR #pinglacson) -is:retweet -is:reply -has:links", "tag":"Lacson"},

        {"value": "(Manny Pacquiao OR pacquiao) -is:retweet -is:reply -has:links", "tag":"Pacqiaou"},

        {"value": "(#IskoMoreno OR Isko Moreno OR Isko Domagoso Moreno OR #KayIskoPosible OR #SwitchToIsko) -is:retweet -is:reply -has:links", "tag":"Isko"},

        # {"value": "Leni Robredo -is:retweet -is:reply -has:links"},
        # {"value": "Bong Bong Marcos -is:retweet -is:reply -has:links"},
        # {"value": "Ping Lacson -is:retweet -is:reply -has:links"},
        # {"value": "Manny Pacqiaou -is:retweet -is:reply -has:links"},
        # {"value": "Isko Moreno -is:retweet -is:reply -has:links"},

        # {"value": "(Leni Robredo OR BongBong Marcos OR Ferdinand Romualdez Marcos) -is:reply"},
        # {"value": "#SMNIdebates2022"}
    ]
    payload = {"add": sample_rules}
    response = requests.post(
        "https://api.twitter.com/2/tweets/search/stream/rules",
        auth=bearer_oauth,
        json=payload,
    )
    if response.status_code != 201:
        raise Exception(
            "Cannot add rules (HTTP {}): {}".format(response.status_code, response.text)
        )
    print(json.dumps(response.json()))

def predict(tweet):
    y_hat = predict_tweet(tweet, freqs, theta)
    if y_hat > 0.5:
        print(tweet +' : Positive sentiment \n')
        return(tweet +' : Positive sentiment')
        
    else: 
        print(tweet +' : Negative sentiment \n')
        return(tweet +' : Negative sentiment')

def file_import(text, file): #saves a text in a csv file separated by a nextline, if file doesnt exist; creates one
    if os.path.isfile(f'C:\\Users\\Winzyl\\Desktop\\migrate\\data\\{file}.csv'):
        with open(f'C:\\Users\\Winzyl\\Desktop\\migrate\\data\\{file}.csv', 'a') as f: # able to append data to file
            f.write(text+"\n") 
    else:
        with open(f'C:\\Users\\Winzyl\\Desktop\\migrate\\data\\{file}.csv', 'x') as f:
            f.write(text+"\n")

# def text_export():
#     with open('C:\\Users\\Winzyl\\Desktop\\migrate\\filename.csv', 'r') as f:
#         return(f.read().splitlines()[-1])

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
    threading.Timer(30.0, ratioToCsv, (posFile,negFile,file)).start() #runs code on a separate thread every 30 sec in order to match frontend update cycle
    pos = sumCount(posFile)
    neg = sumCount(negFile)
    posRatio = ratioPos(pos,neg)
    print(posRatio)
    file_import(str(posRatio), file)
    
def countTimer():   
    threading.Timer(30.0, countTimer).start()
    now = datetime.now()
    file_import(now.strftime("%Y-%m-%d %H:%M:%S"), 'lenDates')
    

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
    elif "Positive sentiment" in sentiment and "Lacson Tag:" in sentiment:
        file_import('1', 'lacsonPos')
        print("plus 1 positive lacson")
    elif "Negative sentiment" in sentiment and "Lacson Tag:" in sentiment:
        file_import('1', 'lacsonNeg')
        print("plus 1 negative lacson")      

    else:
        print("Error counter")

    return sentiment

######### Leni ratio ###########
posLen = "lenPos"
negLen = "lenNeg"
ratioLen = "ratio"
################################

######### marcos ratio #########
posMarcos = "marcosPos"
negMarcos = "marcosNeg"
marcosRatio = "marcosRatio"
################################

######### Isko ratio ###########
posIsko = "iskoPos"
negIsko = "iskoNeg"
iskoRatio = "iskoRatio"
################################

######### Pacqiaou ratio #######
posManny = "pacqiaouPos"
negManny = "pacqiaouNeg"
ratioManny = "mannyRatio"
################################

######### Lacson ratio #########
lacPos = "lacPos"
lacNeg = "lacNeg"
laRatio = "lacsonRatio"
################################

def get_stream(set):
    response = requests.get(
        "https://api.twitter.com/2/tweets/search/stream", auth=bearer_oauth, stream=True,
    )
    print(str(response.status_code) + " : Twitter API connected")
    if response.status_code != 200:
        raise Exception(
            "Cannot get stream (HTTP {}): {}".format(
                response.status_code, response.text
            )
        )
    for response_line in response.iter_lines():
        if response_line:
            json_response = json.loads(response_line)
            file_import(counter(predict(json.dumps((json_response['matching_rules'][0]['tag'])+" Tag: "+(json_response['data']['text']), indent=4, sort_keys=True))),'filename')

def main():
    ratioToCsv(posLen,negLen,ratioLen)
    ratioToCsv(posMarcos,negMarcos,marcosRatio)
    ratioToCsv(posIsko,negIsko,iskoRatio)
    ratioToCsv(posManny,negManny,ratioManny)
    ratioToCsv(lacPos,lacNeg,laRatio)
    countTimer()
    rules = get_rules()
    delete = delete_all_rules(rules)
    set = set_rules(delete)
    get_stream(set)
    

if __name__ == "__main__": #means the code will only execute if the module is not imported
    # main()
    while True:
        try:
            main()
        except KeyError:
            print('restarting')

