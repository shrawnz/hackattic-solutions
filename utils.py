import requests
import base64
import json

access_token = ""

def get_challenge(name: str) -> str:
    resp = requests.get("https://hackattic.com/challenges/" + name  + "/problem?access_token=" +  access_token)
    return resp.text

def submit_challenge(name, data):
    resp = requests.post("https://hackattic.com/challenges/" + name  + "/solve?playground=1&access_token=" +  access_token, data=data)
    return resp.text

def base64encode(string):
    return base64.b64encode(string.encode())

def base64decode(b64string):
    return base64.b64decode(b64string)

if __name__ == "__main__":
    val = json.loads(get_challenge("help_me_unpack"))
    print(base64decode(val["bytes"]))
