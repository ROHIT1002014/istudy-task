from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import homePageView, loginView, logoutView

urlpatterns = [
    path('', homePageView, name='home'),
    path('login/', loginView, name='login'),
    path('logout/', logoutView, name='logout')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
