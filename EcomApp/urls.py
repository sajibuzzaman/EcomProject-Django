from django.urls import path
from .views import Home, product_single, product_category, About, Contact, SearchView, Faq_details

urlpatterns = [
    path('', Home, name='home'),
    path('about/', About, name='about'),
    path('contact/', Contact, name='contact'),
    path('product/<int:id>/', product_single, name='product_single'),
    path('product/<int:id>/<slug:slug>/', product_category, name='product_category'),
    path('search/', SearchView, name='SearchView'),
    path('faq/', Faq_details, name='Faq_details'),
]