from django.urls import path
from django.urls.resolvers import URLPattern
from . import views



app_name='flights'
urlpatterns = [
  path('',views.index,name='index'),
  path('<int:flight_id>',views.show,name='show')
]