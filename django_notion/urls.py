"""mesto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from django.conf import settings
from django.conf.urls.static import static

from blog.views import home_page, blog_home, blog_post, blog_category
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),

    # path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('', home_page, name='index'),
    path('blog', blog_home, name='blog_home'),
    path('blog/category/<int:code>', blog_category, name='blog_category'),
    path('blog/<int:code>', blog_post, name='blog_post'),
    path('about', TemplateView.as_view(template_name='about.html'), name='about'),
    path('contact', TemplateView.as_view(template_name='contact.html'), name='contact'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
