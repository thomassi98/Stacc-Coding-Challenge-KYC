from flask import Flask, jsonify
from KYCSearch import Stacc_API

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to the KYC API"

@app.route('/PEP/name=<string:name>', methods = ['GET'])
def get_PEP(name):
    return Stacc_API.get_PEP(name)

@app.route('/roles/org_num=<int:org_num>', methods = ['GET'])
def get_roles(org_num):
    return jsonify(Stacc_API.get_roles(org_num))

@app.route('/company/org_num=<int:org_num>', methods = ['GET'])
def get_company(org_num):
    return Stacc_API.get_company(org_num)


if __name__ == "__main__":
    app.run(debug=True)