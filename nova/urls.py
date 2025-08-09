from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("accounts/", include("allauth.urls")),
    path("admin/", admin.site.urls),
    path("summernote/", include("django_summernote.urls")),
    path("", include("home.urls", namespace="home")),
    path("menu/", include("menu.urls", namespace="menu")),
    path("reservations/", include("reservations.urls"), name="reservations-urls"),
    path("reviews/", include("reviews.urls", namespace="reviews")),
    path("contact/", include("contact.urls", namespace="contact")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
