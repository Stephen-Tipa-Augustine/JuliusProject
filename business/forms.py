from django import forms
from . import models


class ListCreationForm(forms.ModelForm):
    class Meta:
        tag_choice = [("very popular", "very popular"), ("popular", "popular"), ("not that popular", "not that popular"),
                      ("just new", "just new")]
        category_choice = [("service Business", "service Business"), ("Merchandising Business", "Merchandising Business"),
                           ("Manufacturing Business", "Manufacturing Business")]
        form_choice = [("Sole Proprietorship", "Sole Proprietorship"), ("Partnership", "Partnership"), ("Corporation", "Corporation"),
                       ("Limited Liability Company", "Limited Liability Company"), ('Cooperative', 'Cooperative')]
        model = models.Listing
        fields = ("name", "tag", "address", "location", 'category', 'form', "overview", "logo")
        labels = {
            'name': 'Name of the business', 'tag': 'It\'s Ranking', 'address': 'The Business Web Address',
            'location':'The physical location of the business', 'overview':'A brief business overview',
            'logo':'A logo or image of the business', 'category':'Business Category', 'form':'form of business ownership'
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Short Descriptive Name', 'class':'form-control w-100'}),
            'location': forms.TextInput(attrs={'placeholder': 'e.g kampala along Jinja Road', 'class':'form-control w-100'}),
            'overview': forms.Textarea(
                attrs={'placeholder': 'Overview of the business', 'rows': 9, 'cols': 30, 'class':'form-control w-100'}),
            'address':forms.URLInput(attrs={'placeholder':'e.g https://www.businessA.com', 'class':'form-control w-100'}),
            'tag': forms.Select(choices=tag_choice, attrs={'placeholder':'Select From Dropdown', 'class':'form-control w-100'}),
            'category': forms.Select(choices=category_choice,
                                attrs={'placeholder': 'Select From Dropdown', 'class': 'form-control w-100'}),
            'form': forms.Select(choices=form_choice,
                                attrs={'placeholder': 'Select From Dropdown', 'class': 'form-control w-100'})
        }

class CommentCreationForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ("comment", 'user', 'email')
        widgets = {
            'comment': forms.Textarea(
                attrs={'placeholder': 'Enter Message', 'rows': 9, 'cols': 30, 'class': 'form-control w-100','name':'message',
                       'id': 'message', 'onfocus':"this.placeholder = ''", 'onblur':"this.placeholder = 'Enter Message'"}),
            'user': forms.TextInput(
                attrs={'placeholder': 'Your Name', 'class': 'form-control w-100', 'name':'user',
                       'id': 'user', 'onfocus':"this.placeholder = ''",
                       'onblur': "this.placeholder = 'Your Name'"}),
            'email': forms.TextInput(
                attrs={'placeholder': 'Email address', 'class': 'form-control w-100','name':'email',
                       'id': 'email', 'onfocus':"this.placeholder = ''",
                       'onblur': "this.placeholder = 'Email address'"})
        }

class BlogCreationForm(forms.ModelForm):
    class Meta:
        categories = [('All Categories', 'All Categories'), ('Restaurant Food','Restaurant Food'),
                      ('Travel News','Travel News'), ('Modern Technology','Modern Technology'),
                      ('Products', 'Products'), ('Inspirational','Inspirational'), ('Health Care','Health Care')]
        model = models.Blog
        fields = ('name', 'category', 'post', 'photo')
        labels = {'name':'Title of the blog', 'post':'Your Blog Post Data', 'photo': 'An optional image upload for your post'}
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'e.g The Wonder of current world businesses', 'class':'form-control w-100', 'id':'name'}),
            'post': forms.Textarea(
                attrs={'placeholder': 'Text of your blog post...', 'rows': 9, 'cols': 30, 'class':'form-control w-100', 'id':'comment'}),
            'category': forms.Select(choices=categories,
                                attrs={'placeholder': 'Select From Dropdown', 'class': 'form-control w-100'}),
        }

class ContactCreationForm(forms.ModelForm):
    class Meta:
        model = models.Contact
        fields = '__all__'
        widgets = {
            'message': forms.Textarea(
                attrs={'placeholder': 'Enter Message', 'rows': 9, 'cols': 30, 'class': 'form-control w-100','name':'message',
                       'id': 'message', 'onfocus':"this.placeholder = ''", 'onblur':"this.placeholder = 'Enter Message'"}),
            'name': forms.TextInput(
                attrs={'placeholder': 'Your Name', 'class': 'form-control valid', 'name':'name',
                       'id': 'name', 'onfocus':"this.placeholder = ''",
                       'onblur': "this.placeholder = 'Your Name'"}),
            'email': forms.TextInput(
                attrs={'placeholder': 'Email address', 'class': 'form-control valid','name':'email',
                       'id': 'name', 'onfocus':"this.placeholder = ''",
                       'onblur': "this.placeholder = 'Email address'"}),
            'subject': forms.TextInput(
                attrs={'placeholder': 'Enter Subject', 'class': 'form-control valid', 'name':'subject',
                       'id': 'name', 'onfocus':"this.placeholder = ''",
                       'onblur': "this.placeholder = 'Enter Subject'"})
        }