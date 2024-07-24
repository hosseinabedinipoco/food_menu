from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'food'
urlpatterns = [
    path('', views.index, name="index"),
    path('delete/<int:id>', views.delete, name="delete"),
    path('add', views.add, name="add"),
    path('update/<int:id>', views.update, name="update")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)