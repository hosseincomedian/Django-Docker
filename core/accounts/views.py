from django.http import HttpResponse
import time
from .tasks import sendEmail
def send_email(request, *args, **kwargs):
    sendEmail.delay()
    return HttpResponse("ok")