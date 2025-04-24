import requests

class APIClient:
    def __init__(self, base_url):
        self.session = requests.Session()
        self.base_url = base_url

    def get(self, path, **kwargs):
        return self.session.get(self.base_url + path, **kwargs)

    def post(self, path, **kwargs):
        return self.session.post(self.base_url + path, **kwargs)

    def put(self, path, **kwargs):
        return self.session.put(self.base_url + path, **kwargs)

    def delete(self, path, **kwargs):
        return self.session.delete(self.base_url + path, **kwargs)

