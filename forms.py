from wtforms import Form, StringField, SelectField

class KYCSearchForm(Form):
    choices = [
        ('PEP', 'PEP'),
        ('Company Roles', 'Company Roles'),
        ('Company', 'Company')
    ]
    select = SelectField('Do a KYC Search:', choices = choices)
    search = StringField("")