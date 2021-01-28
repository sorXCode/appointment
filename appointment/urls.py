from django.urls import path

from appointment import views

urlpatterns = [
    path('appointments', views.appointment_list),
    path('appointments/book', views.book_appointment),
    path('block', views.block_time),
]