from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import Setting, ContactMessage, ContactForm, FAQ
from Product.models import Category, Product, Images, Comment
from .forms import SearchForm
from OrderApp.models import ShopCart

# Create your views here.
def Home(request):

    slider_image = Product.objects.all().order_by('id')[:2]
    latest_product = Product.objects.all().order_by('-id')
    products = Product.objects.all()
    current_user = request.user
    cart_products = ShopCart.objects.filter(user_id=current_user.id)
   
    total_amount = 0
    for p in cart_products:
        total_amount+=p.product.new_price*p.quantity
    context={
       
        'slider_image' : slider_image,
        'latest_product' : latest_product,
        'products' : products,
        'cart_products' : cart_products,
        'total_amount' : total_amount,
        
    }
    return render(request, 'home.html', context)


def product_single(request, id):

    single_product = Product.objects.get(id=id)
    images = Images.objects.filter(product_id = id)
    category_product = Product.objects.filter(category = single_product.category)
    current_user = request.user
    cart_products = ShopCart.objects.filter(user_id=current_user.id)
    comment_show = Comment.objects.filter(product_id=id, status='True')
   
    total_amount = 0
    for p in cart_products:
        total_amount+=p.product.new_price*p.quantity

    context={
      
        'single_product' : single_product,
        'images' : images,
        'category_product' : category_product,
     
        'cart_products' : cart_products,
        'total_amount' : total_amount,
        'comment_show': comment_show,
        
    }
    return render(request, 'product-single.html', context)


def product_category(request, id, slug):

    products = Product.objects.filter(category_id = id)
    context={
     
        'products': products,
    }
    return render(request, 'product-category.html', context)

def About(request):
  
    context={
       
    }
    return render(request, 'about.html', context)

def Contact(request):
    form = ContactForm
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            # messages.success(request, 'Profile details updated.')

            return redirect('contact')
    
   
    context={
      
        'form': form,
    }
    return render(request, 'contact.html', context)

def SearchView(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            cat_id = form.cleaned_data['cat_id']
            if cat_id == 0:
                products = Product.objects.filter(title__icontains=query)
            else:
                products = Product.objects.filter(title__icontains = query, category_id=cat_id)

           
    
            context={
                
                'products': products,
            }
           
            return render(request, 'product-category.html', context)

    return HttpResponseRedirect('product_category')


def Faq_details(request):

    faq = FAQ.objects.filter(status=True).order_by('created_at')

    context = {
  
        'faq': faq

    }
    return render(request, 'faq.html', context)