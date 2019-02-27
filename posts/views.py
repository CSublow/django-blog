from django.shortcuts import render, get_object_or_404, redirect # get_object_or_404 and redirect help you serve urls, or return an error
from django.utils import timezone
from .models import Post
from .forms import BlogPostForm

def get_posts(request):
    """ 
    Create a view that will return a list of posts that were published prior to now
    Render the posts to the 'blogposts.html' template 
    """
    
    # Create posts object
    # Filter all of the posts by the published date, those less than or equal to timezone now
    # Order by published date in descending order
    # You will get an error from c9 saying 'Class Post has no objects member'. Django sorts this out under the hood.
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    # Use the render library to return the blogposts.html template, which will contain the list of posts
    return render(request, "blogposts.html", {'posts': posts})
    
def post_detail(request, pk):
    """
    Create a view that returns a single post object based on the post ID (pk)
    Render the post to the 'postdetails.html' template
    Or return a 404 error if the post is not found
    """
    # get_object_or_404 gets the Post item based on the Post ID
    post = get_object_or_404(Post, pk=pk)
    # Every time we view the post (i.e the view is called), views go up by 1
    post.views += 1
    post.save()
    # Render the postdetail.html template, send the post object
    return render(request, "postdetail.html", {'post': post})
    
def create_or_edit_post(request, pk=None):
    """
    Create a view that allows users to create or edit a post
    Depending if the Post ID is null or not
    """
    
    # get_object_or_404 either gets the object or returns a 404
    post = get_object_or_404(Post, pk=pk) if pk else None
    # If the form is posted
    if request.method == "POST":
        # Render the blogpostform
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            # Redirect to the post detail using the post id
            return redirect(post_detail, post.pk)
            
    else:
        form = BlogPostForm(instance=post)
    
    return render(request, "blogpostform.html", {'form': form})