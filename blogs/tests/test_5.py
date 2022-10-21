from .test_base import BaseTests


class FifthTests(BaseTests):
    def test_author1_entries(self):
        response = self.client.get('/blogs/entry/author/1/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'headline1')
        self.assertContains(response, 'headline2')
        self.assertContains(response, 'headline3')
        self.assertContains(response, 'headline4')
        self.assertContains(response, 'author1')
        self.assertNotContains(response, 'author2')
        self.assertNotContains(response, 'author3')
    
    def test_author2_entries(self):
        response = self.client.get('/blogs/entry/author/2/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'headline2')
        self.assertContains(response, 'headline4')
        self.assertContains(response, 'author2')
        self.assertNotContains(response, 'headline1')
        self.assertNotContains(response, 'headline3')
        self.assertNotContains(response, 'author3')
        self.assertNotContains(response, 'author1')
