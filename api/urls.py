from django.conf.urls import url
from django.urls import path
from api.views import HomeView, AlbumsView,NewsView,ArticleView,Pop30View,EventView
from . import views
app_name = 'api'

urlpatterns = [
    # url(r'^$', HomeView.as_view(), name = 'home'),
    path('', HomeView.as_view(), name = 'home'),
    # path('albums/', views.albums, name="albums"),
    path('albums/', AlbumsView.as_view(), name='albums'),
    path('news/', NewsView.as_view(), name='news'),
    path('event/', EventView.as_view(), name='event'),
    path('article/', ArticleView.as_view(), name='article'),
    path('pop30/', Pop30View.as_view(), name='pop30'),
]