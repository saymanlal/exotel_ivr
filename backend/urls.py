from django.contrib import admin
from django.urls import path
from ivr.views import start_call, gather

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ivr/start/', start_call),
    path('ivr/gather/', gather),
]
