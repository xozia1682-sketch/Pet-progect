import pytest
import requests




class GetClient():
    def __init__(self,session, base_url):
        self.session = session
        self.base_url = base_url

    def get_data(self):
        return self.session.get(self.base_url)

