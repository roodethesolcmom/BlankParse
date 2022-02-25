# -*- encoding: utf-8 -*-

from django.urls import path
from .views import WebhookTG, GrafanaRedirect, GraphQL
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('tg/', csrf_exempt(WebhookTG.as_view()), name="tg"),
    path('stats/', GrafanaRedirect.as_view()),
    path('graph/', GraphQL.as_view())

]
