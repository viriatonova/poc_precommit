from django.test import TestCase
from django.urls import reverse


class SampleTest(TestCase):
    def test_sample(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        json_content = str(response.content, encoding='utf8')
        self.assertJSONEqual(json_content, {'status': 'api' })
