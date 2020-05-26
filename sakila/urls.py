from django.urls import path

from . import views

app_name = 'sakila'
urlpatterns = [
    path('', views.IndexView.as_view(), name='customer_index'),
    path('<int:pk>/', views.DetailView.as_view(), name='customer_detail'),
    path('update/<int:pk>/', views.DeleteView.as_view(), name='customer_update'),
    path('delete/<int:pk>/', views.DeleteView.as_view(), name='customer_delete'),
    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]