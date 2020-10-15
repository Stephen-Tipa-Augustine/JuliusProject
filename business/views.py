from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from django.contrib.auth.decorators import login_required
from . import models

# Create your views here.

def index(request):
    popular = [i for i in models.Listing.objects.all() if i.tag in ["very popular", 'popular']]
    blogs = models.Blog.objects.order_by('date')
    blogs = [blogs[i] for i in range(len(blogs) - 1, -1, -1)]
    recentBlogs = blogs[: 4] if len(blogs) > 4 else blogs
    if request.method == 'POST':
        if request.POST.get('id') == "simple":
            keyword = request.POST.get('keyword')
            searchResults = [i for i in models.Listing.objects.all() if keyword in i.name]
        else:
            keyword = request.POST.get('keyword')
            categoryFilter = request.POST.get('select')
            if categoryFilter != 'All Catagories':
                filter1 = [i for i in models.Listing.objects.all() if categoryFilter == i.category]
                searchResults = [i for i in filter1 if keyword in i.name]
            else:
                searchResults = [i for i in models.Listing.objects.all() if keyword in i.name]
        return render(request, 'business/show-search-results.html', {'searchResults':searchResults})
    return render(request, 'main/index.html', {'popular': popular, 'blogs':recentBlogs})
def about(request):
    dirs = models.Listing.objects.all()
    popular = [i for i in models.Listing.objects.all() if i.tag in ["very popular", 'popular']]
    return render(request, 'business/about.html', {'listings':dirs, 'popular':popular})
def listing(request):
    dirs = models.Listing.objects.all()
    popular = [i for i in models.Listing.objects.all() if i.tag in ["very popular", 'popular']]
    query = []
    showQueries = False
    if request.method == 'POST':
        data = request.POST
        keyword = data.get('keyword')
        categoryOfItem = data.get('category')
        form = data.get('form')
        tag = data.get('tag')
        showQueries = True
        if categoryOfItem == form == tag:
            query = [i for i in models.Listing.objects.all() if keyword in i.name]
        elif categoryOfItem == 'All' and form != 'All' and tag != 'All':
            query = models.Listing.objects.filter(form=form, tag=tag).values()
        elif categoryOfItem != 'All' and form == 'All' and tag != 'All':
            query = models.Listing.objects.filter(category=categoryOfItem, tag=tag).values()
        elif categoryOfItem != 'All' and form != 'All' and tag == 'All':
            query = models.Listing.objects.filter(form=form, category=categoryOfItem).values()
        elif categoryOfItem != 'All' and form != 'All' and tag != 'All':
            query = models.Listing.objects.filter(form=form, tag=tag, category=categoryOfItem).values()
    return render(request, 'business/listing.html', {'showQueries':showQueries, 'listings': dirs, 'popular': popular, 'queries': query})
def listingDetails(request, slug):
    listing = get_object_or_404(models.Listing, slug=str(slug))
    popular = [i for i in models.Listing.objects.all() if i.tag in ["very popular", 'popular']]
    if request.method == 'POST':
        form = forms.ContactCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        form = forms.ContactCreationForm()
    return render(request, 'business/listing_details.html', {'contactCreationForm':form, 'listing':listing, 'popular':popular})

@login_required(login_url='auth:login')
def addListing(request):
    popular = [i for i in models.Listing.objects.all() if i.tag in ["very popular", 'popular']]
    if request.method == 'POST':
        form = forms.ListCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        form = forms.ListCreationForm()
    return render(request, 'business/add-listing.html', {'listingCreationForm':form, 'popular':popular})
def contact(request):
    popular = [i for i in models.Listing.objects.all() if i.tag in ["very popular", 'popular']]
    if request.method == 'POST':
        form = forms.ContactCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'business/record-added.html', {'popular': popular})
    else:
        form = forms.ContactCreationForm()
    return render(request, 'business/contact.html', {'contactCreationForm':form, 'popular':popular})
def blog(request):
    dirs = models.Listing.objects.all()
    popular = [i for i in models.Listing.objects.all() if i.tag in ["very popular", 'popular']]
    blogs = models.Blog.objects.order_by('date')
    blogs = [blogs[i] for i in range(len(blogs) - 1, -1, -1)]
    recentBlogs = blogs[: 4] if len(blogs) > 4 else blogs
    return render(request, 'business/blog.html', {'blogs':blogs, 'listings':dirs, 'popular':popular, 'recentBlogs':recentBlogs})

@login_required(login_url='auth:login')
def addBlog(request):
    dirs = models.Listing.objects.all()
    popular = [i for i in models.Listing.objects.all() if i.tag in ["very popular", 'popular']]
    if request.method == 'POST':
        form = forms.BlogCreationForm(request.POST, request.FILES)
        if form.is_valid():
            formObj = form.save(commit=False)
            post = request.POST.get('post')
            formObj.overview = post[:20] + '...'
            formObj.save()
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        form = forms.BlogCreationForm()
    return render(request, 'business/add-blog.html', {'blogCreationForm':form, 'listings':dirs, 'popular':popular})
def privacy(request):
    dirs = models.Listing.objects.all()
    popular = [i for i in models.Listing.objects.all() if i.tag in ["very popular", 'popular']]
    return render(request, 'business/element.html', {'listings':dirs, 'popular':popular})
def category(request):
    dirs = models.Listing.objects.all()
    categ = {'Manufacturing Business':[i for i in dirs if i.category == 'Manufacturing Business'],
             'Service Business':[i for i in dirs if i.category == 'service Business'],
             'Merchandising Business':[i for i in dirs if i.category =='Merchandising Business']}
    popular = [i for i in models.Listing.objects.all() if i.tag in ["very popular", 'popular']]
    return render(request, 'business/category.html', {'listings':dirs, 'popular':popular, 'category_content':categ})
def blogQueryResults(request):
    queries = []
    recentBlogs = [i for i in models.Blog.objects.all()]
    recentBlogs = [recentBlogs[i] for i in range(len(recentBlogs) - 1, -1, -1)]
    recentBlogs = recentBlogs[: 4] if len(recentBlogs) > 4 else recentBlogs
    if request.method == 'POST':
        keyword = request.POST.get('keyword')
        queries = [i for i in models.Blog.objects.all() if keyword in i.name]
    return render(request, 'business/blog-query-results.html', {'queries':queries, 'recentBlogs':recentBlogs})
def blogCategoryContent(request, slug):
    recentBlogs = [i for i in models.Blog.objects.all()]
    recentBlogs = [recentBlogs[i] for i in range(len(recentBlogs) - 1, -1, -1)]
    recentBlogs = recentBlogs[: 4] if len(recentBlogs) > 4 else recentBlogs
    if str(slug) == 'All Categories':
        blogs = models.Blog.objects.all()
    else:
        blogs = models.Blog.objects.filter(category=str(slug)).values()
    return render(request, 'business/blog-category-content.html', {'categoryContent':blogs, 'recentBlogs':recentBlogs})
def blogDetails(request, slug):
    blogs = [i for i in models.Blog.objects.all()]
    blogs = [blogs[i] for i in range(len(blogs)-1, -1, -1)]
    recentBlogs = blogs[: 4] if len(blogs) > 4 else blogs
    comm = models.Comment.objects.filter(blog=str(slug)).values()
    popular = [i for i in models.Listing.objects.all() if i.tag in ["very popular", 'popular']]
    blog = get_object_or_404(models.Blog, slug=slug)
    #Logic for checking next and previous blogs starts here
    blogIndex=blogs.index(blog)
    numberOfBlogs = len(blogs)
    if blogIndex == 0 and numberOfBlogs == 1:
        previousPostIndex = None
        nextPostIndex = None
    elif blogIndex == 0 and numberOfBlogs >1:
        previousPostIndex = None
        nextPostIndex = 1
    elif blogIndex == numberOfBlogs-1 and numberOfBlogs == 1:
        previousPostIndex = None
        nextPostIndex = None
    elif blogIndex == numberOfBlogs-1 and numberOfBlogs > 1:
        previousPostIndex = -2
        nextPostIndex = None
    elif (blogIndex != 0 or blogIndex != numberOfBlogs-1) and (numberOfBlogs>1):
        previousPostIndex = blogIndex-1
        nextPostIndex = blogIndex+1

    if previousPostIndex is None and nextPostIndex is None:
        previousPost = 0
        nextPost = 0
    elif previousPostIndex is not None and nextPostIndex is None:
        previousPost = blogs[previousPostIndex]
        nextPost = 0
    elif previousPostIndex is None and nextPostIndex is not None:
        previousPost = 0
        nextPost = blogs[nextPostIndex]
    else:
        previousPost = blogs[previousPostIndex]
        nextPost = blogs[nextPostIndex]
    # Logic for checking next and previous blogs ends here
    if request.method == 'POST':
        form = forms.CommentCreationForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.blog = str(slug)
            post.save()
            blog.comments += 1
            blog.save()
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        form = forms.CommentCreationForm()
    context = {'comments':comm,'blog':blog, 'popular':popular, 'commentCreationForm':form,
               'nextPost':nextPost, 'previousPost':previousPost, 'recentBlogs':recentBlogs}
    return render(request, 'business/blog-detail.html', context=context)
def likeBlog(request, slug):
    blog = get_object_or_404(models.Blog, slug=str(slug))
    if request.method == 'POST':
        like = request.POST.get('like')
        if like == '1' and request.user.is_authenticated:
            currentLikes = models.BlogLike.objects.filter(blog=str(slug), user=request.user).values()
            if len(currentLikes) == 0:
                likeModel = models.BlogLike()
                likeModel.blog = str(slug)
                likeModel.user = request.user
                likeModel.save()
                blog.likes += 1
                blog.save()
        else:
            return redirect('account:login')
    return redirect(request.META.get('HTTP_REFERER'))

def userSpecialRequestForListing(request):
    popular = [i for i in models.Listing.objects.all() if i.tag in ["very popular", 'popular']]
    success = False
    if request.method == 'POST':
        data = request.POST.get('query')
        model = models.UserRequest()
        try:
            model.lookingFor = data
            model.save()
            success = True
        except:
            success = False
    return render(request, 'business/user-request-addition.html', {'success': success, 'popular': popular})
def addToSubscriptionList(request):
    if request.method == 'POST':
        model = models.NewsLetterSubscription()
        model.email = request.POST.get('email')
        model.save()
    return redirect(request.META.get('HTTP_REFERER'))