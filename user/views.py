from django.shortcuts import render

from user.models import User

from user.forms import NewUserForm


def add_user(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST, request.FILES)

        if form.is_valid():
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            img = request.FILES.get('img')
            address = request.POST.get('address')

            user = User.objects.create(
                first_name=first_name,
                last_name=last_name,
                img=img,
                address=address
            )

    form = NewUserForm()

    context = {
        'form': form,
    }

    return render(request, 'add_user.html', context)


def list_of_user(request):
    users = User.objects.all()

    context = {
        'users': users,
    }

    return render(request, 'list_user.html', context)