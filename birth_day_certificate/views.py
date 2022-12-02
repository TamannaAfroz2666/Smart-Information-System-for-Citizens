from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages
from user_authentications.models import User
# Create your views here.


def admin_birthday_certificate_list(request):
    birth_day_certificate = BirthDayCertificate.objects.all()
    print('birth_day_certificate = ', birth_day_certificate)
    context = {
        'all_birth_day_certificate': birth_day_certificate,
        'count': birth_day_certificate.count()
    }
    return render(request, 'Admin/birth_day_certificate/birth_day_certificate_list.html', context=context)


def birth_day_certificate_verified(request, birth_day_certificate_id):
    if request.method == 'POST':
        birth_day_certificate = BirthDayCertificate.objects.get(id=birth_day_certificate_id)
        birth_day_certificate.is_verified = True
        birth_day_certificate.save()
        messages.success(request, 'Birthday Certificate Verified Successfully')
        return redirect('admin_birth_day_certificate_list')


def birthday_certificate_list(request):
    birth_day_certificate = BirthDayCertificate.objects.filter(user_id=request.user)
    print('birth_day_certificate = ', birth_day_certificate)
    context = {
        'birth_day_certificate': birth_day_certificate.last(),
        'count': birth_day_certificate.count()
    }
    return render(request, 'User/birth_day_certificate/birth_day_certificate_list.html', context=context)


def birthday_certificate_search(request):
    birth_day_certificate = BirthDayCertificate.objects.filter(user_id=request.user)
    print('birth_day_certificate = ', birth_day_certificate)
    context = {
        'birth_day_certificate': birth_day_certificate.last(),
        'count': birth_day_certificate.count()
    }
    return render(request, 'User/birth_day_certificate/birth_day_certificate_search.html', context=context)


def birthday_certificate_search_result(request):
    if request.method == 'POST':
        birth_registration_number = request.POST['birth_registration_number']
        birth_day_certificate = BirthDayCertificate.objects.filter(
            birth_registration_number=birth_registration_number
        )
        context = {
            'birth_day_certificate': birth_day_certificate.last(),
            'count': birth_day_certificate.count()
        }
        return render(request, 'User/birth_day_certificate/birth_day_certificate_search_result.html', context=context)


def birthday_certificate_create(request):
    if request.method == 'POST' or request.FILES:
        print('data = ', request.POST)
        print('data = ', request.FILES)
        user_id = User.objects.get(id=request.user.id)
        date_of_registration = request.POST['date_of_registration']
        date_of_issue_certificate = request.POST['date_of_issue_certificate']
        birth_registration_number = request.POST['birth_registration_number']
        name = request.POST['name']
        gender = request.POST['gender']
        birth_date = request.POST['birth_date']
        birth_place = request.POST['birth_place']
        father_name = request.POST['father_name']
        mother_name = request.POST['mother_name']
        father_nationality = request.POST['father_nationality']
        mother_nationality = request.POST['mother_nationality']
        present_address = request.POST['present_address']
        if 'image' in request.FILES:
            image = request.FILES['image']
        else:
            image = ''
        b = BirthDayCertificate()
        b.user_id = user_id
        b.date_of_registration = date_of_registration
        b.date_of_issue_certificate = date_of_issue_certificate
        b.birth_registration_number = birth_registration_number
        b.name = name
        b.gender = gender
        b.birth_date = birth_date
        b.birth_place = birth_place
        b.father_name = father_name
        b.mother_name = mother_name
        b.father_nationality = father_nationality
        b.mother_nationality = mother_nationality
        b.present_address = present_address
        b.image = image
        b.save()
        messages.success(request, 'Birth Certificate Created Successfully')
        return redirect('birth_day_certificate_list')
    return render(request, 'User/birth_day_certificate/birth_day_certificate_create.html')


def birth_day_certificate_update(request, birth_day_certificate_id):
    if request.method == 'GET':
        birth_day_certificate = BirthDayCertificate.objects.get(id=birth_day_certificate_id)
        print('birth_day_certificate = ', birth_day_certificate)
        context = {
            'birth_day_certificate': birth_day_certificate
        }
        return render(request, 'User/birth_day_certificate/birth_day_certificate_update.html', context=context)
    if request.method == 'POST' or request.FILES:
        print('data = ', request.POST)
        print('data = ', request.FILES)
        birth_day_certificate = BirthDayCertificate.objects.get(id=birth_day_certificate_id)
        date_of_registration = request.POST['date_of_registration']
        date_of_issue_certificate = request.POST['date_of_issue_certificate']
        birth_registration_number = request.POST['birth_registration_number']
        name = request.POST['name']
        gender = request.POST['gender']
        birth_date = request.POST['birth_date']
        birth_place = request.POST['birth_place']
        father_name = request.POST['father_name']
        mother_name = request.POST['mother_name']
        father_nationality = request.POST['father_nationality']
        mother_nationality = request.POST['mother_nationality']
        present_address = request.POST['present_address']
        if 'image' in request.FILES:
            image = request.FILES['image']
        else:
            image = birth_day_certificate.image
        b = birth_day_certificate
        b.date_of_registration = date_of_registration
        b.date_of_issue_certificate = date_of_issue_certificate
        b.birth_registration_number = birth_registration_number
        b.name = name
        b.gender = gender
        b.birth_date = birth_date
        b.birth_place = birth_place
        b.father_name = father_name
        b.mother_name = mother_name
        b.father_nationality = father_nationality
        b.mother_nationality = mother_nationality
        b.present_address = present_address
        b.image = image
        b.save()
        messages.success(request, 'Birth Certificate Update Successfully')
        return redirect('birth_day_certificate_list')


def birth_day_certificate_delete(request, birth_day_certificate_id):
    birth_day_certificate = BirthDayCertificate.objects.get(id=birth_day_certificate_id)
    if request.method == 'POST':
        birth_day_certificate.delete()
        messages.success(request, 'Education Deleted Successfully')
        return redirect('birth_day_certificate_list')

