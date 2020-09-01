"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from django.urls import path,include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from projects import views as pview
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from ckeditor_uploader import views as ckeditor_views



urlpatterns = [
    url(r'^$', pview.project_index,name="project_index"),
    url(r'^admin/', admin.site.urls),
    path("",include("users.urls")),
    path("projects/",include("projects.urls")),
    path("blog/",include("blog.urls")),
    path("art/", include("art.urls")),
    url(r'^ckeditor/upload/', login_required(ckeditor_views.upload), name='ckeditor_upload'),
    url(r'^ckeditor/browse/', never_cache(login_required(ckeditor_views.browse)), name='ckeditor_browse'),   
] 



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
