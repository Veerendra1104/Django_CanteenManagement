
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import Register, Customer_login
from .models import Registers, Item

# Create your views here.
def home(request):
    return render(request, "home.html")


def index(request):
    items = Item.objects.all()
    if request.method == 'POST':
        quantity_in_form = int(request.POST.get("quantity"))
        item_in_form  = request.POST.get("item")
        
        database_items = Item.objects.get(itemname = item_in_form)
        if quantity_in_form <= int(database_items.quantity):
            database_items.quantity -=  int(quantity_in_form)
            database_items.save()
            items = Item.objects.all()
            itemcost_in_form = quantity_in_form * int(database_items.itemcost)
            return render(request, "orders.html",{"ordered_item": item_in_form, "ordered_quantity":quantity_in_form, "ordered_cost":itemcost_in_form})

    
    return render(request, "index.html", {"items": items})

def login(request):
    if request.method == 'POST':
        email_entered = request.POST.get("email")
        password = request.POST.get("password")
        # return HttpResponse("<html><body><h1> %s %s</h1> </body></html>" %email_entered %password)
         #get the correct user using mail or id
        user = Registers.objects.get(email = email_entered)
        if password == user.password :
            return redirect("index")
   
    return render(request, "login.html")


def register(request):
    form = Register(request.POST)
    if form.is_valid():
       name = request.POST.get("name")
       password = request.POST.get("password")
       conform_password = request.POST.get("conform_password")
       if password==conform_password :
        
        if Registers.objects.filter(name = name):
            return  HttpResponse("<html><body><h1>Name Already Exists!!!</h1> </body></html>")
            
        else :
            form.save()
            return redirect('login')
       else:
           return HttpResponse("<html><body><h1>Different in password and Conform_Password</h1> </body></html>")

    return render(request, "register.html", {'form' : form})


def item(request):
    return render(request, "itempage.html")