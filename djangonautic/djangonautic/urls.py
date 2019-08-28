
from django.contrib import admin
from django.conf.urls import url, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# from django.urls import path
# from django.contrib import url
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    url(r'^admin/',admin.site.urls),
    url(r'^articles/',include('articles.urls')),
    url(r'^about/$',views.about),
    url(r'^$', views.homepage),
]

urlpatterns += staticfiles_urlpatterns()
