import requests

class APIClient:

    @staticmethod
    def get(url, headers=None, timeout=10):
        return requests.get(url, headers=headers, timeout=timeout)

    @staticmethod
    def post(url, data=None, json=None, headers=None, timeout=10):
        return requests.post(url, data=data, json=json, headers=headers, timeout=timeout)

    @staticmethod
    def put(url, data=None, json=None, headers=None, timeout=10):
        return requests.put(url, data=data, json=json, headers=headers, timeout=timeout)

    @staticmethod
    def delete(url, headers=None, timeout=10):
        return requests.delete(url, headers=headers, timeout=timeout)
