from django.db import models
from django.contrib.auth.models import User

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Post(models.Model):
    """
        Blog post Model.

        Attributes:
            title (str): The title of the blog post.
            slug (str): A slug field for the URL.
            author (User): The author of the blog post.
            updated_on (datetime): The date and time of the last update.
            content (str): The content of the blog post.
            created_on (datetime): The date and time of creation.
            status (int): The status of the blog post.

        Meta:
            This orders post by creation date.

        Methods:
            Returns the title of the blog post as a string.
        """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        """
            Returns the title of the blog post as a string.

         """
        return self.title
