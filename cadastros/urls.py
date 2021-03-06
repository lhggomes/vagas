from django.urls import path
from .views import CandidatoCreate, VagaCreate, CandidaturaCrate, VagaUpdate, EmpresaCreate
from .views import VagaDelete
from .views import VagaList, CandidaturaView, VagasDashboardView, CandidatoDashboardView, CandidaturasListView
from .views import pie_chart, pie_char_candidate

urlpatterns = [
    path('cadastrar/candidato/', CandidatoCreate.as_view(), name="cad-candidato"),
    path('cadastrar/vaga/', VagaCreate.as_view(), name="cad-vaga"),
    path('cadastrar/empresa/', EmpresaCreate.as_view(), name="cad-empresa"),
    path('cadastrar/candidatura', CandidaturaCrate.as_view(), name="cad-candidatura"),
    path('editar/vaga/<int:pk>', VagaUpdate.as_view(), name="editar-vaga"),
    path('excluir/vaga/<int:pk>', VagaDelete.as_view(), name="excluir-vaga"),
    path('listar/vagas/', VagaList.as_view(), name="listar-vagas"),
    path('listar/informacao/vaga/<int:vaga_id>', CandidaturaView.as_view(), name="listar-cand-vagas"),
    path('empresa/dashboard/vagas/', VagasDashboardView.as_view(), name="vagas-dashboard"),
    path('empresa/dashboard/candidatos', CandidatoDashboardView.as_view(), name='candidato-dashboard'),
    path('empresa/dashboard/grafico/vagas', pie_chart, name='vagas-mes'),
    path('empresa/dashboard/candidaturas/', CandidaturasListView.as_view(), name="listar-candidaturas"),
    path('empresa/dashboard/grafico/candidatos', pie_char_candidate, name='candidatos-mes'),

]
