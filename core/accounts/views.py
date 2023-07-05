from django.http import HttpResponse, JsonResponse
import time
from .tasks import sendEmail
import requests

def send_email(request, *args, **kwargs):
    sendEmail.delay()
    return HttpResponse("ok")

def test(request, *args, **kwargs):
    response = requests.get("https://e3a7ef5a-1f3a-4b12-8490-71bae8aff6bd.mock.pstmn.io/test/delay/5")
    return JsonResponse(response.json())