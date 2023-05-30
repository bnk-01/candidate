from django.views import generic
from .models import Post
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


class PostList(generic.ListView):
    """
        A view displaying a list of blog posts.

        Attributes:
            queryset (QuerySet): The queryset used to retrieve the blog posts.
            template_name (str): The name of the template used for rendering the view.
        """

    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'


class PostDetail(generic.DetailView):
    """
       A view displaying a single blog post.

       Attributes:
           model (Model): The model class representing the blog post.
           template_name (str): The name of the template used for rendering the view.
       """
    model = Post
    template_name = 'post_detail.html'


def home(request):
    """
      Renders the home page.

      Parameters:
          request (HttpRequest): The request object.

      Returns:
          HttpResponse: The rendered response.
      """
    return render(request, "home.html")


@login_required
def about(request):
    """
       Renders the about page, accessible only to authenticated users.

       Parameters:
           request (HttpRequest): The request object.

       Returns:
           HttpResponse: The rendered response.
       """
    return render(request, "about.html")
