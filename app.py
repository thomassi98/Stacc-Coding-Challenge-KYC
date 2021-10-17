from flask import Flask, jsonify, flash, render_template, request, redirect
from stacc_api import Stacc_API
from forms import KYCSearchForm

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.secret_key = 'dev'

#Task a)
#Web app and search functions. Inspired by https://www.blog.pythonlibrary.org/2017/12/13/flask-101-how-to-add-a-search-form/
@app.route('/', methods = ["GET", "POST"])
def index():
    search = KYCSearchForm(request.form)
    if request.method == "POST":
        return search_results(search)

    return render_template('index.html', form=search)


@app.route('/results')
def search_results(search):
    search_string = search.data['search']
    selected_string = search.select.data

    if search_string != '':
        data = get_response(selected_string, search_string)
        if data:
            #selected = selected_string.replace(' ', '_').lower()
            return render_template(f'{selected_string}_data_table.html', data = data, search_string = search_string, selected = selected_string)

    flash('No results found')
    return redirect('/')


def get_response(selection, search):
    '''
    Uses selection argument to call the correct get function from stacc_api
    Param selection: String with selected search type, eg. PEP
    Param search: search String
    returns: Api response json
    '''
    if selection == 'PEP':
        return get_PEP(search)
    elif selection == 'company_roles':
        return Stacc_API.get_roles(search) #Roles are returned as list, not json
    elif selection == 'company':
        return get_company(search)
    else:
        return None


#Task b)
#API part
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