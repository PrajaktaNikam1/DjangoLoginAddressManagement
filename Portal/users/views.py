from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import File_Form,Address_Form,Signup,Profile_imgF,Update_usernameF
from .models import User,Address,File,Profile_img
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login
from django.shortcuts import render
from django.db.models import Q
from django.contrib import messages

# Create your views here.
@login_required()
def user_Portal(request):
    form=File_Form
    if request.method=='POST':
        form=File_Form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"Data and File Uploaded sucessfully !!")
            return HttpResponseRedirect('/user/showdata/')
    return render(request,'users/user_portal.html',{'form':form})


# def user_data(request):
#     form=File_Form
#     if request.method=='POST':
#         form=File_Form(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/user/showdata/')
#     return render(request,'users/user_portal.html',{'form':form})

@login_required()
def Display_data(request):
    data2=File.objects.all()
    total_files_uploaded = File.objects.count()
    queryP = Q(file__endswith='.{}'.format('pdf'))
    pdf_files_uploaded = File.objects.filter(queryP).count()
    queryT = Q(file__endswith='.{}'.format('doc')) or Q(file__endswith='.{}'.format('docx'))
    word_files_uploaded = File.objects.filter(queryT).count()
    queryX = Q(file__endswith='.{}'.format('xls')) or Q(file__endswith='.{}'.format('xlsx'))
    excel_files_uploaded = File.objects.filter(queryX).count()
    queryC = Q(file__endswith='.{}'.format('csv'))
    csv_files_uploaded = File.objects.filter(queryC).count()
    # user_files_uploaded = File.objects.values('user').annotate(File=File.file.count('id')).order_by('-file')
    # fdata = {'total_files_uploaded': total_files_uploaded,
             # 'pdf_files_uploaded': pdf_files_uploaded,
             # 'excel_files_uploaded': excel_files_uploaded,
             # 'csv_files_uploaded': csv_files_uploaded,
             # 'user_files_uploaded': user_files_uploaded
             # }

    return render(request,'users/showdata.html',{"data":data2,'total_files_uploaded':total_files_uploaded,
                                                 'excel_files_uploaded': excel_files_uploaded,
                                                 'csv_files_uploaded':csv_files_uploaded,
                                                 'pdf_files_uploaded':pdf_files_uploaded,
                                                 'word_files_uploaded':word_files_uploaded,
                                                 })

@login_required()
def profile(request):
    adata = Address.objects.all()
    return render(request,'users/profile_page.html',{'adata':adata})

@login_required()
def address(request):
    form = Address_Form
    if request.method=='POST':
        form=Address_Form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Address Added Successfully !')
            return HttpResponseRedirect('/user/profile_info/')
    return render(request,'users/address.html',{'form':form})

# def phone(request):
#     form = Phone_Form
#     if request.method == 'POST':
#         form = Phone_Form(request.data)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/')
#     return render(request, 'users/phone.html', {'form': form})
#
# def update_ph(request,id):
#     form = Phone.objects.get(id=id)
#     if request.method=='POST':
#         form= Phone_Form(request.POST,instance=form)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/user/profile_info/')
#     return render(request, 'users/update_ph.html',{'form': form})

@login_required()
def update_addr(request,id):
    form = Address.objects.get(id=id)
    if request.method=='POST':
        form= Address_Form(request.POST,instance=form)
        if form.is_valid():
            form.save()
            messages.success(request, "Address Updated sucessfully !!")
            return HttpResponseRedirect('/user/profile_info/')
    return render(request, 'users/update_addr.html',{'form': form})

def delete_addr(request,id):
    data = Address.objects.get(id=id)
    data.delete()
    messages.success(request,'Address Removed Successfully !')
    return HttpResponseRedirect('/user/profile_info/')


def signupF(request):
    form = Signup
    if request.method == 'POST':
        form = Signup(request.POST)
        if form.is_valid():
            pswd = form.save()
            pswd.set_password(pswd.password)
            pswd.save()
            messages.success(request,'User Created Successfully Please Login To Login Portal !')
            return HttpResponseRedirect('/')
    return render(request, 'users/signup.html', {'form': form})

@login_required()
def update_profile(request,id):
    form=Profile_img.objects.get(id=id)
    if request.method=='POST':
        form=Profile_imgF(request.POST,instance=form)
        if form.is_valid():
            form.save()
            messages.success(request,'Username Updated Successfully !')
            return HttpResponseRedirect('/user/profile_info/')
    return render(request,'users/update_profile.html',{'form':form})

def upload_profile(request):
    form=Profile_imgF
    if request.method=='POST':
        form=Profile_imgF(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Profile Photo Uploaded Successfully !')
            return HttpResponseRedirect('/user/profile_info/')
    return render(request,'users/upload_img.html',{'form':form})

def update_username(request,id):
    form=User.objects.get(id=id)
    if request.method=="POST":
        form=Update_usernameF(request.POST,instance=form)
        if form.is_valid():
            form.save()
            messages.success(request, 'Username Updated Successfully !')
            return HttpResponseRedirect('/user/profile_info/')
    return render(request,'users/update_profile.html',{'form':form})


# def loginPage(request):
#     if request.method=='POST':
#         uname=request.POST.get('username')
#         pswd=request.POST.get('password')
#         user=authenticate(request,username=uname,password=pswd)
#         if user is not None:
#             login(request,user)
#         raise forms.ValidationError("Entered Wrong Username or Password")
#     return render(request,'registration/login.html')

def my_view(request):
    user = request.user
    return render(request, 'base1.html', {'user': user})

# def pr_img(request):
#     # img=get_object_or_404(Profile_img, id=id)
#     img=Profile_img.objects.all()[-1]
#     return render(request, 'base1.html', {'img':img})



