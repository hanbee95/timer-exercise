from django.urls import include, path
from django.conf.urls import url

from . import views
#from .views import geeks_view
app_name = 'exercise'
urlpatterns = [
    # ex: /exercise/
    url(r'^exercise/timer$',views.timer, name='timer'),
    path('', views.index, name='index'),
    path('timer', views.timer, name='timer'),   
    path('timer/showtimer', views.showtimer, name='showtimer'), 
    # ex: /exercise/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /exercise/5/results/
    #path('<int:question_id>/results/', views.results, name='results'),
    # ex: /exercise/5/vote/
    #path('<int:question_id>/vote/', views.vote, name='vote'),
    #path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),    
]