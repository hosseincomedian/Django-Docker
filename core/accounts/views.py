from django.http import HttpResponse, JsonResponse
import time
import requests
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from .tasks import sendEmail

def send_email(request, *args, **kwargs):
    sendEmail.delay()
    return HttpResponse("ok")

@cache_page(60)
def test(request, *args, **kwargs):
    response = requests.get("https://e3a7ef5a-1f3a-4b12-8490-71bae8aff6bd.mock.pstmn.io/test/delay/5")
    return JsonResponse(response.json())