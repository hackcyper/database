from django.db import models

class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=255)
    payment_status = models.CharField(max_length=255)
    payment_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)

from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Payment

class PaymentSuccessView(APIView):
    def post(self, request):
        payment_id = request.data['payment_id']
        payment_status = request.data['payment_status']

        payment = Payment.objects.get(id=payment_id)
        payment.payment_status = payment_status
        payment.save()

        return Response({'message': 'Payment successful'}, status=201)

class PaymentFailureView(APIView):
    def post(self, request):
        payment_id = request.data['payment_id']
        payment_status = request.data['payment_status']

        payment = Payment.objects.get(id=payment_id)
        payment.payment_status = payment_status
        payment.save()

        return Response({'message': 'Payment failed'}, status=400)
