import requests
import json

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

        {"value": "( #LeniKiko2022 OR Leni Robredo OR leni robredo) -is:retweet -is:reply", "tag":"Leni"},

        {"value": "(#BBMDuwag OR #BBMSara2022 OR #BBMSaraUniteam OR Bong Bong Marcos OR bong bong marcos OR bbm OR BBM) -is:retweet -is:reply", "tag":"Marcos"},

        {"value": "Ping Lacson -is:retweet -is:reply", "tag":"Lacson"},

        {"value": "Manny Pacqiaou -is:retweet -is:reply", "tag":"Pacqiaou"},

        {"value": "Isko Moreno -is:retweet -is:reply", "tag":"Isko"},

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

def get_stream(set):
    response = requests.get(
        "https://api.twitter.com/2/tweets/search/stream", auth=bearer_oauth, stream=True,
    )
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Cannot get stream (HTTP {}): {}".format(
                response.status_code, response.text
            )
        )
    for response_line in response.iter_lines():
        if response_line:
            json_response = json.loads(response_line)
            # print(json.dumps(json_response, indent=4, sort_keys=True))
            print(json.dumps((json_response['matching_rules'][0]['tag'])+" Tag: "+(json_response['data']['text']), indent=4, sort_keys=True))

def main():
    rules = get_rules()
    delete = delete_all_rules(rules)
    set = set_rules(delete)
    get_stream(set)

if __name__ == "__main__": #means the code will only execute if the module is not imported
    main()