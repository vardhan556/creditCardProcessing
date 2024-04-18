from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate, login
from django.contrib import messages



def home_page(request):
    user_authenticated = request.session.get('user_id') is not None
    return render(request, 'homepage.html', {'user_authenticated': user_authenticated})



def register_user(request):
    if request.method == 'POST':
        user_id = request.POST.get('user-id')
        password = request.POST.get('password')
        email_id=request.POST.get('email')
        phone_number=request.POST.get('phone-number')

         # Check if user_id already exists
        if RegistrationDetails.objects.filter(user_id=user_id).exists():
            message = 'User ID already taken'
            return render(request, 'registerpage.html', {'message': message})
        
        if RegistrationDetails.objects.filter(email_id=email_id).exists():
            message2='email_id exists'
            return render(request,'registerpage.html',{'message2':message2})
        
        if RegistrationDetails.objects.filter(phone_number=phone_number).exists():
            message3='phone number exists'
            return render(request,'registerpage.html',{'message3':message3})
        
        RegistrationDetails.objects.create(user_id=user_id,password=password,email_id=email_id,phone_number=phone_number)
        # Store user_id in session after registration
        request.session['user_id'] = user_id
        return redirect('success_page')
    return render(request, 'registerpage.html')



#user authentication using django user authentication (in built functions)
# def login_user(request):
#     val = ''
#     if request.method == 'POST':
#         user_id = request.POST.get('user-id')
#         password = request.POST.get('password')
#         user = authenticate(request, user_id=user_id, password=password)

#         if user is not None:  # Check if authentication is successful
#             login(request, user)  # Log in the user
#             return redirect('homepage')  # Redirect to homepage after successful login
#         else:
#             val = 'Login failed'

#     return render(request, 'loginpage.html', {'val': val})



# def success_page(request):
#     return render(request, 'homepage.html')


def login_user(request):
    val=''
    if request.method == 'POST':
        user_id = request.POST.get('user-id')
        password = request.POST.get('password')
        obj=RegistrationDetails.objects.filter(user_id=user_id).first()
        if obj is not None:
            # val=obj
            # if(obj.password)
            if obj.password == password:  # Check if password matches
                val = 'Login successful'
                request.session['user_id'] = user_id  # Store user_id in session
                return redirect('success_page')
            else:
                val = 'Login Failed: password incorrect'
        else:
            val='user is not present'
    return render(request,'loginpage.html',{'val':val})    

def success_page(request):
    user_id = request.session.get('user_id')  # Retrieve user_id from session
    return render(request,'homepage.html',{'user_id': user_id})

def login_page(request):
    return render(request,'loginpage.html')


# def home_page(request):
#     user_id=None
#     if request.user.is_authenticated:
#         user_id=request.user.user_id
# def add_account(request):
#     try:
#         if request.method == 'POST':
#             user_id = request.POST.get('user-id')
#             cardholder_name = request.POST.get('holder-name')
#             account_number = request.POST.get('account-number')
#             expiration_date = request.POST.get('expiry-data')
#             cvv = request.POST.get('cvv')
            
#             try:
#                 # Get the RegistrationDetails instance based on the user_id
#                 registration_details = RegistrationDetails.objects.get(user_id=user_id)
#             except RegistrationDetails.DoesNotExist:
#                 return render(request, "addaccount.html",{"value":"User_id does not exists"})
            
#             # Create CreditCard instance
#             CreditCard.objects.create(user_id=registration_details,
#                                     cardholder_name=cardholder_name,
#                                     account_number=account_number,
#                                     expiration_date=expiration_date,
#                                     cvv=cvv)
            
#             return redirect('success_page')
#     except Exception as e:
#         return render(request,'addaccount.html',{'value':e})
#     return render(request,'addaccount.html')



def add_account(request):
    try:
        if request.method == 'POST':
            user_id = request.POST.get('user-id')
            cardholder_name = request.POST.get('holder-name')
            account_number = request.POST.get('account-number')
            expiration_date = request.POST.get('expiry-data')
            cvv = request.POST.get('cvv')
            
            try:
                # Get the RegistrationDetails instance based on the user_id
                registration_details = RegistrationDetails.objects.get(user_id=user_id)
            except RegistrationDetails.DoesNotExist:
                return render(request, "addaccount.html",{"value":"User_id does not exists"})
            
            # Create CreditCard instance
            CreditCard.objects.create(user_id=registration_details,
                                    cardholder_name=cardholder_name,
                                    account_number=account_number,
                                    expiration_date=expiration_date,
                                    cvv=cvv)
            
            return redirect('success_page')
    except Exception as e:
        return render(request,'addaccount.html',{'value':e})
    return render(request,'addaccount.html')






# def buy_product(request):
#     try:
#         if request.method == 'POST':
#             user_id = request.POST.get('user-id')
#             product_name=request.POST.get('product-name')
#             product_id=request.POST.get('product-id')
#             price=request.POST.get('price')

#             try:
#                 registration_details2=RegistrationDetails.objects.get(user_id=user_id)
#             except RegistrationDetails.DoesNotExist:
#                 return render(request,"addproduct.html")
            
#             Product.objects.create(user_id=registration_details2,
#                                    product_name=product_name,
#                                    product_id=product_id,
#                                    price=price)
            
#             return redirect('success_page')
#     except Exception as f:
#         return render(request,'addproduct.html',{'value':f})
#     return render(request,'addproduct.html')





def buy_product(request):
    if request.method == 'POST':
        # Get form data
        user_id = request.POST.get('user-id')
        product_name = request.POST.get('product-name')
        product_id = request.POST.get('product-id')
        price = request.POST.get('price')

        # Validate form data
        if not all([user_id, product_name, product_id, price]):
            return render(request, "addproduct.html", {'error_message': 'All fields are required'})

        try:
            # Check if user exists
            registration_details = RegistrationDetails.objects.get(user_id=user_id)
        except RegistrationDetails.DoesNotExist:
            return render(request, "addproduct.html", {'error_message': 'User not found'})

        # Create product for the user
        Product.objects.create(user_id=registration_details,
                               product_name=product_name,
                               product_id=product_id,
                               price=price)

        # Redirect to select account page
        return redirect('transaction') #select_account

    return render(request, 'addproduct.html')






# def select_account(request):
#     if request.method == 'POST':
#         account_number = request.POST.get('account_number')
#         # You can perform any necessary validation here
#         # For example, check if the account number is valid
        
#         # Once validated, you can redirect to the transaction page
#         return redirect('transaction', account_number=account_number)
#     else:
#         user_id = request.session.get('user_id')
#         try:
#             user_accounts = CreditCard.objects.filter(user_id=user_id)
#             return render(request, 'selectaccount.html', {'user_accounts': user_accounts})
#         except CreditCard.DoesNotExist:
#             error_message = "No accounts found for this user."
#             return render(request, 'selectaccount.html', {'error_message': error_message})




def transaction(request):
    if request.method == 'POST':
        user_id = request.POST.get('user-id')
        holder_name = request.POST.get('holder_name')
        account_number = request.POST.get('account_number')
        expiry_data = request.POST.get('expiry_data')
        cvv = request.POST.get('cvv')
        msg=''
        print(user_id, holder_name, account_number,expiry_data , cvv,"is the name")
        try:
            person = CreditCard.objects.get(account_number = account_number)
        except CreditCard.DoesNotExist:
            msg = "Account number does not exist"
            return render(request,'transaction.html',{'error_message' : msg})
        
        print(person.cvv,person.account_number,person.cardholder_name,person.expiration_date)
        if expiry_data != person.expiration_date:
            msg='expiration date is not correct'
            return render(request,'transaction.html', {'error_message': msg})
        # if user_id != person.user_id:
        #     msg='usernAME is not correct'
        #     return render(request,'transaction.html', {'error_message': msg})

        if cvv != person.cvv:
            msg='cvv is not correct'
            return render(request,'transaction.html', {'error_message': msg})
        if account_number != person.account_number:
            msg='expiration date is not correct'
            return render(request,'transaction.html', {'error_message': msg})
        if expiry_data != person.expiration_date:
            msg='expiration date is not correct'
            return render(request,'transaction.html', {'error_message': msg})
        if holder_name != person.cardholder_name:
            msg='holder name is not correct'
            return render(request,'transaction.html', {'error_message': msg})
        if holder_name != person.cardholder_name and  expiry_data != person.expiration_date and  cvv != person.cvv :
            msg='details not correct'
            return render(request,'transaction.html')
        else:
            
            return render(request,'homepage.html')
   
        return render(request, 'homepage.html')
    return render(request, 'transaction.html')
