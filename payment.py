

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
import razorpay

razorpay_client = razorpay.Client(auth=(settings.RAZORPAY_API_KEY, settings.RAZORPAY_API_SECRET_KEY))

class PaymentView(APIView):
    def post(self, request):
        order_id = request.data['order_id']
        payment_method = request.data['payment_method']
        amount = request.data['amount']

        order = Order.objects.get(id=order_id)
        payment = Payment(order=order, payment_method=payment_method, amount=amount)

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
        razorpay_order = razorpay_client.order.create(dict(amount=amount, currency='INR', receipt='order_rcptid_11'))

        # Redirect the user to the Razorpay payment page
        return Response({'redirect_url': razorpay_order['payment_url']}, status=302)
