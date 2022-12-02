from django.shortcuts import render, redirect
from .models import NIDInformation
from django.contrib import messages
# Create your views here.
from user_authentications.models import User


def admin_nid_list(request):
    queryset = NIDInformation.objects.all()
    context = {
        'all_nid_information': queryset,
        'count': queryset.count()
    }
    return render(request, 'Admin/NID/nid_list.html', context=context)


def nid_list(request):
    queryset = NIDInformation.objects.filter(user_id=request.user)
    context = {
        'nid_information': queryset.last(),
        'count': queryset.count()
    }
    return render(request, 'User/NID/nid_list.html', context=context)


def nid_list_search(request):
    queryset = NIDInformation.objects.filter(user_id=request.user)
    context = {
        'nid_information': queryset.last(),
        'count': queryset.count()
    }
    return render(request, 'User/NID/nid_search.html', context=context)


def nid_list_search_result(request):
    if request.method == 'POST':
        nid_no = request.POST['nid_no']
        professions = request.POST['professions']
        if professions != '' and nid_no == '':
            queryset = NIDInformation.objects.filter(professions=professions)
            context = {
                'all_nid_information': queryset,
                'count': queryset.count()
            }
            return render(request, 'User/NID/nid_search_result_list.html', context=context)
        else:
            queryset = NIDInformation.objects.filter(nid_no=nid_no)
            context = {
                'nid_information': queryset.last(),
                'count': queryset.count()
            }
            return render(request, 'User/NID/nid_search_result.html', context=context)


def nid_create(request):
    if request.method == 'POST' or request.FILES:
        user_id = User.objects.get(id=request.user.id)
        professions = request.POST['professions']
        # name_bangla = request.POST['name_bangla']
        name_english = request.POST['name_english']
        father_name = request.POST['father_name']
        mother_name = request.POST['mother_name']
        date_of_birth = request.POST['date_of_birth']
        nid_no = request.POST['nid_no']
        if 'back_image' in request.FILES:
            back_image = request.FILES['back_image']
        else:
            back_image = ''
        if 'front_image' in request.FILES:
            front_image = request.FILES['front_image']
        else:
            front_image = ''
        n = NIDInformation()
        n.user_id = user_id
        n.professions = professions
        # n.name_bangla = name_bangla
        n.name_english = name_english
        n.father_name = father_name
        n.mother_name = mother_name
        n.date_of_birth = date_of_birth
        n.nid_no = nid_no
        n.back_image = back_image
        n.front_image = front_image
        n.save()
        messages.success(request, 'NID Created Successfully')
        return redirect('nid_list')


def nid_update(request, nid_id):
    if request.method == 'POST' or request.FILES:
        print(request.POST)
        print(request.FILES)
        queryset = NIDInformation.objects.get(id=nid_id)
        print(queryset)
        professions = request.POST['professions']
        # name_bangla = request.POST['name_bangla']
        name_english = request.POST['name_english']
        father_name = request.POST['father_name']
        mother_name = request.POST['mother_name']
        date_of_birth = request.POST['date_of_birth']
        nid_no = request.POST['nid_no']
        if 'back_image' in request.FILES:
            back_image = request.FILES['back_image']
        else:
            back_image = queryset.back_image
        if 'front_image' in request.FILES:
            front_image = request.FILES['front_image']
        else:
            front_image = queryset.front_image
        n = queryset
        # n.name_bangla = name_bangla
        n.professions = professions
        n.name_english = name_english
        n.father_name = father_name
        n.mother_name = mother_name
        n.date_of_birth = date_of_birth
        n.nid_no = nid_no
        n.back_image = back_image
        n.front_image = front_image
        n.save()
        messages.success(request, 'NID Update Successfully')
        return redirect('nid_list')


def nid_delete(request, nid_id):
    if request.method == 'POST':
        queryset = NIDInformation.objects.get(id=nid_id)
        queryset.delete()
        messages.warning(request, 'NID Delete Successfully')
        return redirect('nid_list')


def admin_nid_verified(request, nid_id):
    if request.method == 'POST':
        queryset = NIDInformation.objects.get(id=nid_id)
        queryset.is_verified = True
        queryset.save()
        messages.warning(request, 'NID Verified Successfully')
        return redirect('admin_nid_list')
