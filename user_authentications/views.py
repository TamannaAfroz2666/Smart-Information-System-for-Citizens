from django.shortcuts import render, redirect, reverse
from user_authentications.models import User
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate, logout
from birth_day_certificate.models import BirthDayCertificate
from passport.models import Passport
from nid_information.models import NIDInformation
from education.models import Education
from skills.models import Skills
from experience.models import Experience
from .models import User


# Create your views here.

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = User.objects.filter(email=email)
        print('user = ', user)
        if len(user) != 0:
            username = user[0].username
            user_authentication = authenticate(request, username=username, password=password)
            if user_authentication is not None:
                auth_login(request, user_authentication)
                if user_authentication.is_superuser:
                    pass
                    return redirect(reverse('admin_home'))
                elif user_authentication.is_user:
                    return redirect(reverse('user_home'))
                else:
                    return redirect(reverse(''))
            else:
                message = "Your email And Password Is Wrong"
                context = {
                    'message': message,
                }
                return render(request, 'login.html', context=context)
        else:
            message = "Your email And Password Is Wrong"
            context = {
                'message': message,
            }
            return render(request, 'login.html', context=context)
    return render(request, 'login.html')


def registration(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if username == '':
            message = 'username required'
            return render(request, 'registration.html', context={'message': message})
        if email == '':
            message = 'email required'
            return render(request, 'registration.html', context={'message': message})
        if password != confirm_password:
            message = 'password not match'
            return render(request, 'registration.html', context={'message': message})

        check_username = User.objects.filter(username=username)
        if len(check_username) != 0:
            message = 'username already exists. please use another'
            return render(request, 'registration.html', context={'message': message})
        check_email = User.objects.filter(email=email)
        if len(check_email) != 0:
            message = 'email already exists. please use another'
            return render(request, 'registration.html', context={'message': message})
        check_phone = User.objects.filter(phone_number=phone_number)
        if len(check_phone) != 0:
            message = 'phone number already exists. please use another'
            return render(request, 'registration.html', context={'message': message})
        user = User()
        user.username = username
        user.email = email
        user.phone_number = phone_number
        user.is_user = True
        user.save()

        user.set_password(password)
        user.save()
        return redirect('login')

    return render(request, 'registration.html')


def dataTableView(request):
    return render(request, 'datatable.html')


def admin_home(request):
    total_birth_certificate = BirthDayCertificate.objects.count()
    total_nid = NIDInformation.objects.count()
    total_passport = Passport.objects.count()
    total_education = Education.objects.count()
    total_skills = Skills.objects.count()
    total_experience = Experience.objects.count()
    context = {
        'total_birth_certificate': total_birth_certificate,
        'total_nid': total_nid,
        'total_passport': total_passport,
        'total_education': total_education,
        'total_skills': total_skills,
        'total_experience': total_experience
    }
    return render(request, 'Admin/home.html', context)


def user_home(request):
    total_birth_certificate = BirthDayCertificate.objects.count()
    total_nid = NIDInformation.objects.count()
    total_passport = Passport.objects.count()
    total_education = Education.objects.count()
    total_skills = Skills.objects.count()
    total_experience = Experience.objects.count()
    context = {
        'total_birth_certificate': total_birth_certificate,
        'total_nid': total_nid,
        'total_passport': total_passport,
        'total_education': total_education,
        'total_skills': total_skills,
        'total_experience': total_experience
    }
    return render(request, 'home.html', context)


def search_nid(request):
    nid_number = request.POST['nid_number']
    print('nid number = ', nid_number)
    nid = NIDInformation.objects.filter(nid_no=str(nid_number))
    print('nid = ', nid)
    if len(nid) >= 1:
        nid_count = nid.count()
        nid = nid[0]
        nid_user_id = nid.user_id.id
        birth_day_certificate = BirthDayCertificate.objects.filter(user_id=nid_user_id)
        print('birth_day_certificate = ', birth_day_certificate)
        passport = Passport.objects.filter(user_id=nid_user_id)
        education = Education.objects.filter(user_id=nid_user_id)
        skill = Skills.objects.filter(user_id=nid_user_id)
        experience = Experience.objects.filter(user_id=nid_user_id)
        user_info = User.objects.filter(id=nid_user_id)

        context = {
            'birth_day_certificate_count': birth_day_certificate.count(),
            'birth_day_certificate': birth_day_certificate.last(),
            'passport_info': passport.last(),
            'passport_info_count': passport.count(),
            'nid_information': nid,
            'nid_information_count': nid_count,
            'education': education,
            'education_count': education.count(),
            'skill': skill,
            'skill_count': skill.count(),
            'experience': experience,
            'experience_count': experience.count(),
            'user_info': user_info,
            'count': 1
        }
        return render(request, 'User/search_result.html', context)
    else:
        context = {
            'count': 0
        }
        return render(request, 'User/search_result.html', context=context)


def user_logout(request):
    logout(request)
    return redirect('login')


def profile(request):
    return render(request, 'profile.html')


def update_profile(request):
    print('request data = ', request.POST)
    print('files = ', request.FILES)
    user = User.objects.get(id=request.user.id)
    email = request.POST['email']
    phone_number = request.POST['phone_number']
    address = request.POST['address']
    if 'image' in request.FILES:
        image = request.FILES['image']
    else:
        image = request.user.image
    user.email = email
    user.phone_number = phone_number
    user.address = address
    user.image = image
    user.save()
    return redirect('profile')


def user_password_change(request):
    if request.method == 'POST':
        user = request.user
        old_password = request.POST['old_password']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']
        check_user = User.objects.filter(id=user.id).first()
        if not check_user.check_password(old_password):  # check user's old password from db model
            message = 'wrong old password'
            return render(request, 'password_change.html', context={'message': message})
        if new_password != confirm_password:
            message = 'new password and confirm password not match'
            return render(request, 'password_change.html', context={'message': message})
        check_user.set_password(new_password)
        check_user.save()
        return redirect('login')
    else:
        return render(request, 'password_change.html')

