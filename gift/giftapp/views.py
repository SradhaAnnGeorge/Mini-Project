from datetime import timezone
from django.db import IntegrityError
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.urls import reverse
from .models import Product, Category,Userprofile, Communityprofile, Cart, CartItem,BillingInformation,Certification


def index(request):
    return render(request,'index.html')

def admin_base(request):
    return render(request,'admin/admin_base.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def detail(request):
    return render(request,'detail.html')

def admin_dashboard(request):
    print('got')
    customers = Userprofile.objects.all()
    products = Product.objects.all()
    community = Communityprofile.objects.all()
    print(customers)
    customer_count = customers.count()
    product_count = products.count()
    community_count = community.count()
    commusers = Communityprofile.objects.all()
    context = {'customer_count':customer_count,'commusers':commusers,'product_count':product_count,'community_count':community_count}
    return render(request, 'admin/admin_dashboard.html',context)


def community_dashboard(request):
    user=request.user
    products = Product.objects.all()
    product_count = products.count()
    # existing_certification = Certification.objects.filter(user=user).first()

    # if existing_certification:
    #     return render(request, 'seller/dashseller.html', {'existing_certification': existing_certification,})

    if request.method == 'POST':
        # Handle form submission
        certification_image = request.FILES.get('certification_image')
        owner_name = request.POST.get('owner_name')
    
        # Perform client-side validation here using JavaScript if needed

        # Perform server-side validation if needed
        # if not certification_image or not owner_name or not store_name or not expiry_date_from or not expiry_date_to:
        #     messages.error(request, 'Please fill in all required fields.')
        # else:
            # Create and save the Certification instance
        certification = Certification(
            user=request.user,
            certification_image=certification_image,
            owner_name=owner_name,
        )
        certification.save()


    context = {'product_count':product_count,
               }

    return render(request,'community/community_dashboard.html',context)

def admin_category(request):
    categories = Category.objects.all()  
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
        return redirect('userprofile')
    return render(request, 'edit-profile .html', {'user_profile': user_profile})  

def communityprofile(request):

    community_profile = request.user 

    context = {
        'community_profile': community_profile,
    }

    return render(request, 'community/communityprofile.html', context)

def community_edit_profile(request):
    try:
            community_profile = Communityprofile.objects.get(user=request.user)
    except Communityprofile.DoesNotExist:
        
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
        return redirect('communityprofile') 

    return render(request, 'community_edit-profile .html', {'community_profile': community_profile})  


def community_product(request):
    com = Communityprofile.objects.get(user=request.user)

    product = Product.objects.filter(community=com)
    context = {
        'product': product,
    }
    return render(request, 'community/community_product.html', context)

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
        community = Communityprofile.objects.get(user=request.user)
        product = Product(name=name, description=description, price=price, category=category, image=product_image, community=community)
        product.save()
        # messages.success(request, "Product Succesfully Added")
        return redirect('community_product') 


    categories = Category.objects.all() 
    context = {'categories': categories}
    return render(request, 'community/community_add_products.html', context)

def community_deleteproduct(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        product.delete()
    except Product.DoesNotExist:
        pass
    return redirect('community_product')

def admin_edit_category(request, category_id):

    category = Category.objects.get(id=category_id)
    if request.method == 'POST':
        category.name = request.POST['name']
        category.save()
        return redirect('admin_category') 

    return render(request, 'admin/admin_editcategory.html', {'category': category})


def community_edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    categories = Category.objects.all()

    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        price = request.POST['price']
        category_id = request.POST['category']
        product_image = request.FILES.get('product_image')
        product.name = name
        product.description = description
        product.price = price
        product.category_id = category_id
        product.image = product_image
        product.save()

        return redirect('community_product') 
    context = {
        'product': product,
        'categories': categories,
    }
    return render(request, 'community/community_edit_product.html', context)
    
def admin_delete_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    if request.method == 'POST':
        category.delete()
        return redirect('admin_category')
    return render(request, 'admin/admin_deletecategory.html', {'category': category})

from django.db import IntegrityError
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Category

def admin_add_category(request):
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            if Category.objects.filter(name=name).exists():
                messages.error(request, 'Category with this name already exists.')
            else:
                category = Category(
                    name=name,
                )
                category.save()
                messages.success(request, 'Category created successfully.')
                return redirect('admin_category_list')  

        except IntegrityError as e:
            messages.error(request, 'Error creating category: {}'.format(str(e)))

    return render(request, 'admin/add_category.html')

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def login_page(request):
    if request.method == "POST":
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        
        if user is not None:
            if user.is_superuser:
                login(request, user)
                return redirect('admin_dashboard')
            elif user.is_staff:
                if user.communityprofile.is_approval:
                    login(request, user)
                    return redirect('community_dashboard')
                else:
                    messages.info(request, "Your seller account is not yet approved by admin. Please wait for approval.")
                    return redirect('login_page')
            else:
                login(request, user)
                return redirect('/')
        else:
            messages.info(request, "Invalid Login")
            return redirect('login_page')
    else:
        return render(request, 'login.html')



from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Communityprofile 

def register(request):
    if request.method == "POST":
        name = request.POST['username']
        username = request.POST['email']
        mobile = request.POST['mobile']
        password = request.POST['password']
        confirm_password = request.POST['confirmPassword']
        user_role = request.POST.get('user_role', 'customer')

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password, email=username)
                if user_role == 'staff':
                    user.is_staff = True  # Set the user as staff
                    community_profile = Communityprofile.objects.create(
                        user=user,
                        name=name,
                        email=username, 
                        mobile=mobile,
                        is_approval=False  # Wait for admin approval for staff
                    )
                   
                    messages.success(request, 'Registration successful. Please wait for admin approval.')
                else:
                    user.is_staff = False
                    Userprofile.objects.create(user=user,name=name, email=username, mobile=mobile)

                    messages.success(request, 'Registration successful.')

                user.save()
                
                return redirect('login_page')

        else:
            messages.error(request, 'Password confirmation does not match')
            return redirect('register')
    else:
        return render(request, 'signup.html')

from django.contrib.auth.decorators import login_required 
from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Product, CartItem
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Cart, Product

from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Category, CartItem, Cart
from django.contrib.auth.decorators import login_required

@login_required
def products_list(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category)
    
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity', 1))
        product = get_object_or_404(Product, pk=product_id)
        cart, created = Cart.objects.get_or_create(user=request.user)
        try:
            cart_item = CartItem.objects.get(cart=cart, product=product)
            cart_item.quantity += quantity
            cart_item.save()
        except CartItem.DoesNotExist:
            cart_item = CartItem.objects.create(user=request.user, cart=cart, product=product, quantity=quantity)
        return redirect('cart') 
    
    return render(request, 'product_list.html', {'category': category, 'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'product_detail.html', {'product': product})

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if 'cart' not in request.session:
        request.session['cart'] = {}

    cart = request.session['cart']

    if product_id in cart:
        cart[product_id]['quantity'] += 1
    else:
        cart[product_id] = {
            'name': product.name,
            'price': product.price,
            'quantity': 1,
        }
    request.session.modified = True
    return redirect('cart')  

def cart(request):
    cart_items = CartItem.objects.filter(user=request.user) 
    total_price = sum(item.product.price * item.quantity for item in cart_items)

    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})


from django.shortcuts import render
from .models import CartItem

def cart_view(request):
    user = request.user
    cart_items = CartItem.objects.filter(user=user)
    total_price = sum(item.total_price() for item in cart_items)

    context = {
        'cart_items': cart_items,
        'total_price': total_price,
    }

    return render(request, 'cart.html', context)

from django.shortcuts import render, redirect, get_object_or_404
from .models import Product

def remove_from_cart(request, product_id):
    # print("HELLO")
    product=CartItem.objects.get(product_id=product_id,user_id=request.user.id).delete()

    return redirect('cart')  # Redirect to the cart page or wherever you want to go after removing the item



# def remove_product(request, product_id):
#     product = get_object_or_404(Product, id=product_id)
#     product.delete()
#     return redirect('cart')  

def loggout(request):
        print('Logged Out')
        logout(request)
        return redirect('/')

from django.shortcuts import render
from .models import Communityprofile

def registered_customer_count(request):
    registered_customers_count = Communityprofile.objects.count()
    print(registered_customers_count)
    context = {'registered_customers_count': registered_customers_count}
    return render(request, 'admin/admin_dashboard_cards.html', context)


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, CartItem

@login_required 
def add_to_cart(request, product_id):
    product = Product.objects.get(pk=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    try:
        cart_item = CartItem.objects.get(cart=cart, product=product)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(user=request.user, cart=cart, product=product, quantity=1)

    return redirect('cart')  

from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from .models import Communityprofile,Userprofile

# @login_required
# def admin_dashboard(request):
#     users = Communityprofile.objects.filter(is_approval=False)
#     context = {'users': users}
#     return render(request, 'admin/admin_dashboard.html', context)

from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse
from .models import Communityprofile

def approve_user(request, user_id):
    if request.method == 'POST':
        # Debugging code to check the user_id
        print(f"User ID received: {user_id}")
        
        # Get the Communityprofile instance associated with the user
        community_profile = get_object_or_404(Communityprofile, user_id=user_id)
        
        # Set is_approval to True
        community_profile.is_approval = True
        community_profile.save()

       
        # Get the user ID associated with this Communityprofile
        user_id = community_profile.user.id
        
        # Now you have the user ID
        print("User ID associated with the Communityprofile: {user_id}")
        
        # Redirect to a success page or wherever you want
        return redirect('admin_dashboard')
    else:
        # Handle GET requests or other methods if needed
        return HttpResponse("Method not allowed", status=405)



@login_required
def delete_user(request, user_id):

    if request.method == 'POST':
        # Debugging code to check the user_id
        print(f"User ID received: {user_id}")
        
        # Get the Communityprofile instance associated with the user
        community_profile = get_object_or_404(Communityprofile, user_id=user_id)
        
        # Set is_approval to True
        community_profile.is_approval = False
        community_profile.save()

       
        # Get the user ID associated with this Communityprofile
        user_id = community_profile.user.id
        
        # Now you have the user ID
        print(f"User ID associated with the Communityprofile: {user_id}")
        
        # Redirect to a success page or wherever you want
        return redirect('admin_dashboard')
    else:
        # Handle GET requests or other methods if needed
        return HttpResponse("Method not allowed", status=405)

from django.shortcuts import render
from .models import Product  # Import your Product model or adjust the import as needed

def search_product(request):
    productname = request.GET.get('productname', '')
    
    # Filter products based on the search query
    products = Product.objects.filter(name__icontains=productname)
    
    return render(request, 'product_list.html', {'products': products})


# admin_user_details

# profiles/views.py

# views.py
from django.contrib.auth.models import User
from django.shortcuts import render

def all_users(request):
    users = User.objects.all()
    return render(request, 'admin/customer_details.html', {'users': users})


from django.shortcuts import render, redirect
from .models import BillingInformation, CartItem, Product
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from .models import BillingInformation, CartItem, Product,Payment
from django.contrib.auth.decorators import login_required


from django.shortcuts import render
import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest

razorpay_client = razorpay.Client(
    auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))

# @login_required
# def billing(request):
#     user = request.user
#     cart_items = CartItem.objects.filter(user=user)
#     total_price = sum(item.total_price() for item in cart_items)

#     if request.method == 'POST':
#         address = request.POST.get('address')
#         town = request.POST.get('town')
#         zip_code = request.POST.get('zip')
#         name = request.POST.get('name')

#         # Create or update billing information
#         billing_info, created = BillingInformation.objects.get_or_create(user=user)
#         billing_info.name = name
#         billing_info.address = address
#         billing_info.town = town
#         billing_info.zip_code = zip_code

#         # Ensure the amount field is set with a valid value
#         billing_info.amount = total_price if total_price else 0

#         billing_info.save()

#         # Save the products from the cart to billing_info
#         product_ids = [item.Product.id for item in cart_items]
#         products_to_add = Product.objects.filter(id__in=product_ids)

#         # Replace existing products with the new ones
#         billing_info.product.set(products_to_add)

#         return redirect('payment', billing_id=billing_info.id)  # Redirect to a success page

#     context = {
#         'cart_items': cart_items,
#         'total_price': total_price,
#     }

#     return render(request, 'billing.html', context)

@login_required
def billing(request, user_id):
    user = request.user
    cart_items = CartItem.objects.filter(user=user)
    total_price = sum(item.total_price() for item in cart_items)

    try:
        billing_info = BillingInformation.objects.get(user=user)
    except BillingInformation.DoesNotExist:
        billing_info = None

    if request.method == 'POST':
        address = request.POST.get('address')
        town = request.POST.get('town')
        zip_code = request.POST.get('zip_code')
        name = request.POST.get('name')

        if billing_info:
            billing_info.address = address
            billing_info.town = town
            billing_info.zip_code = zip_code
            billing_info.name = name
            billing_info.amount = total_price
            billing_info.save()
        else:
            billing_info = BillingInformation(
                user=user,
                address=address,
                town=town,
                zip_code=zip_code,
                name=name,
                amount=total_price
            )
            billing_info.save()

        # Save the products from the cart to billing_info
        product_ids = [item.product.id for item in cart_items]
        products_to_add = Product.objects.filter(id__in=product_ids)
        billing_info.product.set(products_to_add)

        return redirect('payment', billing_id=billing_info.id)  # Redirect to a success page

    context = {
        'cart_items': cart_items,
        'total_price': total_price,
        'billing_info': billing_info,
    }

    return render(request, 'billing.html', context)


def payment(request, billing_id):
    billing = BillingInformation.objects.get(pk=billing_id)
    user = request.user

    # For Razorpay integration
    currency = 'INR'
    amount = billing.amount 
    amount_in_paise = int(amount * 100)

    # Create a Razorpay Order
    razorpay_order = razorpay_client.order.create(dict(
        amount=amount_in_paise,
        currency=currency,
        payment_capture='0'  # Capture payment manually after verifying it
    ))

    # Order ID of the newly created order
    razorpay_order_id = razorpay_order['id']
    callback_url = reverse('paymenthandler', args=[billing_id])

    # Create a Payment record
    payment = Payment.objects.create(
        user=request.user,
        razorpay_order_id=razorpay_order_id,
        amount=billing.amount,
        currency=currency,
        payment_status=Payment.PaymentStatusChoices.PENDING,
    )
    payment.billing_info.add(billing)

    # Prepare the context data
    context = {
        'user': request.user,
        'billing': billing,
        'razorpay_order_id': razorpay_order_id,
        'razorpay_merchant_key': settings.RAZOR_KEY_ID,
        'razorpay_amount': amount,
        'currency': currency,
        'amount': billing.amount,
        'callback_url': callback_url,
    }

    return render(request, 'confirm_payment.html', context)

from django.shortcuts import render
from .models import CartItem
@csrf_exempt
def paymenthandler(request, billing_id):
    # Only accept POST requests.
    if request.method == "POST":
        # Get the required parameters from the POST request.
        payment_id = request.POST.get('razorpay_payment_id', '')
        razorpay_order_id = request.POST.get('razorpay_order_id', '')
        signature = request.POST.get('razorpay_signature', '')
        params_dict = {
            'razorpay_order_id': razorpay_order_id,
            'razorpay_payment_id': payment_id,
            'razorpay_signature': signature
        }
        # Verify the payment signature.
        result = razorpay_client.utility.verify_payment_signature(params_dict)
        user = request.user
        
        payment = Payment.objects.get(razorpay_order_id=razorpay_order_id)
        amount = int(payment.amount * 100)  # Convert Decimal to paise
        cart_items=CartItem.objects.filter(user=user)
        # Capture the payment.
        razorpay_client.payment.capture(payment_id, amount)
        payment = Payment.objects.get(razorpay_order_id=razorpay_order_id)

        # Update the order with payment ID and change status to "Successful."
        payment.payment_id = payment_id
        payment.payment_status = Payment.PaymentStatusChoices.SUCCESSFUL
        payment.save()

        cart_items.update(status=0)

        # Mark the cart items as inactive (status = 0)
        billing = BillingInformation.objects.get(id=billing_id)
        billing.status = True
        billing.payment_status=True
        billing.save()

        # Render the success page on successful capture of payment.
        return render(request, 'index.html')

    else:
        
        # If other than POST request is made.
        return HttpResponseBadRequest()

from django.shortcuts import render, get_object_or_404
from .models import BillingInformation

def admin_view_booking(request):
    billing_info_list = BillingInformation.objects.all()
    return render(request, 'admin/admin_view_booking.html', {'billing_info_list': billing_info_list})

def admin_view_booking(request):
    billing_information_list = BillingInformation.objects.all()
    context = {'billing_information_list': billing_information_list}
    return render(request, 'admin/admin_view_booking.html', context)


def block_user(request, user_id):
    user = User.objects.get(pk=user_id)
    if request.method == "POST":
        if user.is_active== True:
           user.is_active= False
        elif user.is_active== False:
           user.is_active= True 
    
        user.is_blocked = not user.is_blocked
        user.save()
    return redirect('customer_details')

from django.shortcuts import render

def profile_view(request):
    # Assuming you have UserProfile related to User using a OneToOneField
    user_profile = request.user.userprofile
    context = {
    'user_profile': request.user.userprofile,
}
    return render(request, 'profile.html', context)

def viewproducts(request):
    # Retrieve all products
    all_products = Product.objects.all()

    context = {
        'all_products': all_products,
    }
    return render(request, 'admin/admin_view_product.html', context)

@login_required
def dashlegal(request):
    # Retrieve Certification objects including their IDs
    seller_applications = Certification.objects.all()
    today = timezone.now().date()

    # Retrieve User roles for each Certification applicant
    user_roles = {}
    for application in seller_applications:
        # Ensure the user associated with the Certification exists
        user = get_object_or_404(User, id=application.user_id)

        # Retrieve user roles
        user_roles[application.id] = {
            'is_admin': user.is_superuser,
            'is_customer': user,
            'is_community': user.is_staff
        }

    context = {
        'seller_applications': seller_applications,
        'user_roles': user_roles,  # Include user roles in the context
        'today': today,
    }
    return render(request, 'admin/dashlegal.html', context)


@login_required

def approve_certification(request, certification_id):
    certification = get_object_or_404(Certification, id=certification_id)
    if request.method == 'POST':
        certification.is_approved = Certification.APPROVED  # Set it to 'approved'
        certification.save()
    return redirect('dashlegal')

