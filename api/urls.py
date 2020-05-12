from django.urls import path
from .views import PersonaLis, PersonaList

app_name = 'api'
urlpatterns=[
    path('personas/',PersonaLis.as_view(),name='personalist'),
    path('lista/',PersonaList.as_view(),name="lista")
]
