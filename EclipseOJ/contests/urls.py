from django.conf.urls import url, include
from . import views as contests_views

urlpatterns = [
    url(r'^$', contests_views.index, name='index'),
    url(r'^(?P<contestID>[0-9]+)/$', contests_views.contest, name='contest'),
]