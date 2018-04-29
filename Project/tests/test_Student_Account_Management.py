import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)

def test_urls(self):
    response = self.client.get('/account/')
    self.assertEquals(response.status_code, self.expected_response_200)
    response = self.client.get('/account/BookLesson')
    self.assertEquals(response.status_code, self.expected_response_301)
    response = self.client.get('/account/ManageContract')
    self.assertEquals(response.status_code, self.expected_response_301)
    response = self.client.get('/account/HireIntstrument')
    self.assertEquals(response.status_code, self.expected_response_301)
    response = self.client.get('/account/ConfirmContract')
    self.assertEquals(response.status_code, self.expected_response_301)
    response = self.client.get('/account/Feedback')
    self.assertEquals(response.status_code, self.expected_response_301)



if __name__ == '__main__':
    unittest.main()
