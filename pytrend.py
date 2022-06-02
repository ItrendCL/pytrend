import urllib
import requests

class itrend_developer_tools():
    
    def __init__(self, access_key_id = None, secret_access_key = None):
        
        if access_key_id is None and secret_access_key is None:
            pass
        elif not self._are_valid_credentials(access_key_id, secret_access_key):
            raise TypeError('access_key_id and secret_access_key must be str, not %s and %s' %(type(access_key_id), type(secret_access_key)))
        
        self.headers = {
            'access_key_id': access_key_id,
            'secret_access_key': secret_access_key
        }
        
        self.itrendApi = 'https://6olpgdxhp8.execute-api.us-east-1.amazonaws.com/prod/itrend-developer-tools'
        
    def _are_valid_credentials(self, access_key_id, secret_access_key):
        if not isinstance(access_key_id, str) or not isinstance(secret_access_key, str):
            return False
        else:
            return True
        
    def set_credentials(self, access_key_id = None, secret_access_key = None):
        
        if not self._are_valid_credentials(access_key_id, secret_access_key):
            raise TypeError('access_key_id and secret_access_key must be str, not %s and %s' %(type(access_key_id), type(secret_access_key)))
        
        self.headers = {
            'access_key_id': access_key_id,
            'secret_access_key': secret_access_key
        }
        
    def get_credentials(self):
        return self.headers
    
    def get_dataset_formats(self, dataset_id, access_key_id = None, secret_access_key = None):

        # Check inputs
        if not isinstance(dataset_id, str):
            raise TypeError('dataset_id must be str, not %s' %type(dataset_id))

        # Check credentials
        if access_key_id is None and secret_access_key is None:
            headers = self.get_credentials()
            if headers.get('access_key_id') is None or headers.get('secret_access_key') is None:
                raise Exception('No credentials provided')
                
        elif not self._are_valid_credentials(access_key_id, secret_access_key):
            raise TypeError('access_key_id and secret_access_key must be str, not %s and %s' %(type(access_key_id), type(secret_access_key)))
        else:
            headers = {
                'access_key_id': access_key_id,
                'secret_access_key': secret_access_key
            }

        params = {
            'dataset_id': dataset_id,
            'getFormats': 'true'
        }
        
        response = requests.get(self.itrendApi, params=params, headers=headers)
        body = response.json()

        if response.status_code == 200:
            return body['formats']
        else:
            raise Exception('Invalid credentials')

    def get_element_formats(self, dataset_id, access_key_id = None, secret_access_key = None):

        # Check inputs
        if not isinstance(dataset_id, str):
            raise TypeError('dataset_id must be str, not %s' %type(dataset_id))

        # Check credentials
        if access_key_id is None and secret_access_key is None:
            headers = self.get_credentials()
            if headers.get('access_key_id') is None or headers.get('secret_access_key') is None:
                raise Exception('No credentials provided')
                
        elif not self._are_valid_credentials(access_key_id, secret_access_key):
            raise TypeError('access_key_id and secret_access_key must be str, not %s and %s' %(type(access_key_id), type(secret_access_key)))
        else:
            headers = {
                'access_key_id': access_key_id,
                'secret_access_key': secret_access_key
            }

        params = {
            'dataset_id': dataset_id,
            'getFormats': 'true',
            'collectionFormats': 'true'
        }
        
        response = requests.get(self.itrendApi, params=params, headers=headers)
        body = response.json()

        if response.status_code == 200:
            return body['formats']
        else:
            raise Exception('Invalid credentials')

    def download_file(self, dataset_id, fmt, element_id = None, filename = None,
                      access_key_id = None, secret_access_key = None):
        
        # Check inputs
        if not isinstance(dataset_id, str):
            raise TypeError('dataset_id must be str, not %s' %type(dataset_id))
        
        if not isinstance(fmt, str):
            raise TypeError('fmt must be str, not %s' %type(fmt))
            
        if element_id is not None:
            if not isinstance(element_id, str):
                raise TypeError('element_id must be str, not %s' %type(element_id))

            element_id = self._normalizeString(element_id)
        
        # Check credentials
        if access_key_id is None and secret_access_key is None:
            headers = self.get_credentials()
            if headers.get('access_key_id') is None or headers.get('secret_access_key') is None:
                raise Exception('No credentials provided')
                
        elif not self._are_valid_credentials(access_key_id, secret_access_key):
            raise TypeError('access_key_id and secret_access_key must be str, not %s and %s' %(type(access_key_id), type(secret_access_key)))
        else:
            headers = {
                'access_key_id': access_key_id,
                'secret_access_key': secret_access_key
            }
            
        params = {
            'dataset_id': dataset_id,
            'fmt': fmt,
            'element_id': element_id
        }
        
        response = requests.get(self.itrendApi, params=params, headers=headers)
        body = response.json()
        
        if response.status_code == 200:
            url = body.get('url')
            
            if filename is None:
                filename = body.get('filename')
                
            delimiter = body.get('delimiter')
            if delimiter == 'pipe':
                delimiter = '|'
            
            response.close()
            try:
                _ = urllib.request.urlretrieve(url, filename)
                output = {
                    'filename': filename,
                    'delimiter': delimiter
                }
                return output
            except:
                raise Exception('Incorrect parameters. Check your dataset_id, fmt and, if given, element_id')
        else:
            raise Exception('Invalid credentials')

    def _normalizeString(self, s1):
        s2 = s1.replace(" ", '')
        s2 = s2.replace("Á", 'A')
        s2 = s2.replace("É", 'E')
        s2 = s2.replace("Í", 'I')
        s2 = s2.replace("Ó", 'O')
        s2 = s2.replace("Ú", 'U')
        s2 = s2.replace("á", 'a')
        s2 = s2.replace("é", 'e')
        s2 = s2.replace("í", 'i')
        s2 = s2.replace("ó", 'o')
        s2 = s2.replace("ú", 'u')
        s2 = s2.replace("Ü", 'U')
        s2 = s2.replace("ü", 'u')
        s2 = s2.replace("Ñ", 'N')
        s2 = s2.replace("ñ", 'n')
        s2 = s2.replace(".", '')
        s2 = s2.replace(",", '')
        s2 = s2.replace(":", '')
        s2 = s2.replace("_", '')
        s2 = s2.replace("[", '')
        s2 = s2.replace("]", '')
        s2 = s2.replace("(", '')
        s2 = s2.replace(")", '')
        s2 = s2.replace("!", '')
        s2 = s2.replace("?", '')
        s2 = s2.replace("*", '')
        s2 = s2.replace("-", '')
        s2 = s2.replace("'", '')
        s2 = s2.replace('"', '')
        s2 = s2.replace("^", '')
        s2 = s2.replace("<", '')
        s2 = s2.replace(">", '')
        s2 = s2.replace("{", '')
        s2 = s2.replace("}", '')
        s2 = s2.replace("#", '')
        s2 = s2.replace("%", '')
        s2 = s2.replace("~", '')
        s2 = s2.replace("|", '')
        return s2
