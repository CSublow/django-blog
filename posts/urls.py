from django.conf.urls import url
from .views import get_posts, post_detail, create_or_edit_post

urlpatterns = [
    # This first one is the root directory for the posts app
    # It is using the get_posts view
    url(r'^$', get_posts, name='get_posts'),
    # The next one has a group which indicates a decimal number which is your id. So if it is passed in with an id you want to open the post_detail view
    url(r'^(?P<pk>\d+)/$', post_detail, name='post_detail'),
    # url for creating a new post
    url(r'^new/$', create_or_edit_post, name='new_post'),
    # url for if a user wants to edit
    url(r'^(?P<pk>\d+)/edit/$', create_or_edit_post, name='edit_post')
    ]