import unittest
import json
from api.views import app

class QuestionTestCase(unittest.TestCase):
    def setUp(self):
        self.sample_data = {
            'body':'What is HTML in full',
            'poster':'Robert'
        }

        # initialize the test client
        self.client = app.test_client()

    def test_add_question(self):
        response = self.client.post(
            '/api/v1/questions',
            data=json.dumps(self.sample_data),
            content_type='application/json'
        )
        resp_data = json.loads(response.data.decode())
        # assert keys
        self.assertIn('status', resp_data)
        self.assertIn('message', resp_data)
        self.assertIn('_id', resp_data)
        # assert expected data
        self.assertEqual(resp_data['status'],'ok')
        # assert expected status code
        self.assertEqual(response.status_code,201)
    
    def test_add_question_with_invalid_data(self):
        self.sample_data = {
            'body':'Wh',
            'poster':''
        }
        response = self.client.post(
            '/api/v1/questions',
            data=json.dumps(self.sample_data),
            content_type='application/json'
        )
        resp_data = json.loads(response.data.decode())
        # assert keys
        self.assertIn('status', resp_data)
        self.assertIn('message', resp_data)
        # assert expected data
        self.assertEqual(resp_data['message'],'Invalid input data')
    
    def test_add_answer(self):
        response = self.client.post(
            '/api/v1/questions',
            data=json.dumps(self.sample_data),
            content_type='application/json'
        )
        self.sample_data = {
            'response':'Python is a language',
            'username':'Robert'
        }
        
        response = self.client.post(
            '/api/v1/questions/1/answers',
            data=json.dumps(self.sample_data),
            content_type='application/json'
        )
        resp_data = json.loads(response.data.decode())
         # assert keys
        self.assertIn('status', resp_data)
        self.assertIn('message', resp_data)
        self.assertIn('id', resp_data)
        # assert expected data
        self.assertEqual(resp_data['status'],'ok')
        # assert expected status code
        self.assertEqual(response.status_code,201)