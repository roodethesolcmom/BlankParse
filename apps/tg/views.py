
# -*- encoding: utf-8 -*-

from django.http import JsonResponse
import logging
import threading
import json
from django.views.generic import View
from django.views.generic.base import RedirectView
# from django.conf import settings
# from .models import Users, Items, PaymentHistory, Profiles, ReferalBase, Audiences
# from .kb import inlinekb
#from .TextConfig import Texts as textconf
# from .TextConfig import Links as link
from telebot import types
from .front import bot

logging.basicConfig(level=logging.INFO)

def index(request):
    return JsonResponse({"error": "sup hacker"})

class GrafanaRedirect(RedirectView):
    url = 'https://92.255.110.178:3000'

class GraphQL(RedirectView):
    url = 'http://92.255.110.178:8080'

class WebhookTG(View):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        update = types.Update.de_json(data)
        upd = bot.process_new_updates([update])
        bu = threading.Thread(upd)
        bu.start()
        return JsonResponse({"ok": "200"})

    def get(self, request, *args, **kwargs):  # for debug
        return JsonResponse({"ok": "200"})
