# from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate, login, logout
# from django.contrib import messages
# from . models import Transactions

# # Create your views here.
# def index(request):
#     return render(request, 'index.html')

# def user_login(request):
#     if request.method == "POST":
#         username = request.POST(username)
#         password = request.POST(password)
#         user = authenticate(request, username = username, password= password)
        
#         if user is not None:
#             login(request, user)
#             messages.success(request, 'login sucessfull')
#             return redirect(request, 'index')
#         else:
#             messages.error(request, 'invalid username or password')
#     return render(request, 'login.html')

# def register(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         confirm_password = request.POST.get('confirm_password')
        
#         if password == confirm_password:
#             if User.objects.filter(username = username).exists():
#                 messages.error(request, "username taken")
#             elif User.objects.filter(email = email).exists():
#                 messages.error(request, 'email exists') 
#             else:
#                 user = User.objects.createuser(username = username, email = email, password = password)
#             user.save()
#             messages.sucess(request, 'Account created sucessfully, please login')
#             return redirect('login')     
#         else:
#             messages.error(request, 'passwords doesnot match')
#     return render(request, 'register.html')

# def user_logout(request):
#     logout(request)
#     messages.sucess(request, 'sucessfully logedout')
#     return redirect('login')
    

# def transactions(request):
#     if request.method == "POST":
#         print("POST DATA:", request.POST)
#         transaction_type = request.POST.get("type")
#         source_input = request.POST.get("source")
#         paid_to_input = request.POST.get("paid_to")
#         category_input = request.POST.get("category")
#         payment_mode = request.POST.get("mode_of_payment")
#         amount = request.POST.get("amount")
#         currency = request.POST.get("currency")
#         description = request.POST.get("description")
#         date = request.POST.get("date")

#         if transaction_type == "income":
#             Transactions.objects.create(
#             type = transaction_type,
#             source = source_input,
#             paid_to = None,
#             category = category_input,
#             mode_of_payment = payment_mode,
#             amount = amount,
#             currency = currency,
#             description = description,
#             date = date
#             )
#         else:
#             Transactions.objects.create(
#             type = transaction_type,
#             source = None,
#             paid_to = paid_to_input,
#             category = category_input,
#             mode_of_payment = payment_mode,
#             amount = amount,
#             currency = currency,
#             description = description,
#             date = date 
#             )

#         return redirect('transactions')
    
#     trans_actions_data = Transactions.objects.all().order_by('-date')
#     return render(request, 'transactions.html', {'transactions': trans_actions_data})

# def loans(request):
#     return render(request, 'loans.html')  



from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . models import Transactions, Loan
# from django.db.models import Q

# Create your views here.
def index(request):
    return render(request, 'index.html')

def user_login(request):
    if request.method == "POST":
        username = request.POST(username)
        password = request.POST(password)
        user = authenticate(request, username = username, password= password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'login sucessfull')
            return redirect(request, 'index')
        else:
            messages.error(request, 'invalid username or password')
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        if password == confirm_password:
            if User.objects.filter(username = username).exists():
                messages.error(request, "username taken")
            elif User.objects.filter(email = email).exists():
                messages.error(request, 'email exists') 
            else:
                 User.objects.create_user(username = username, email = email, password = password)
                 User.save()
            messages.success(request, 'Account created sucessfully, please login')
            return redirect('login')     
        else:
            messages.error(request, 'passwords doesnot match')
    return render(request, 'register.html')

def user_logout(request):
    logout(request)
    messages.success(request, 'sucessfully logedout')
    return redirect('login')
    

def transactions(request):
    if request.method == "POST":
        # print("POST DATA:", request.POST)
        transaction_type = request.POST.get("type")
        source_input = request.POST.get("source")
        paid_to_input = request.POST.get("paid_to")
        category_input = request.POST.get("category")
        payment_mode = request.POST.get("mode_of_payment")
        amount = request.POST.get("amount")
        currency = request.POST.get("currency")
        description = request.POST.get("description")
        date = request.POST.get("date")
        in_voice = request.FILES.get("invoice")

        if transaction_type == "income":
            Transactions.objects.create(
            type = transaction_type,
            source = source_input,
            paid_to = None,
            category = category_input,
            mode_of_payment = payment_mode,
            amount = amount,
            currency = currency,
            description = description,
            date = date,
            invoice = in_voice
            )
        else:
            Transactions.objects.create(
            type = transaction_type,
            source = None,
            paid_to = paid_to_input,
            category = category_input,
            mode_of_payment = payment_mode,
            amount = amount,
            currency = currency,
            description = description,
            date = date,
            invoice = in_voice 
            )

        return redirect('transactions')
    
    trans_actions_data = Transactions.objects.all().order_by('-date')
    return render(request, 'transactions.html', {'transactions': trans_actions_data})

        
def loans(request):
    if request.method == "POSt":
        Loan.objects.create(
            name = request.POST.get("name"),
            lender = request.POST.get("lender"),
            loan_type = request.POST.get("loan_type"),
            start_date = request.POST.get("start_date"),
            tenure = request.POST.get("tenure"),
            intrest_rate = request.POST.get("intrestrate"),
            loan_amount = request.POST.get("loan_amount"),
            emi_amount = request.POST.get("emi_amount"),
            loan_balance = request.POST.get("loan_balance"),
            status = request.POST.get("status")
        )
        
        return redirect('loans')
        
    loans_data = Loan.objects.all().order_by('-emi_amount')
    return render(request, 'loans.html', {'loans':loans_data})