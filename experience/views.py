from django.shortcuts import render, redirect
from .models import Experience
from django.contrib import messages
from user_authentications.models import User

def experience_list(request):
    experience = Experience.objects.filter(user_id=request.user)
    context = {
        'experiences': experience
    }
    return render(request, 'User/Experience/experience_list.html', context=context)


def admin_experience_list(request):
    experience = Experience.objects.all()
    context = {
        'experiences': experience
    }
    return render(request, 'Admin/Experience/experience_list.html', context=context)


def experience_create(request):
    if request.method == 'POST':
        print('request post = ', request.POST)
        title = request.POST['title']
        company = request.POST['company']
        location = request.POST['location']
        description = request.POST['description']
        fromDate = request.POST['fromDate']
        toDate = request.POST['toDate']
        if 'i_currently_work_here' in request.POST:
            i_currently_work_here = request.POST['i_currently_work_here']
            print('i_currently_work_here =  ', i_currently_work_here)
            i_currently_work_here = True
        else:
            i_currently_work_here = False
        if title == '':
            messages.error(request, 'Title Required')
            return redirect('experience_list')
        if fromDate == '':
            messages.error(request, 'From Date Required')
            return redirect('experience_list')
        if toDate == '':
            toDate = None
        experience = Experience()
        experience.user_id = User.objects.get(id=request.user.id)
        experience.title = title
        experience.company = company
        experience.location = location
        experience.fromDate = fromDate
        experience.description = description
        if i_currently_work_here:
            experience.i_currently_work_here = i_currently_work_here
            experience.toDate = None
        else:
            experience.i_currently_work_here = i_currently_work_here
            experience.toDate = toDate
        experience.save()
        messages.success(request, 'Experience Created Successfully')
        return redirect('experience_list')


def experience_update(request, experience_id):
    if request.method == 'POST':
        print('request data = ', request.POST)
        experience = Experience.objects.get(id=experience_id)
        title = request.POST['title']
        company = request.POST['company']
        location = request.POST['location']
        description = request.POST['description']
        fromDate = request.POST['fromDate']
        toDate = request.POST['toDate']
        if 'i_currently_work_here' in request.POST:
            i_currently_work_here = request.POST['i_currently_work_here']
            print('i_currently_work_here =  ', i_currently_work_here)
            i_currently_work_here = True
        else:
            i_currently_work_here = False
        if title == '':
            messages.error(request, 'Title Required')
            return redirect('experience_list')
        if fromDate == '':
            messages.error(request, 'From Date Required')
            return redirect('experience_list')
        if toDate == '':
            toDate = None
        experience.title = title
        experience.company = company
        experience.location = location
        experience.fromDate = fromDate
        experience.description = description
        if i_currently_work_here:
            experience.i_currently_work_here = i_currently_work_here
            experience.toDate = None
        else:
            experience.i_currently_work_here = i_currently_work_here
            experience.toDate = toDate
        experience.save()
        messages.success(request, 'Experience Update Successfully')
        return redirect('experience_list')


def experience_delete(request, experience_id):
    if request.method == 'POST':
        experience = Experience.objects.get(id=experience_id)
        experience.delete()
        messages.success(request, 'Experience Deleted Successfully')
        return redirect('experience_list')
