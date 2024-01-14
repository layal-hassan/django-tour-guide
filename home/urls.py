from django.urls import include ,path 
from . import views

urlpatterns = [
    path('',views.service_list),
    # path('<int :id>',views.service_detail),

]