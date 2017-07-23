from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /tracker/
    url(r'^$', views.history, name='history'),
    # ex: /tracker/add/
    url(r'^add/', views.add, name='add'),
]
