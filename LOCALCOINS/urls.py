"""LOCALCOINS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import django
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _

urlpatterns = [
    path("home",views.home,name="home"),
    
    path('i18n/', include('django.conf.urls.i18n')),
]


urlpatterns += i18n_patterns(
    path(_('admin/'), admin.site.urls),
    
    path('home/', include('account.urls')),
    path('', include('advertisements.urls')),
    path('', include('traderequest.urls')),
    path('', include('cryptocurrency.urls')),
    path('', include('user_logged_in.urls')),
    path('', include('wallet.urls')),
    path('', include('transactions.urls')),
    path('', include('support.urls')),
    path('adminpage/', include('all_extensions_languagemanager.urls')),
    path('adminpage/', include('emailtemplates_faq.urls')),
    path('adminpage/', include('policypages_managesection.urls')),
    path('home/', include('contact.urls')),
    path('adminpage/', include('admin_app.urls')),
    path('adminpage/', include('paymentwindows.urls')),
    path('adminpage/', include('fiatgateways.urls')),
    path('adminpage/', include('fiatcurrency.urls')),
    prefix_default_language=False,
    
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)