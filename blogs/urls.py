from django.urls import path

from . import views

app_name = "blogs"
urlpatterns = [
    ## Menampilkan daftar blogs
    # ex: /blogs/
    path('', views.index, name='index'),

    ## Menampilkan entry (tulisan) di setiap blog
    # ex: /blogs/entry/2/
    path('entry/<int:blog_id>/', views.blog_entries, name='blog_entries'),
    # ex: /blogs/entry/detail/4/
    path('entry/detail/<int:entry_id>/', views.entry_detail, name='entry_detail'),

    ## Menampilkan entry (tulisan) dari setiap Author (penulis)
    # ex: /blogs/entry/author/1/
    path('entry/author/<int:author_id>/', views.author_entries, name='author_entries'),

    ## Menambahkan entry (tulisan) ke dalam blog, 
    ## tetapi hanya bisa dilakukan oleh Author (penulis) setelah login.
    # ex: /blogs/entry/1/add/
    path('entry/<int:blog_id>/add/', views.add_entry, name='add_entry'),
]
