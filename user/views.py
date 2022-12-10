from django.shortcuts import render, redirect

from user.models import User
from order_custom.models import Purchase
from order_custom.models import Payment

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

            return redirect('user_list')

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


def reports(request):
    users = User.objects.all()
    purchases = Purchase.objects.all()
    payments = Payment.objects.all()

    # reports = Payment.objects.all().select_related('purchase__user__id')
    reports = Payment.objects.values('amount', 'purchase__product__title', 'purchase__user__first_name', 'purchase__user__last_name').order_by('purchase__user__id')

    # print(reports)

    for report in reports:
        print(report)
    #     print(report['amount'])
    
    context = {
        'users': users,
        'purchases': purchases,
        'payments': payments,
        'reports': reports,
    }

    return render(request, 'reports.html', context)