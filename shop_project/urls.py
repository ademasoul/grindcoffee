"""shop_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

from catalog import urls as catalog_urs
from auth_app import urls as auth_urls


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='catalog/dev_banner.html'), name='home'),
    url(r'^catalog/', include(catalog_urs, namespace='catalog')),
    url(r'^auth/', include(auth_urls, namespace='auth'))



    # url(r'^cart/', TemplateView.as_view(template_name='catalog/_page.html'), name='cart'),
    # url(r'^about/', TemplateView.as_view(template_name='catalog/_page.html'), name='about'),
]
