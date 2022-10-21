from django.test import TestCase
from blogs.models import Blog, Author, Entry


class BaseTests(TestCase):
    def setUp(self) -> None:
        author1 = Author.objects.create(name='author1', email='author1@coba.com')
        author2 = Author.objects.create(name='author2', email='author2@coba.com')
        
        blog1 = Blog.objects.create(name='blog1', tagline='tagline1')
        entry1 = Entry.objects.create(blog=blog1, headline='headline1', body_text='body_text1', pub_date='2021-01-01', mod_date='2021-01-01', number_of_comments=0, number_of_pingbacks=0, rating=5)
        entry1.authors.add(author1)
        entry2 = Entry.objects.create(blog=blog1, headline='headline2', body_text='body_text2', pub_date='2022-02-02', mod_date='2022-02-02', number_of_comments=0, number_of_pingbacks=0, rating=5)
        entry2.authors.add(author1, author2)
        
        blog2 = Blog.objects.create(name='blog2', tagline='tagline2')
        entry3 = Entry.objects.create(blog=blog2, headline='headline3', body_text='body_text3', pub_date='2023-03-03', mod_date='2023-03-03', number_of_comments=0, number_of_pingbacks=0, rating=5)
        entry3.authors.add(author1)
        entry4 = Entry.objects.create(blog=blog2, headline='headline4', body_text='body_text4', pub_date='2024-04-04', mod_date='2024-04-04', number_of_comments=0, number_of_pingbacks=0, rating=5)
        entry4.authors.add(author1, author2)
