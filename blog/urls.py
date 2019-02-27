"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# include lets you create extra url files
from django.conf.urls import url, include
from django.contrib import admin
# Redirect View allows you to redirect to a view
from django.views.generic import RedirectView
from django.views.static import serve
# You need to import media root to be able to serve out the media url
from .settings import MEDIA_ROOT

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # The root directory, this takes the user to posts
    url(r'^$', RedirectView.as_view(url='posts/')),
    # If someone goes to the posts url, pass it using the urls in the posts app
    url(r'posts/', include('posts.urls')),
    # The media, using a regexp you point towards a path to a particular file. Then using the serve library serve up document_root: MEDIA_ROOT
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT }),
]