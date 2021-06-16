from django.shortcuts import render,redirect
from .forms import PhotoFrom
from .models import Category, Photo
# Create your views here.

def home(request):
    if request.method == "POST":
        form = PhotoFrom(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    
    form = PhotoFrom() 
    category = request.GET.get('category')
    print(category)
    if category == None:
       pic = Photo.objects.all()
    else:
        pic = Photo.objects.filter(category__name=category)
    
    categories = Category.objects.all()
    photo = Photo.objects.all()
    context = {'form':form,'categories':categories,'photo':photo,'pic':pic}
    return render(request,'home.html',context)

def delete_photo(request,id):
    Photo.objects.get(pk=id).delete()
    return redirect('home')

        
    

   
# name: mitu
# pass: @mitu123
