from django.db import models
from django.utils import timezone # timezone lets you work with time and date

class Post(models.Model): #class Post is based off a standard model
    """ A single blog post """
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True) # auto_now_add means that as soon as the post is created, the current date/time will be added to this field
    # The created date might be different to the published date
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    # When a post is first created it has no views
    views = models.IntegerField(default=0)
    tag = models.CharField(max_length=30, blank=True, null=True)
    image = models.ImageField(upload_to="img", blank=True, null=True) # The 'img' corresponds to the directory you created under media
    
    def __unicode__(self):
        return self.title
    
    
