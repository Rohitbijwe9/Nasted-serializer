from django.urls import path
from.views import SongView,SingerView

urlpatterns=[
    path('song/',SongView.as_view()),
    path('singer/',SingerView.as_view())

]