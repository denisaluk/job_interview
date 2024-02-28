import unittest
import requests
import json
import datetime


class TestCase1(unittest.TestCase):

    def setUp(self):
        url = 'https://reqres.in/api/users'
        post_data = { "name": "morpheus" , "job": "leader" }

        self.response = requests.post(url, json=post_data)

        # test correct response code
        self.assertEqual(201, self.response.status_code)
        # test valid json
        json.loads(self.response.text)

    def testResponseData(self):
        response = self.response
        self.assertTrue(response.json().get('id'))
        self.assertTrue(response.json().get('createdAt'))
        created = datetime.datetime.strptime(response.json().get('createdAt'), "%Y-%m-%dT%H:%M:%S.%fZ")
        header_time = datetime.datetime.strptime(response.headers.get('Date'), "%a, %d %b %Y %H:%M:%S GMT")
        self.assertEqual(created.ctime(),header_time.ctime())

    def testResponseTime(self):
        response = self.response
        limit = 0.1 # 100ms
        self.assertLess(response.elapsed.total_seconds(), limit, 'Response time is more than limit')


if __name__ == "__main__":
    unittest.main()