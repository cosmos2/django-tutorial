from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.IndexView.as_view(), name='index'), # 수정
    # path('<int:question_id>/', views.detail, name='detail'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'), # 수정
    # path('<int:question_id>/results/', views.results, name='results'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'), # 수정
    path('<int:question_id>/vote/', views.vote, name='vote'),
]

