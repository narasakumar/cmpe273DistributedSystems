import sys
import requests
import base64
import json
import yaml
# from github import Github
# from github3 import GitHub,repos
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Dockerized Flask App!!"

@app.route("/v1/<filename>")
def get_file_content(filename):
    print filename
    url=sys.argv[1]
    api=""
    arr=url.split('/')
    # print arr
    userName=arr[3]
    repoName=arr[4]
    
    

    if(filename=="dev-config.json"): 
        api="https://api.github.com/repos/"+userName+"/"+repoName+"/contents/"+"dev-config.yml"
        print api
        response =requests.get(api,verify=False).json()
        print response["content"]
        encoded = response["content"]
        data = base64.b64decode(encoded)
        print data
        # YAML to JSON Conversion
        jsonData=json.dumps(yaml.load(data))
        print jsonData
        return jsonData
    elif(filename=="test-config.json"): 
        api="https://api.github.com/repos/"+userName+"/"+repoName+"/contents/"+"test-config.yml"
        print api
        response =requests.get(api,verify=False).json()
        print response["content"]
        encoded = response["content"]
        data = base64.b64decode(encoded)
        print data
        # YAML to JSON Conversion
        jsonData=json.dumps(yaml.load(data))
        print jsonData
        return jsonData
    else :
        api="https://api.github.com/repos/"+userName+"/"+repoName+"/contents/"+filename
        print api
        response =requests.get(api,verify=False).json()
        print response["content"]
        encoded = response["content"]
        data = base64.b64decode(encoded)
        print data
        return data

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
