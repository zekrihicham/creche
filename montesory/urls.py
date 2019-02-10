from django.urls import path

from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.first_page, name='first_page'),
    path('admin', views.dashboardAdmin, name='dashboardAdmin'),
    path('admin/ajouterEns', views.ajouterEnseignant, name='ajouterEnseignant'),
    path('admin/ajouterModule', views.ajouterModule, name='ajouterModule'),
    path('admin/affectation', views.affectation, name='affectation'),
    path('admin/affectation/<int:id_affectation>', views.desaffecter, name='desaffecter'),
    path('admin/ajouterEnfant', views.ajouterEnfant, name='ajouterEnfant'),
    path('admin/consu_clients', views.consu_clients, name='consu_clients'),
    path('admin/consu_clients/s/<int:id_client>', views.supp_client, name='supp_client'),
    path('admin/consu_clients/m/<int:id_client>', views.modifierEnfant, name='modifierEnfant'),
    path('admin/consu_clients/<int:id_client>', views.client, name='client'),
    path('admin/Enfant/<int:id_client>/parent', views.ajouterParent, name='ajouterParent'),
    path('admin/article', views.article, name='article'),
    path('admin/enseignants', views.enseignants, name='enseignants'),
    path('admin/enseignants/s/<int:id_ens>', views.sup_enseignants, name='sup_enseignants'),
    path('admin/enseignants/m/<int:id_ens>', views.modifier_ens, name='modifier_ens'),
    path('admin/enseignants/<int:id_ens>', views.enseignant, name='enseignant'),
    path('admin/articles', views.voir_contacts, name='voir_contacts'),
    path('admin/test', views.test, name='test'),
    path('admin/test1', views.test1, name='test1'),
    path('admin/test1/<int:id_mes>', views.test4, name='test4'),

    path('admin/test2', views.test2, name='test2'),

    path('admin/ajouterGroupe', views.ajouterGroupe, name='ajouterGroupe'),
    #---------------------------------------------------------------------------------------------------
    path('login/', auth_views.login, name='login'),
    path('logout/', auth_views.logout, name='logout'),
    path('admin1/', views.valide, name='valide'),


    #----------------------------------------------------------------------------------------------------
    path('admin1/teacher/<int:id_user>', views.teacher, name='teacher'),
    path('admin1/teacher/<int:id_user>/consulterEnfant', views.consulterEnfant, name='consulterEnfant'),
      path('admin1/teacher/<int:id_user>/statistique', views.statTeacher, name='statTeacher'),

]
