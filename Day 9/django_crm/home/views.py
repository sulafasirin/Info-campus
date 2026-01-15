from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'index.html')

def base(request):
    return render(request,'base.html')

def home(request):
    return render(request,'home.html')

def customers(request):
    customers = [
        {'name': 'Sulafa', 'email': 'sulafa@gmail.com', 'phone_number': '7907708044', 'status': 'Lead'},
        {'name': 'Shahidh', 'email': 'shahidh@gmail.com','phone_number':'7034032592', 'status': 'Customer'},
        {'name': 'Rohan', 'email': 'rohan@gmail.com','phone_number':'8137962377', 'status': 'Client'},
        {'name': 'Nived', 'email': 'nived@gmail.com','phone_number':'9745701272', 'status': 'Lead'},
        {'name': 'Zalzameen', 'email': 'zalzameen@gmail.com','phone_number':'7356296069', 'status': 'Client'},
    ]
    return render(request, 'customer.html', {'customers': customers})
