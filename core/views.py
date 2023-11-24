from django.shortcuts import render, redirect
from django.contrib import messages
from .models import UserProfile
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='signin')
def home(request):
    all_users = UserProfile.objects.all()
    return render(request, "index.html", {'all_user': all_users})

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        if password == password:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email already exists")
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, "Please another username")
                return redirect('register')
            
            else:
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password
                )
                user.save()
                
                # login the user and redirect
                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)
                
                # we create a profile for new user
                user_model = User.objects.get(username=username)
                new_user_profile = UserProfile.objects.create(user=user_model, id_user=user_model.id)
                new_user_profile.save()
                return redirect('profile')
        else:
            messages.info(request, "Invalid password")
            return redirect('register')
    else:
        return render(request, "register.html")


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # first we authenticate the user
        user = auth.authenticate(username=username, password=password)
        
        # if user details recognised
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Invalid detials")
            return redirect('signin')
    else:
        return render(request, "signin.html")

@login_required(login_url='signin')
def profile(request):
    # this is used to get all details of the settings file
    user_profile = UserProfile.objects.get(user=request.user)
    
    # to get the whole input of the user
    if request.method == 'POST':
        # here to chck if there is any update but not the image profile
        # these part say if the user did not chaneg the profile picture
        if request.FILES.get('image') == None:
            image = user_profile.profileimg
            fname = request.POST['fname']
            lname = request.POST['lname']
            sname = request.POST['sname']
            bio = request.POST['bio']
            dob = request.POST['dob']
            location = request.POST['location']
            
            user_profile.profileimg = image
            user_profile.fname = fname
            user_profile.sname = sname
            user_profile.lname = lname
            user_profile.bio = bio
            user_profile.dob = dob
            user_profile.location = location
            user_profile.save()
        
        # if there was an update these code will run
        if request.FILES.get('image') != None:
            image = request.FILES.get('image')
            name = request.POST['fname']
            lname = request.POST['lname']
            sname = request.POST['sname']
            dob = request.POST['dob']
            bio = request.POST['bio']
            location = request.POST['location']
            
            user_profile.profileimg = image
            user_profile.fname = fname
            user_profile.lname = lname
            user_profile.sname = sname
            user_profile.bio = bio 
            user_profile.dob = dob
            user_profile.location = location
            user_profile.save()
        return redirect('profile')
    return render(request, "profile.html", {'user_profile': user_profile})

@login_required(login_url='signin')
def logout(request):
    auth.logout(request)
    return redirect('signin')