import os, json
from chalice import Chalice
from dotenv import load_dotenv

load_dotenv()

app = Chalice(app_name='swifthire-app')


@app.route('/')
def connect_opensearch():
    return {os.getenv("APIFY_API_KEY")}


#chalice package packaged/
#aws cloudformation package --template-file sam.json --s3-bucket swifthire-chalice --output-template-file sam-packaged.yaml
#aws cloudformation deploy --template-file sam-packaged.yaml --stack-name swifthire-stack --capabilities CAPABILITY_IAM
#aws cloudformation describe-stacks --stack-name swifthire-stack

#https://oz9zqm8a23.execute-api.us-east-1.amazonaws.com/api/
#https://oz9zqm8a23.execute-api.us-east-1.amazonaws.com/api/



# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
