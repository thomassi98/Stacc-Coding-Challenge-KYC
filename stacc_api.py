import requests

class Stacc_API():
    '''
    Class for communicating with Stacc Code Challenge API
    '''
    base_uri = 'https://stacc-code-challenge-2021.azurewebsites.net/api/'

    def __get_data(param_string):
        """
        Take uri parameter string to get data from OpenSea API
        param_string: addition parameter to base uri, eg. "api/pep?name=Knut Arild Hareide"
        return: json or None if error status code
        """
        uri = Stacc_API.base_uri+param_string

        try:
            response = requests.get(uri)
            if response.status_code == 200:
                return response.json()
            else:
                print(f"Something went wrong getting the data. Error: {str(response.status_code)} {response.reason}")
                return None
        except requests.exceptions.RequestException as error:
            raise error


    def get_PEP(name):
        '''
        Send API Get request to search for and retriev PEP's
        param name: String with name to search for
        return: json with PEP info, None if none found
        '''
        return Stacc_API.__get_data(f'pep?name={name}')


    def health():
        '''
        Send API Get request to retrieve and return health status
        return: Header with API health status
        '''
        return requests.get('https://stacc-code-challenge-2021.azurewebsites.net/healthz').status_code == 200


    def get_roles(org_num):
        '''
        Send API Get request to search for and retriev roles in a company
        param org_num: String with organization number to search for
        return: json with company roles, None if none found
        '''
        return Stacc_API.__get_data(f'roller?orgNr={org_num}')


    def get_company(org_num):
        '''
        Send API Get request to search for and retrieve a company
        param org_num: String with organization number to search for
        return: json with company roles, None if none found
        '''
        return Stacc_API.__get_data(f'enheter?orgNr={org_num}')
