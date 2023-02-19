"""webbugs URL Configuration

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
from django.contrib import admin
from django.urls import path
from api.views import topsupplier, searchshops, shopsuppliers, ReportSend

urlpatterns = [
    path('admin/', admin.site.urls),
    path('topsupplier/', topsupplier, name='top-suppliers'),
    path('searchshops/', searchshops, name='search-shops'),
    path('suppliers-by-shop/<int:shop_id>/', shopsuppliers, name='suppliers-by-shop'),
    path('ReportSend-email/', ReportSend, name='send-report-email'),
]
