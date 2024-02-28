import unittest
import requests
import json


class TestCase1(unittest.TestCase):

    def setUp(self):
        url = 'https://reqres.in/api/users?page=2'
        self.response = requests.get(url)
        # test correct response code
        self.assertEqual(200, self.response.status_code)
        # test valid json
        json.loads(self.response.text)

    def testTotal(self):
        response = self.response
        self.assertEqual(12, response.json().get('total'))

    def testLastName(self):
        response = self.response
        data = response.json().get('data')  # returns list of dictionaries
        self.assertEqual('Lawson',data[0].get('last_name'))
        self.assertEqual('Ferguson',data[1].get('last_name'))

    def testDataCount(self):
        response = self.response
        self.assertEqual(response.json().get('total'), response.json().get('data').__len__())


if __name__ == "__main__":
    unittest.main()