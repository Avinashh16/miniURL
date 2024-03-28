from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('success/<url>',views.success,name='success'),
    path('<str:url>',views.miniurl,name='miniurl')
]
handler404 = views.error_404_view