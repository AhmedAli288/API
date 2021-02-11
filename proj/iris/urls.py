from django.urls import path
from .views import post, iris

app_name = 'iris'

urlpatterns = [
    path('iris/', iris, name='iris'),
    path('ocr/', post, name='ocr'),
]
