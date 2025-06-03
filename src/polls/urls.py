from django.urls import path

from polls import views

app_name = 'polls'

urlpatterns = [
    path('', views.PollListView.as_view(), name='poll_list'),
    path('create/', views.PollCreateView.as_view(), name='poll_create'),
    path('<int:pk>/', views.PollDetailView.as_view(), name='poll_detail')
]

