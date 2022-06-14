from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('machines/', views.machine_list_view, name='machines'),
	path('machine/<pk>', views.machine_detail_view, name = 'machine-detail'),
	path('employes/', views.employe_list_view, name='employes'),
	path('employe/<pk>', views.employe_detail_view, name = 'employe-detail'),
	path('add-machine', views.machine_add_from, name='add-machine'),
	path('add-employe', views.employe_add_from, name='add-employe'),
	path('infrastructures/', views.infra_list_view, name='infrastructures'),
	path('infrastructure/<pk>', views.infra_detail_view, name = 'infrastructure-detail'),
	path('add-infrastructure', views.infra_add_from, name='infrastructure'),
]

