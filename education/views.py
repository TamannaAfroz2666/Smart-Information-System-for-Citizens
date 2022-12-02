from django.shortcuts import render, redirect
from .models import Education
from django.contrib import messages
from user_authentications.models import User


def education_list(request):
    education = Education.objects.filter(user_id=request.user)
    context = {
        'educations': education
    }
    return render(request, 'User/Education/education.html', context=context)


def education_list_search_result(request):
    if request.method == 'POST':
        board = request.POST['board']
        examination = request.POST['examination']
        roll_no = request.POST['roll_no']
        # registration_no = request.POST['registration_no']
        education = Education.objects.filter(
            board=board,
            examination=examination,
            roll_no=roll_no,
            # registration_no=registration_no
        )
        print('education = ', education)
        context = {
            'education': education.last(),
            'count': education.count()
        }
        return render(request, 'User/Education/education_search_result.html', context)


def education_list_search(request):
    context = {}
    return render(request, 'User/Education/education_search.html', context=context)


def admin_education_list(request):
    education = Education.objects.all()
    context = {
        'educations': education
    }
    return render(request, 'Admin/Education/education.html', context=context)


def education_create(request):
    if request.method == "GET":
        return render(request, 'User/Education/education_create.html')

    if request.method == 'POST' or request.FILES:
        print('request post = ', request.POST)
        board = request.POST['board']
        examination = request.POST['examination']
        roll_no = request.POST['roll_no']
        registration_no = request.POST['registration_no']
        institution = request.POST['institution']
        major = request.POST['major']
        degree = request.POST['degree']
        location = request.POST['location']
        description = request.POST['description']
        fromDate = request.POST['fromDate']
        toDate = request.POST['toDate']
        if 'image' in request.FILES:
            image = request.FILES['image']
        else:
            image = ''
        if 'i_currently_attend' in request.POST:
            i_currently_attend = request.POST['i_currently_attend']
            print('i_currently_attend =  ', i_currently_attend)
            i_currently_attend = True
        else:
            i_currently_attend = False
        if institution == '':
            print('skill name condition true')
            messages.error(request, 'Institution Required')
            return redirect('education_list')
        if fromDate == '':
            fromDate = None
        if toDate == '':
            toDate = None
        education = Education()
        education.user_id = User.objects.get(id=request.user.id)
        education.board = board
        education.examination = examination
        education.roll_no = roll_no
        education.registration_no = registration_no
        education.institution = institution
        education.major = major
        education.degree = degree
        education.location = location
        education.fromDate = fromDate
        education.description = description
        education.image = image
        if i_currently_attend:
            education.i_currently_attend = i_currently_attend
            education.toDate = toDate
        else:
            education.i_currently_attend = i_currently_attend
            education.toDate = toDate
        education.save()
        messages.success(request, 'Education Created Successfully')
        return redirect('education_list')


def education_update(request, education_id):
    if request.method == 'GET':
        education = Education.objects.get(id=education_id)
        context = {
            'education': education
        }
        return render(request, 'User/Education/education_update.html', context)

    if request.method == 'POST':
        print('request data = ', request.POST)
        education = Education.objects.get(id=education_id)
        board = request.POST['board']
        examination = request.POST['examination']
        roll_no = request.POST['roll_no']
        registration_no = request.POST['registration_no']
        institution = request.POST['institution']
        major = request.POST['major']
        degree = request.POST['degree']
        location = request.POST['location']
        description = request.POST['description']
        fromDate = request.POST['fromDate']
        toDate = request.POST['toDate']
        if 'image' in request.FILES:
            image = request.FILES['image']
        else:
            image = education.image
        if 'i_currently_attend' in request.POST:
            i_currently_attend = request.POST['i_currently_attend']
            print('i_currently_attend =  ', i_currently_attend)
            i_currently_attend = True
        else:
            i_currently_attend = False
        if institution == '':
            print('skill name condition true')
            messages.error(request, 'Institution Required')
            return redirect('education_list')
        if fromDate == '':
            fromDate = None
        if toDate == '':
            toDate = None
        print(i_currently_attend)
        education.board = board
        education.examination = examination
        education.roll_no = roll_no
        education.registration_no = registration_no
        education.image = image
        education.institution = institution
        education.major = major
        education.degree = degree
        education.location = location
        education.fromDate = fromDate
        education.description = description
        if i_currently_attend:
            education.i_currently_attend = i_currently_attend
            education.toDate = None
        else:
            education.i_currently_attend = i_currently_attend
            education.toDate = toDate
        print('i= ', i_currently_attend)
        print('f= ', fromDate)
        print('t = ', toDate)
        education.save()
        messages.success(request, 'Education Update Successfully')
        return redirect('education_list')


def education_delete(request, education_id):
    if request.method == 'POST':
        education = Education.objects.get(id=education_id)
        education.delete()
        messages.success(request, 'Education Deleted Successfully')
        return redirect('education_list')
