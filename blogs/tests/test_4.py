from .test_base import BaseTests


class FourthTests(BaseTests):
    def test_entry_detail1(self):
        response = self.client.get('/blogs/entry/detail/1/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'blog1')
        self.assertContains(response, 'headline1')
        self.assertContains(response, 'body_text1')
        self.assertContains(response, 'author1')
        self.assertNotContains(response, 'blog2')
        self.assertNotContains(response, 'headline2')
        self.assertNotContains(response, 'body_text2')
        self.assertNotContains(response, 'author2')
    
    def test_entry_detail2(self):
        response = self.client.get('/blogs/entry/detail/2/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'blog1')
        self.assertContains(response, 'headline2')
        self.assertContains(response, 'body_text2')
        self.assertContains(response, 'author1')
        self.assertContains(response, 'author2')
        self.assertNotContains(response, 'blog2')
        self.assertNotContains(response, 'headline1')
        self.assertNotContains(response, 'body_text1')
        self.assertNotContains(response, 'author3')
    
    def test_entry_detail3(self):
        response = self.client.get('/blogs/entry/detail/3/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'blog2')
        self.assertContains(response, 'headline3')
        self.assertContains(response, 'body_text3')
        self.assertContains(response, 'author1')
        self.assertNotContains(response, 'blog1')
        self.assertNotContains(response, 'headline1')
        self.assertNotContains(response, 'body_text1')
        self.assertNotContains(response, 'author2')
    
    def test_entry_detail4(self):
        response = self.client.get('/blogs/entry/detail/4/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'blog2')
        self.assertContains(response, 'headline4')
        self.assertContains(response, 'body_text4')
        self.assertContains(response, 'author1')
        self.assertContains(response, 'author2')
        self.assertNotContains(response, 'blog1')
        self.assertNotContains(response, 'headline1')
        self.assertNotContains(response, 'body_text1')
        self.assertNotContains(response, 'author3')
