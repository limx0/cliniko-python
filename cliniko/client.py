import os

from beckett import clients
from requests.auth import HTTPBasicAuth

from .resources import AppointmentTypes, Invoice, Patient


class ClinikoClient(clients.BaseClient):
    class Meta:
        name = 'Cliniko API Client'
        base_url = 'https://api.cliniko.com/v1'
        resources = (
            AppointmentTypes,
            Invoice,
            Patient,
        )

    def __init__(self, api_key):
        self.api_key = api_key
        super().__init__()
        self.session.auth = HTTPBasicAuth(self.api_key, None)

    @classmethod
    def from_environment(cls, env_var='CLINIKO_PYTHON_API_KEY'):
        return cls(api_key=os.environ[env_var])

    @classmethod
    def get_url(cls, url, uid, **kwargs):
        if kwargs.get('page'):
            return '{}?page={}'.format(url, kwargs.get('page'))
