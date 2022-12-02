from django.shortcuts import render, redirect
from .models import Skills
from django.contrib import messages


def admin_skills_list(request):
    skills = Skills.objects.all()
    print('skills = ', skills)
    context = {
        'skills': skills
    }
    return render(request, 'Admin/Skill/skill_list.html', context=context)


def skills_list(request):
    skills = Skills.objects.filter(user_id=request.user)
    print('skills = ', skills)
    context = {
        'skills': skills
    }
    return render(request, 'User/Skill/skill_list.html', context=context)


def skills_create(request):
    if request.method == 'POST':
        skill_name = request.POST['skill_name']
        skill_level = request.POST['skill_level']
        if skill_name == '':
            print('skill name condition true')
            messages.error(request, 'Skill Name Required')
            return redirect('skill_list')
        if skill_level == '':
            messages.error('skill level required')
            return redirect('skill_list')
        skill_add = Skills()
        skill_add.user_id = request.user
        skill_add.skill_name = skill_name
        skill_add.skill_level = skill_level
        skill_add.save()
        messages.success(request, 'Committee Information Update Successfully')
        return redirect('skill_list')


def skill_update(request, skill_id):
    if request.method == 'POST':
        skill = Skills.objects.get(id=skill_id)
        skill_name = request.POST['skill_name']
        skill_level = request.POST['skill_level']
        print('skill_name = ', skill_name)
        print('skill_level = ', skill_level)
        if skill_name == '':
            print('skill name condition true')
            messages.error(request, 'Skill Name Required')
            return redirect('skill_list')
        if skill_level == '':
            messages.error('skill level required')
            return redirect('skill_list')
        skill.user_id = request.user
        skill.skill_name = skill_name
        skill.skill_level = skill_level
        skill.save()
        messages.success(request, 'Skill Update Successfully')
        return redirect('skill_list')


def skill_delete(request, skill_id):
    if request.method == 'POST':
        skill = Skills.objects.get(id=skill_id)
        skill.delete()
        messages.success(request, 'Skill Deleted Successfully')
        return redirect('skill_list')
