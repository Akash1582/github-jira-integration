# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json
from flask import Flask, request
import os

app = Flask(__name__)

# Define a route that handles GET requests
@app.route('/createJira', methods=['POST'])
def createJira():

    request_data = request.get_json()  #It take request data in json format

    url = "https://bhesalakash123.atlassian.net//rest/api/3/issue"

    #Get the env variable from operating system using OS module
    API_TOKEN= os.getenv("API_Token")
    Username = ""  #Provide email address of jira account
    auth = HTTPBasicAuth(Username, API_TOKEN)

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    payload = json.dumps( {
        "fields": {
        "description": {
            "content": [
                {
                    "content": [
                        {
                            "text": "Order entry fails when selecting supplier.",
                            "type": "text"
                        }
                    ],
                    "type": "paragraph"
                    }
                ],
            "type": "doc",
             "version": 1
        },
        "project": {
           "key": "AK"
        },
        "issuetype": {
            "id": "10006"
        },
        "summary": request_data["issue"]["title"], #Here taking data from request body for issue name on Jira ticket
    },
    "update": {}
    } )

    if (request_data["comment"]["body"] == "/jira"):
        response = requests.request(
        "POST",
        url,
        data=payload,
        headers=headers,
        auth=auth
        )
        return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))
    else:
        return "Comment should be '/jira' "
    
    
@app.route('/')
def index():
    return "Hello this is api hosted for Github-Jira integration"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
