from django.urls import path
from samuv_site import views, forms
from django.contrib.auth import views as auth_views

from .views import Grafico, get_data, ChartData, ListaPaciente

app_name = 'samuv_site'

urlpatterns = [
    path('index/', views.index, name='index'),
    #path('login/', auth_views.login, {'template_name': 'registration/login.html', 'authentication_form': forms.LoginForm}, name='login'),
    path('login/', views.CriarLogin.as_view(), {'template_name': 'registration/login.html', 'authentication_form': forms.LoginForm}, name='login'),
    path('logout/', auth_views.logout, name='logout'),
    path('password-reset/', views.password_reset, name='password_reset'),
    path('password-reset/done', auth_views.password_reset_done, name='password_reset_done'),
    path('password-reset/confirm/', auth_views.password_reset_confirm, name='password_reset_confirm'),
    path('password-reset/complete/', auth_views.password_reset_complete, name='password_reset_complete'),

    path('inicio/', views.inicio, name='inicio'),
    path('pacientes/', views.pacientes, name='pacientes'),
    path('listarDadosPaciente/<int:pk>', views.listarDadosPaciente, name='url_listarDadosPaciente'),
    path('cadastrarAnamnese/<int:pk>', views.CadastrarAnamnese.as_view(), name='url_cadastrarAnamnese'),
    path('cadastrarObservacao/<int:pk>', views.CadastrarObservacao.as_view(), name='url_cadastrarObservacao'),
    path('cadastrarHabitosPessoais/<int:pk>', views.CadastrarHabitosPessoais.as_view(), name='url_cadastrarHabitosPessoais'),
    path('cadastrarDadosClinicos/<int:pk>', views.CadastrarDadosClinicos.as_view(), name='url_cadastrarDadosClinicos'),
    path('cadastrarFerida/<int:pk>', views.CadastrarFerida.as_view(), name='url_cadastrarFerida'),
    path('cadastrarAtendimento/<int:pk>', views.CadastrarAtendimento.as_view(), name='url_cadastrarAtendimento'),
    path('cadastrarCaracteristicaFerida/<int:pk>', views.CadastrarCaracteristicaFerida.as_view(), name='url_cadastrarCaracteristicaFerida'),
    path('relatorio/', views.relatorio, name='relatorio'),
    path('base/', views.base, name='base'),
    path('cadastrarPaciente/', views.CadastrarPaciente.as_view(), name='url_cadastrarPaciente'),
    path('atualizarPaciente/<int:pk>/', views.AtualizarPaciente.as_view(), name='url_atualizarPaciente'),
    path('excluirPaciente/<int:pk>/', views.excluirPaciente, name='url_excluirPaciente'),
    path('feridasPaciente/<int:pk>', views.feridasPaciente, name='url_feridasPaciente'),
    path('atendimentos/<int:pk>', views.atendimentosPaciente, name='url_atendimentosPaciente'),
    path('analise/<int:pk>', views.analiseAtendimento, name='url_analiseAtendimento'),

    # path('segmentar/', views.segmentar, name='segmentar'),
    path('grafico/', views.Grafico.as_view(), name='grafico'),
    path('api/data/', views.get_data, name='api-data'),
    path('api/chart/data/', ChartData.as_view()),

    path('paciente_lista/', ListaPaciente.as_view()),
    path('anamnese/<int:pk>', views.listarAnamneses, name='url_listarAnamneses'),

    path('loginadm/', views.CriarLoginAdm.as_view(), {'template_name': 'registration/loginadm.html', 'authentication_form': forms.LoginForm}, name='loginadm'),
    path('inicioadm/', views.inicioAdm, name='inicioadm'),
    path('logoutadm/', views.logoutAdm, name='logoutadm'),
]
