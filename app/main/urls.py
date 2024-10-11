from django.urls import path
from main import views
# Тут указаны пути только для main поэтому создал отдельынй urls
app_name='main'
urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about')
]
 