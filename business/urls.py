from django.urls import path
from . import views

app_name = "business"

urlpatterns = [
path('about-us/', views.about, name='about-us'),
    path('contact-details/', views.contact, name='contact'),
    path('listing', views.listing, name='listing'),
    path('listing-details/<str:slug>', views.listingDetails, name='listing-details'),
    path('listing/add-listing/', views.addListing, name='add-listing'),
    path('blog/', views.blog, name='blog'),
    path('blog/add-new-blog/authenticated-user/', views.addBlog, name='add-blog'),
    path('blog-details/<str:slug>', views.blogDetails, name='blog-details'),
    path('blog-details/like-post/<str:slug>', views.likeBlog, name='like-blog'),
    path('elements/', views.privacy, name='privacy'),
    path('categories/', views.category, name='categories'),
    path('listing/user-requesting-data-info/', views.userSpecialRequestForListing, name='user-data-requests'),
    path('listing/blog-category-contents/view/<str:slug>', views.blogCategoryContent, name='blog-category-content'),
    path('listing/blog-query/viewing-results/', views.blogQueryResults, name='blog-query-results'),
    path('listing/adding-user-to-mail-list', views.addToSubscriptionList, name='add-user-to-mailing-list'),
]