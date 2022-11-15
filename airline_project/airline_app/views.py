from django.shortcuts import render,redirect
from .  models import *
from django.contrib import messages
# Create your views here.
def base_page(request):
    return render(request,'base.html')

def home_page(request):
    return render(request,'home.html')

def about_page(request):
    return render(request,'about_us.html')

def contact_page(request):
    return render(request,'contact_us.html')

def login(request):
    return render(request,'login_latest.html')

def customer_home_page(request):
    return render(request,'customer_home_page.html')

def admin_home_page(request):
    return render(request,'admin_home_page.html')

def airlines_home_page(request):
    return render(request,'airlines_home_page.html')

def change_password_page(request):
    return render(request,'change_password.html')

def registration_customer_page(request):
    message=""
    if request.method == 'POST':
        FullName = request.POST['Fullname']
        UserName = request.POST['Username']
        EMail = request.POST['Email']
        ConTact = request.POST['Contact']
        PassWord = request.POST['Password']
        Confirm_Password = request.POST['Confirm_password']
        City = request.POST['City']
        Date_of_birth = request.POST['Date']
        Gender = request.POST['Gender']
        Image = request.FILES['Image']
        
        # if PassWord == Confirm_Password:
        #     if Customer.objects.filter(username=UserName).exists():
        #         messages.info("username already exists")
            
        #     elif Customer.objects.filter(email=EMail).exists():
        #         messages.info("Email is already taken")
            
            
        customer_details = Customer(fullname=FullName,username=UserName,email=EMail,contact=ConTact,password=PassWord,city=City,date_of_birth=Date_of_birth,image=Image,gender=Gender)
        customer_details.save()
        if customer_details:
            message = "Data inserted successfully"
        else:
            message = "error"
    
    return render(request,'registration_customer.html',{'error_message':message})

def registration_airlines_page(request):
    return render(request,'registration_airlines.html')

def searchhome_page(request):
    return render(request,'search_flight_home.html')

def searchcustomer_page(request):
    return render(request,'search_flight_customer.html')

def addflight_page(request):
    return render(request,'add_flight.html')

def mybookings_page(request):
    return render(request,'mybookings.html')

def viewbookings_admin_page(request):
    return render(request,'view_bookings_admin.html')


def viewbookings_airlines_page(request):
    return render(request,'view_bookings_airlines.html')

def viewbookings_admin_details_page(request):
    return render(request,'view_bookings_admin_details.html')

def viewbookings_airlines_details_page(request):
    return render(request,'view_bookings_airlines_details.html')

def viewfeedback_page(request):
    return render(request,'view_feedback.html')

def viewusers_page(request):
    return render(request,'view_users.html')

def viewprofile_customer_page(request):
    return render(request,'view_profile_customer.html')

def viewprofile_airlines_page(request):
    return render(request,'view_profile_airlines.html')

def searchresult_home_page(request):
    return render(request,'search_result_home.html')

def searchresult_customer_page(request):
    return render(request,'search_result_customer.html')

def searchresult_detail_home_page(request):
    return render(request,'search_result_detail_home.html')

def searchresult_detail_customer_page(request):
    return render(request,'search_result_detail_customer.html')

def view_flightdetail_admin_page(request):
    return render(request,'view_flight_detail_admin.html')


def view_flight_airlines_page(request):
    return render(request,'view_flight_airlines.html')

def view_airlines_admin_page(request):
    return render(request,'view_airlines_admin.html')

def view_flightdetail_airlines_page(request):
    return render(request,'view_flight_detail_airlines.html')

def edit_flightdetail_airlines_page(request):
    return render(request,'edit_flight_details_airlines.html')

def payment_page(request):
    return render(request,'payment.html')

def add_passenger_page(request):
    return render(request,'add_passenger.html')

def after_booking_page(request):
    return render(request,'after_booking.html')

def view_request_admin_page(request):
    return render(request,'view_request_admin.html')

def image_upload_page(request):
    return render(request,'image_upload.html')