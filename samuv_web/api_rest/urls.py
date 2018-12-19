from api_rest import views
from django.urls import path



app_name = 'api_rest'

urlpatterns = [
    path('logar/', views.LoginServiceView.as_view(), name='logar'),
    path('iniciar_atendimento/', views.IniciarAtendimentoServiceView.as_view(), name='iniciar_atendimento'),
    #path('usuarios/', views.UsuarioList.as_view(), name='usuarios'),
    #path('usuario/<int:pk>/', views.UsuarioDetail.as_view(), name='usuario'),
    path('pacientes/', views.PacienteList.as_view(), name='pacientes'),
    path('paciente/<int:pk>/', views.PacienteDetail.as_view(), name='paciente'),
    path('paciente_id/', views.PacientePorIdServiceView.as_view(), name='paciente_id'),
    path('doencaPaciente/<int:pk>/', views.DoencaPacienteDetail.as_view(), name='doenca_paciente'),
    path('doencasPacientes/', views.DoencaPacienteList.as_view(), name='doencas_pacientes'),
    path('doenca/<int:pk>', views.DoencaDetail.as_view(), name='doenca'),
    path('doencas/', views.DoencaList.as_view(), name='doencas'),
    path('profissionais/', views.ProfissionalList.as_view(), name='profissionais'),
    path('profissional/<int:pk>/', views.ProfissionalDetail.as_view(), name='profissional'),
    path('profissional_usuario/<int:usuario_id>/', views.ProfissionalPorUsuarioServiceView.as_view(), name='profissional_usuario'),
    path('feridas/', views.FeridaList.as_view(), name='feridas'),
    path('ferida/<int:pk>/', views.FeridaDetail.as_view(), name='feridas'),
    path('cadastrarFerida/', views.CadastrarFeridaServiceView.as_view(), name='cadastrarFerida'),
    path('atualizarFerida/', views.AtualizarFeridaServiceView.as_view(), name='atualizarFerida'),
    path('tecnicas/', views.TecnicaList.as_view(), name='tecnicas'),
    path('tecnica/<int:pk>/', views.TecnicaDetail.as_view(), name='tecnica'),
    path('feridas_paciente/', views.FeridasPorPacienteServiceView.as_view(), name='feridas_paciente'),
    path('atendimentos_ferida/', views.AtendimentosPorFeridaServiceView.as_view(), name='atendimentos_ferida'),
    path('atendimentos/', views.AtendimentoDetail.as_view(), name='atendimentos'),
    path('atendimento/<int:pk>/', views.AtendimentoList.as_view(), name='atendimento'),
    path('atendimentos_paciente/<int:pk>/', views.AtendimentosPorPacienteServiceView.as_view(), name='atendimentos_paciente'),
    path('imagem_atendimento/<int:atendimento_id>/', views.ImagemPorAtendimentoServiceView.as_view(), name='imagem_atendimento'),
    path('atendimento_extra/<int:pk>/', views.AtendimentoExtraDetail.as_view(), name='atendimento_extra'),
    path('atendimentos_extras/', views.AtendimentoExtraList.as_view(), name='atendimentos_extras'),
    path('tecnicas_atendimento/<int:atendimento_id>/', views.TecnicasPorAtendimentoServiceView.as_view(), name='tecnicas_atendimento'),
    path('agenda/<int:pk>', views.AgendaDetail.as_view(), name='agenda'),
    path('agendas/', views.AgendaList.as_view(), name='agendas'),

    path('anamnese/<int:pk>/', views.AnamneseDetail.as_view(), name='anamnese'),
    path('anamneses/', views.AnamneseList.as_view(), name='anamneses'),

    # SEGMENTAÇÃO E ANÁLISE DE IMAGENS
    #URLS SEGMENTACAO
    path('pacientes_com_atendimento/', views.PacientesComAtendimentoServiceView.as_view(), name="pacientes_com_atendimento"),
    path('atendimentos_paciente/<int:pk>', views.AtendimentosPorPacienteServiceView.as_view(), name="atendimentos_paciente"),
    path('get_imagem_cadastrada_base64/', views.ImagemCadastradaBase64ServiceView.as_view(), name="get_imagem_cadastrada_base64"),
    path('get_imagem_segmentada_cadastrada/', views.ImagemSegmentadaBase64ServiceView.as_view(), name="get_imagem_segmentada_cadastrada"),
    path('caracteristica/', views.CaracteristicaServiceView.as_view(), name="caracteristica"),
    path('analisar_imagem_base64/', views.AnalisarImagemBase64ServiceView.as_view(), name="analisar_imagem_base64"),
    # path('segmentar_imagem/<int:idImagem>', views.SegmentarImagemServiceView.as_view(), name='segmentar_imagem'),
]

