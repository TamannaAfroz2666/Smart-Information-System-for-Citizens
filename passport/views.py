from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Passport
from user_authentications.models import User
# Create your views here.


def passport_search_result(request):
    if request.method == 'POST':
        passport_number = request.POST['passport_number']
        passport = Passport.objects.filter(passport_number=passport_number)
        context = {
            'passport_info': passport.last(),
            'count': passport.count(),
        }
        return render(request, 'User/passport/passport_search_result.html', context=context)


def passport_list(request):
    queryset = Passport.objects.filter(user_id=request.user)
    context = {
        'passport_info': queryset.last(),
        'count': queryset.count()
    }
    return render(request, 'User/passport/passport.html', context=context)


def passport_search(request):
    context = {
    }
    return render(request, 'User/passport/passport_search.html', context=context)


def admin_passport_list(request):
    queryset = Passport.objects.all()
    context = {
        'passport_info': queryset,
        'count': queryset.count()
    }
    return render(request, 'Admin/passport/passport.html', context=context)


def passport_create(request):
    if request.method == 'POST' or request.FILES:
        print('request data = ', request.POST)
        print('request files = ', request.FILES)
        user_id = User.objects.get(id=request.user.id)
        name = request.POST['name']
        father_name = request.POST['father_name']
        mother_name = request.POST['mother_name']
        spouses_name = request.POST['spouses_name']
        permanent_address = request.POST['permanent_address']
        e_name = request.POST['e_name']
        e_relationship = request.POST['e_relationship']
        e_address = request.POST['e_address']
        e_phone = request.POST['e_phone']
        type = request.POST['type']
        country_code = request.POST['country_code']
        passport_number = request.POST['passport_number']
        surname = request.POST['surname']
        given_name = request.POST['given_name']
        nationality = request.POST['nationality']
        personal_no = request.POST['personal_no']
        dob = request.POST['dob']
        previous_passport_no = request.POST['previous_passport_no']
        sex = request.POST['sex']
        place_of_birth = request.POST['place_of_birth']
        date_of_issue = request.POST['date_of_issue']
        issuing_authority = request.POST['issuing_authority']
        date_of_expiry = request.POST['date_of_expiry']
        holder_name = request.POST['holder_name']
        if 'image' in request.FILES:
            image = request.FILES['image']
        else:
            image = ''
        # image = request.FILES['image']
        p = Passport()
        p.user_id = user_id
        p.name = name
        p.father_name = father_name
        p.mother_name = mother_name
        p.spouses_name = spouses_name
        p.permanent_address = permanent_address
        p.e_name = e_name
        p.e_relationship = e_relationship
        p.e_address = e_address
        p.e_phone = e_phone
        p.type = type
        p.country_code = country_code
        p.passport_number = passport_number
        p.surname = surname
        p.given_name = given_name
        p.nationality = nationality
        p.personal_no = personal_no
        p.dob = dob
        p.previous_passport_no = previous_passport_no
        p.sex = sex
        p.place_of_birth = place_of_birth
        p.date_of_issue = date_of_issue
        p.issuing_authority = issuing_authority
        p.date_of_expiry = date_of_expiry
        p.holder_name = holder_name
        p.image = image
        p.save()
        messages.success(request, 'Passport Created Successfully')
        return redirect('passport_list')
    return render(request, 'User/passport/passport_create.html')


def passport_update(request, passport_id):
    if request.method == "GET":
        passport = Passport.objects.get(id=passport_id)
        context = {
            'passport': passport
        }
        return render(request, 'User/passport/passport_update.html', context=context)
    if request.method == 'POST' or request.FILES:
        print('request data = ', request.POST)
        print('request files = ', request.FILES)
        passport = Passport.objects.get(id=passport_id)
        name = request.POST['name']
        father_name = request.POST['father_name']
        mother_name = request.POST['mother_name']
        spouses_name = request.POST['spouses_name']
        permanent_address = request.POST['permanent_address']
        e_name = request.POST['e_name']
        e_relationship = request.POST['e_relationship']
        e_address = request.POST['e_address']
        e_phone = request.POST['e_phone']
        type = request.POST['type']
        country_code = request.POST['country_code']
        passport_number = request.POST['passport_number']
        surname = request.POST['surname']
        given_name = request.POST['given_name']
        nationality = request.POST['nationality']
        personal_no = request.POST['personal_no']
        dob = request.POST['dob']
        previous_passport_no = request.POST['previous_passport_no']
        sex = request.POST['sex']
        place_of_birth = request.POST['place_of_birth']
        date_of_issue = request.POST['date_of_issue']
        issuing_authority = request.POST['issuing_authority']
        date_of_expiry = request.POST['date_of_expiry']
        holder_name = request.POST['holder_name']
        if 'image' in request.FILES:
            image = request.FILES['image']
        else:
            image = ''
        # image = request.FILES['image']
        p = passport
        p.name = name
        p.father_name = father_name
        p.mother_name = mother_name
        p.spouses_name = spouses_name
        p.permanent_address = permanent_address
        p.e_name = e_name
        p.e_relationship = e_relationship
        p.e_address = e_address
        p.e_phone = e_phone
        p.type = type
        p.country_code = country_code
        p.passport_number = passport_number
        p.surname = surname
        p.given_name = given_name
        p.nationality = nationality
        p.personal_no = personal_no
        p.dob = dob
        p.previous_passport_no = previous_passport_no
        p.sex = sex
        p.place_of_birth = place_of_birth
        p.date_of_issue = date_of_issue
        p.issuing_authority = issuing_authority
        p.date_of_expiry = date_of_expiry
        p.holder_name = holder_name
        p.image = image
        p.save()
        messages.success(request, 'Passport Update Successfully')
        return redirect('passport_list')


def passport_delete(request, passport_id):
    if request.method == "POST":
        passport = Passport.objects.get(id=passport_id)
        passport.delete()
        messages.success(request, 'Passport Delete Successfully')
        return redirect('passport_list')


def admin_passport_verify(request, passport_id):
    if request.method == "POST":
        passport = Passport.objects.get(id=passport_id)
        passport.is_verify = True
        passport.save()
        messages.success(request, 'Passport Verify Successfully')
        return redirect('admin_passport_list')
