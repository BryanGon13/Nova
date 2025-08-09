from django.urls import path

from .views import reservation_delete, reservation_list, reservation_update

app_name = "reservation"

urlpatterns = [
    path("", reservation_list, name="reservation_list"),
    path("<int:pk>/edit/", reservation_update, name="reservation_update"),
    path("<int:pk>/delete/", reservation_delete, name="reservation_delete"),
]
