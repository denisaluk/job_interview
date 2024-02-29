import unittest
import requests
import json


class TestCase2(unittest.TestCase):

    def setUp(self):
        self.url = 'https://reqres.in/api/users'

    def testResponseData(self):

        with open('test_set.txt') as f:
            lines = f.readlines() #list of strings

        for line in lines:
            print(line)

            try:
                postdata = json.loads(line)
            except ValueError as err:
                postdata = line

            with self.subTest(postdata):
                response = requests.post(self.url, json=postdata)
                self.assertEqual(201, response.status_code)
                self.assertTrue(response.json().get('id'), 'Key ID not in response')
                self.assertTrue(response.json().get('createdAt'), 'Key CREATEDAT not in response')
                for key in postdata:
                    print(response.text)
                    self.assertEqual(postdata.get(key), response.json().get(key))


if __name__ == "__main__":
    unittest.main()