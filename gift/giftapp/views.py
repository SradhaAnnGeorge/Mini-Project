from django.db import IntegrityError
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import Product, Category,Userprofile, Communityprofile




# Create your views here.
def index(request):
    return render(request,'index.html')
# def loginn(request):
#     return render(request,'login.html')

def register(request):
    # if request == POST:
        
    return render(request,'signup.html')
def cart(request):
    return render(request,'cart.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def detail(request):
    return render(request,'detail.html')
# def userprofile(request):
#     return render(request, 'userprofile.html')

def admin_dashboard(request):
     return render(request,'admin/admin_dashboard.html')

def community_dashboard(request):
     return render(request,'community/community_dashboard.html')

def admin_category(request):
    categories = Category.objects.all()  # Fetch all categories from the database
    context = {'categories': categories}
    return render(request, 'admin/admin_category.html', context)

def admin_addcategory(request):
     if request.method == 'POST':
        name = request.POST.get('name')
        category = Category(name=name)
        category.save()
        # messages.success(request, "Category Succesfully Added")
        return redirect('admin_category')
     return render(request, 'admin/admin_addcategory.html')
def admin_product(request):
     products = Product.objects.all()
     context = {
        'products': products,
    }
     return render(request, 'admin/admin_products.html', context)

def userprofile(request):

    user_profile = request.user 

    context = {
        'user_profile': user_profile,
    }

    return render(request, 'userprofile.html', context)

def edit_profile(request):
    try:
            user_profile = Userprofile.objects.get(user=request.user)
    except Userprofile.DoesNotExist:
            # Userprofile doesn't exist, create a new one
            user_profile = Userprofile(user=request.user)
            user_profile.save()

    if request.method == "POST":
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        address = request.POST.get('address')
        if 'profile_pic' in request.FILES:
            profile_pic = request.FILES['profile_pic']
            user_profile.profile_pic = profile_pic


        user_profile.name = name
        user_profile.mobile = mobile
        user_profile.address = address
        request.user.email = email

        user_profile.save()
        request.user.save()

        messages.success(request, 'Profile updated successfully.')
        return redirect('userprofile')  # Redirect to the profile page
    return render(request, 'edit-profile .html', {'user_profile': user_profile})  


def community_product(request):
    # Retrieve the product using get_object_or_404
    product = Product.objects.all()

    # Access the category_id from the product object
      # Assuming 'category' is a ForeignKey field in your Product model

    # You can perform additional logic here, such as fetching related data or calculations

    context = {
        'product': product,
          # Include category_id in the context if needed
    }
    return render(request, 'community/community_product.html', context)

def communityprofile(request):

    community_profile = request.user 

    context = {
        'community_profile': community_profile,
    }

    return render(request, 'communityprofile.html', context)

def community_edit_profile(request):
    try:
            community_profile = Communityprofile.objects.get(user=request.user)
    except Communityprofile.DoesNotExist:
            # Userprofile doesn't exist, create a new one
            community_profile = Communityprofile(user=request.user)
            community_profile.save()

    if request.method == "POST":
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        address = request.POST.get('address')
        if 'profile_pic' in request.FILES:
            profile_pic = request.FILES['profile_pic']
            community_profile.profile_pic = profile_pic


        community_profile.name = name
        community_profile.mobile = mobile
        community_profile.address = address
        request.user.email = email

        community_profile.save()
        request.user.save()

        messages.success(request, 'Profile updated successfully.')
        return redirect('communityprofile')  # Redirect to the profile page

    return render(request, 'community_edit-profile .html', {'community_profile': community_profile})  


def community_product(request):
    # Retrieve the product using get_object_or_404
    product = Product.objects.all()

    # Access the category_id from the product object
      # Assuming 'category' is a ForeignKey field in your Product model

    # You can perform additional logic here, such as fetching related data or calculations

    context = {
        'product': product,
          # Include category_id in the context if needed
    }
    return render(request, 'community/community_product.html', context)


def admin_addproduct(request):
    if request.method == 'POST':
        
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        category_id = request.POST.get('category')
        product_image = request.FILES.get('product_image')


        category = Category.objects.get(id=category_id)
        product = Product(name=name, description=description, price=price, category=category, image=product_image)
        product.save()
        # messages.success(request, "Product Succesfully Added")
        return redirect('admin_product')  # Redirect to a product list page or another view


    categories = Category.objects.all()  # Fetch all categories from the database
    context = {'categories': categories}
    return render(request, 'admin/admin_add_products.html', context)

def community_addproduct(request):
    print('Got')
    if request.method == 'POST':
        print('Got')
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        category_id = request.POST.get('category')
        product_image = request.FILES.get('product_image')


        category = Category.objects.get(id=category_id)
        product = Product(name=name, description=description, price=price, category=category, image=product_image)
        product.save()
        # messages.success(request, "Product Succesfully Added")
        return redirect('community_product')  # Redirect to a product list page or another view


    categories = Category.objects.all()  # Fetch all categories from the database
    context = {'categories': categories}
    return render(request, 'community/community_add_products.html', context)

def community_deleteproduct(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        product.delete()
    except Product.DoesNotExist:
        # Handle the case where the product with the given ID does not exist.
        pass

    # Redirect back to the viewproducts page or wherever you want to go after deletion.
    return redirect('community_product')


# def admin_category_list(request):
#     categories = Category.objects.all()
#     return render(request, 'admin/admin_editcategory.html', {'categories': categories})

def admin_edit_category(request, category_id):

    category = Category.objects.get(id=category_id)
    if request.method == 'POST':
        # Handle the form submission for editing the category here
        category.name = request.POST['name']
        category.save()
        return redirect('admin_category')  # Redirect to category list or success page

    return render(request, 'admin/admin_editcategory.html', {'category': category})


def community_edit_product(request, product_id):
    # Get the product object to edit
    product = get_object_or_404(Product, id=product_id)
    categories = Category.objects.all()

    if request.method == 'POST':
        # Retrieve the data from the form fields
        name = request.POST['name']
        description = request.POST['description']
        price = request.POST['price']
        category_id = request.POST['category']
        product_image = request.FILES['product_image']

        # Update the product object with the new data
        product.name = name
        product.description = description
        product.price = price
        product.category_id = category_id
        product.product_image = product_image

        # Save the updated product
        product.save()

        return redirect('community_product')  # Replace 'product_detail' with the URL name of your product detail view
    context = {
        'product': product,
        'categories': categories,
    }
    return render(request, 'community/community_edit_product.html', context)
    # context = {
    #     'product': product,
    # }
    # return render(request, 'community/community_edit_product.html', context)

    
def admin_delete_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    if request.method == 'POST':
        # Handle the category deletion here
        # Example:
        category.delete()
        return redirect('admin_category')
    return render(request, 'admin/admin_deletecategory.html', {'category': category})

def admin_add_category(request):
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
           

            # Create a new Category instance with the form data
            category = Category(
                name=name,
                
            )
            category.save()

            # Display a success message
            messages.success(request, 'Category created successfully.')
            return redirect('admin_category_list')  # Redirect back to the admin page

        except IntegrityError as e:
            # Handle database integrity error (e.g., unique constraint violation)
            messages.error(request, 'Error creating category: {}'.format(str(e)))

    return render(request, 'admin/add_category.html')

# def admin_add_category(request):
#     if request.method == 'POST':
#         # Handle the form submission for adding a new category here
#         # Example:
#         # name = request.POST['name']
#         # category = Category.objects.create(name=name)
#         return redirect('admin_category_list')
#     return render(request, 'admin/add_category.html')



def login_page(request):
    if request.method == "POST":
        username=request.POST['email']
        password=request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('admin_dashboard')
            elif user.is_staff:
                return redirect('community_dashboard')
            else:
                return redirect('/')
        else:
            messages.info(request, "Invalid Login")
            return redirect('login_page')
    else:
            return render(request, 'login.html') 

def register(request): 
    if request.method == "POST":
        username = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirmPassword']
        if password==confirm_password:
              if User.objects.filter(username=username).exists():
 # messages.info(request, 'Username already exists')
 # return redirect('register')
                 return render(request, 'signup.html', {'username_exists': True})
#     messages.info(request, 'Email already exists') 
#     return redirect('register')
              else:
                    user = User.objects.create_user(username=username, password=password)
                    user.save()
                    messages.success(request, 'Registration successful. You can now log in.')
                    return redirect('login_page')
        else:
            messages.error(request, 'Password confirmation does not match') 
            return redirect('register')
    else:
        return render(request, 'signup.html')
    
from django.shortcuts import render, get_object_or_404
from .models import Category, Product

def products_list(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category)
    return render(request, 'product_list.html', {'category': category, 'products': products})




def loggout(request):
        print('Logged Out')
        logout(request)
        return redirect('/')