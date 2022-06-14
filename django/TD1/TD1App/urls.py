from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('infrastructure', views.infrastructure_list_view, name='infrastructures'),
	path('infrastructure/<pk>', views.infrastructure_detail_view, name = 'infrastructure-detail'),
	path('add-infrastructure', views.infrastructure_add_from, name='add-infrastructure'),
	path('infrastructure/<pk>/equipement', views.equipement_list_view, name = 'equipements')
]

