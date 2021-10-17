from flask import Flask, jsonify
from werkzeug.utils import redirect
from KYCSearch import Stacc_API
from forms import KYCSearchForm
from flask import flash, render_template, request

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

#Search functionality inspiration: https://www.blog.pythonlibrary.org/2017/12/13/flask-101-how-to-add-a-search-form/
@app.route('/', methods = ["GET", "POST"])
def index():
    search = KYCSearchForm(request.form)
    if request.method == "POST":
        return search_results(search)

    return render_template('index.html', form=search)


@app.route('/results')
def search_results(search):
    results = []
    search_string = search.data('search')
    
    #If no search
    if search.data['search'] == '':
        flash('Nothing to search for')
    if not results:
        flash('No results found')
        return redirect('/')
    else:
        return render_template('results.html', resutls = results)

#API
@app.route('/API/PEP/name=<string:name>', methods = ['GET'])
def get_PEP(name):
    return Stacc_API.get_PEP(name)

@app.route('/API/roles/org_num=<int:org_num>', methods = ['GET'])
def get_roles(org_num):
    return jsonify(Stacc_API.get_roles(org_num))

@app.route('/API/company/org_num=<int:org_num>', methods = ['GET'])
def get_company(org_num):
    return Stacc_API.get_company(org_num)


if __name__ == "__main__":
    app.run(debug=True)