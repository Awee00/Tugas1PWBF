from .test_base import BaseTests
from django.contrib.auth.models import User


class SixthTests(BaseTests):
    def setUp(self) -> None:
        User.objects.create_user(username='user1', password='password1')
        return super().setUp()

    def test_add_entry_blog1_no_login(self):
        response = self.client.get('/blogs/entry/1/add/')
        self.assertEqual(response.status_code, 302)

    def test_add_entry_blog2_no_login(self):
        response = self.client.get('/blogs/entry/2/add/')
        self.assertEqual(response.status_code, 302)

    def test_add_entry_blog1_login(self):
        self.client.login(username='user1', password='password1')
        response = self.client.get('/blogs/entry/1/add/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['blog'].id, 1)
        self.assertContains(response, 'Tambah Entry')
        self.assertContains(response, 'blog1')
        self.assertNotContains(response, 'blog2')
        self.assertNotContains(response, 'headline1')

    def test_add_entry_blog2_login(self):
        self.client.login(username='user1', password='password1')
        response = self.client.get('/blogs/entry/2/add/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['blog'].id, 2)
        self.assertContains(response, 'Tambah Entry')
        self.assertContains(response, 'blog2')
        self.assertNotContains(response, 'blog1')
        self.assertNotContains(response, 'headline1')
