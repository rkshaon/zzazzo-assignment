from django.shortcuts import render, redirect

from rest_framework.decorators import api_view
from rest_framework.response import Response

from user.models import User
from order_custom.models import Purchase
from order_custom.models import Payment

from user.forms import NewUserForm
from user.serializers import UserSerializer
from order_custom.serializers import PurchaseSerializer
from order_custom.serializers import PaymentSerializer


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
    
    reports = Payment.objects.values('amount', 'purchase__product__title', 'purchase__user__first_name', 'purchase__user__last_name').order_by('purchase__user__id')
    
    final_reports = []

    for user in users:
        purchase_list = Purchase.objects.filter(user=user)

        temp = []

        for purchase in purchase_list:
            payment_list = Payment.objects.filter(purchase=purchase)

            temp.append({
                'purchase': purchase,
                'payment': payment_list
            })

        final_reports.append({
            'user': user,
            'purchase': temp,
        })

    context = {
        'users': users,
        'purchases': purchases,
        'payments': payments,
        'reports': reports,
        'final': final_reports,
    }

    return render(request, 'reports.html', context)


@api_view(['GET'])
def reports_api(request):
    final_reports = []
    users = User.objects.all()

    for user in users:
        user_data = UserSerializer(user, many=False).data

        purchase_list = Purchase.objects.filter(user=user)

        temp = []

        for purchase in purchase_list:
            payment_list = Payment.objects.filter(purchase=purchase)

            temp.append({
                'purchase': PurchaseSerializer(purchase, many=False).data,
                'payment': PaymentSerializer(payment_list, many=True).data,
            })

        final_reports.append({
            'user': user_data,
            'purchase': temp,
        })

    data = final_reports

    return Response({
        'status': True,
        'data': data,
    })