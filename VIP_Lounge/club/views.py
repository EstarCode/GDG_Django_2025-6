from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test

def home(request):
    return render(request, 'club/home.html')


@login_required
def member_lounge(request):
    return render(request, 'club/lounge.html')


def is_manager(user):
    return user.is_authenticated and user.groups.filter(name='Managers').exists()


@user_passes_test(is_manager)
def manager_office(request):
    return render(request, 'club/office.html')
