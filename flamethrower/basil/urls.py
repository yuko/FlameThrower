from django.conf.urls import url
from . import views
from basil.views import PlacesView

urlpatterns = [
    ## need the (\d*) for delete
    url(r'^places/(\d*)$', PlacesView.as_view()),
    url(r'^$', views.index, name='index'),
    #url(r'^$', PlacesView.as_view()),
]
