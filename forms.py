from wtforms import Form, StringField, SelectField

class KYCSearchForm(Form):
    choices = [
        ('PEP', 'Politically Exposed Person'),
        ('company_roles', 'Company Roles'),
        ('company', 'Company')
    ]
    select = SelectField('Search for:', choices = choices)

    search = StringField("Fill in name or organization number:")