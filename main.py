from flask import Flask, request
from flask_restful import Resource, Api
import requests
from get_salesforce_data import *
from threading import Thread
import json
from store_data import update_excel

app = Flask(__name__)
api = Api(app)


def case_details(api_endpoint, case_number, comment):
    case_fields = get_data(case_number)
    if len(case_fields) == 1:
        out_data = {
                    "blocks":
                    [
                            {
                                "type": "section",
                                "text": {
                                        "type": "mrkdwn",
                                        "text": "Provided Case number does not exist. Please mention the correct one."
                                        }
                            }
                    ]
                }
        requests.post(url=api_endpoint, headers=const.headers, data=json.dumps(out_data))
    elif len(case_fields) == 2:
        out_data = {
            "blocks":
                [
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": str(case_fields.get('text'))
                        }
                    }
                ]
        }
        requests.post(url=api_endpoint, headers=const.headers, data=json.dumps(out_data))
    else:
        update_excel(case_fields, comment)
        out_data = {
            "blocks":
                [
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "Case details are updated in the repository!!:thankyou:"
                        }
                    }
                ]
        }
        requests.post(url=api_endpoint, headers=const.headers, data=json.dumps(out_data))


class SlackServer(Resource):
    def post(self):
        api_endpoint = request.values['response_url']
        data = request.values['text'].split()
        case_number = data[0]
        comment = " ".join(data[1:])
        print(case_number)
        print(comment)
        if data[0].isnumeric() and len(data[0]) == 8:
            thr = Thread(target=case_details, args=[api_endpoint, case_number, comment])
            thr.start()
            return ':mag_right: Your Requested has been submitted.Please wait for a while :mag:'
        else:
            return 'Please enter the valid 8 digit Case Number along with comment For example 00012345 Please \
            respond to customer'


api.add_resource(SlackServer, '/slackserver')


if __name__ == '__main__':
    app.run(debug=True)



