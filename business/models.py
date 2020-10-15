from django.db import models
import re
from django.db.models.signals import pre_save

# Create your models here.

def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        name = instance.name
        name = name.lower()
        slug = re.sub(r' +', '-', name)
        instance.slug = slug


class Listing(models.Model):
    slug = models.SlugField(null=True, blank=True, help_text="A short description of the business for urls", max_length=100, unique=True)
    name = models.CharField(max_length=200, help_text="The name of the business", unique=True)
    address = models.URLField(help_text="The web address of the business")
    location = models.CharField(help_text="A short description of where the business in located", max_length=150)
    overview = models.TextField(help_text="A brief overview of the business")
    logo = models.ImageField(upload_to='listing/images/' ,help_text="The logo of the business", null=True, blank=True)
    tag = models.CharField(help_text="Helps to categorize the business", max_length=50)
    category = models.CharField(max_length=30, help_text='simple category for filtering', default='Service Business')
    form = models.CharField(max_length=30, help_text='for filtering', default='Cooperative')
    def __str__(self):
        return self.name

class Comment(models.Model):
    blog = models.CharField(help_text="The blog the comment is for", max_length=100)
    comment = models.TextField(help_text="The comment")
    user = models.CharField(help_text="The user who commented", null=True, blank=True, max_length=100)
    email = models.EmailField(help_text='Mail address of the commenter', null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, help_text="When the comment was added")
    def __str__(self):
        return self.blog

class Blog(models.Model):
    slug = models.SlugField(null=True, blank=True, help_text="short description of the blog", max_length=100, unique=True)
    name = models.CharField(help_text="Blog description", max_length=200, unique=True)
    blogger = models.CharField(max_length=20, help_text='user name of the blogger')
    post = models.TextField(help_text="blof post")
    overview = models.TextField(help_text="a brief overview to invoke eager", default="No overview has been entered for this blog")
    date = models.DateTimeField(auto_now_add=True ,help_text="When the blog post was written")
    category = models.CharField(max_length=50, help_text='Used for filtering', null=True, blank=True)
    comments = models.IntegerField(default=0, help_text='No of comments for particular blog')
    likes = models.IntegerField(default=0, help_text='No of likes for particular blog')
    photo = models.ImageField(upload_to='blog/images/' ,help_text="An Image for the blog", null=True, blank=True)
    def __str__(self):
        return self.name

class Contact(models.Model):
    message = models.TextField(help_text="User feedback")
    name = models.CharField(max_length=50, help_text="user name")
    email = models.EmailField(help_text='email of user')
    subject = models.CharField(max_length=100, help_text='Subject of the contact')
    def __str__(self):
        return self.subject

class UserRequest(models.Model):
    lookingFor = models.CharField(max_length=200, help_text='What the user want to be added to listing')
    def __str__(self):
        return self.lookingFor

class BlogLike(models.Model):
    blog = models.CharField(help_text="The blog the like is for", max_length=100)
    user = models.CharField(help_text="The user who liked", max_length=100)

class NewsLetterSubscription(models.Model):
    email = models.EmailField(help_text='email of subscriber')




pre_save.connect(slug_generator, sender=Listing)
pre_save.connect(slug_generator, sender=Blog)