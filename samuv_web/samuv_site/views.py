from samuv_site import models
from django.shortcuts import render, redirect
from samuv_site.forms import PacienteForm, LoginForm, AnamneseForm, ResetForm, ObservacaoForm, HabitosPessoaisForm, \
    ClinicoForm, FeridaForm, AtendimentoForm, CaracteristicaFeridaForm  #UserForm
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.views.generic.edit import CreateView, FormView, UpdateView 
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from django.views.generic import View
from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model

from api_rest.serializers import PacienteSerializer
import json, requests
from django.db.models import Count, Q

from .multiforms import MultiFormsView

def index(request):
    return render(request, 'samuv_site/index.html', {})


class CriarLogin(FormView):
    model = models.Profissional
    form_class = LoginForm
    sucess_url = '../inicio'
    template_name = 'registration/login.html'
    #success_url = reverse_lazy('samuv_site:inicio')

    def form_valid(self, form):
        '''form.save()
        username = form.cleaned_data.get('login')
        raw_password = form.cleaned_data.get('senha')
        user = authenticate(username=username, password=raw_password)
        login(self.request, user)
        return redirect(self.sucess_url)'''
        login(self.request, form.get_user())
        return HttpResponseRedirect(self.sucess_url)


class CriarLoginAdm(FormView):
    model = models.Profissional
    form_class = LoginForm
    sucess_url = '../inicioadm'
    template_name = 'registration/loginadm.html'

    def form_valid(self, form):
        login(self.request, form.get_user())
        return HttpResponseRedirect(self.sucess_url)


@login_required(login_url=settings.LOGIN_ADM_URL)
def inicioAdm(request):
    return render(request, 'samuv_site/inicioadm.html')


def logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login/'))


def logoutAdm(request):
    logoutAdm(request)
    return HttpResponseRedirect(reverse('loginadm/'))


@login_required(login_url=settings.LOGIN_URL)
def inicio(request):
    return render(request, 'samuv_site/inicio.html')


@login_required(login_url=settings.LOGIN_URL)
def pacientes(request):
    if request.user.is_authenticated:
        requisicao = requests.get("http://127.0.0.1:8000/samuv_site/paciente_lista/?format=json")
        paciente_lista = json.loads(requisicao.content)
        return render(request, 'samuv_site/pacientes.html', {'paciente_lista': paciente_lista})


@login_required(login_url=settings.LOGIN_URL)
def relatorio(request):
    if request.user.is_authenticated:
        requisicao = requests.get("http://127.0.0.1:8000/samuv_site/paciente_lista/?format=json")
        resposta = json.loads(requisicao.content)
        #contexto = {'resposta': resposta}
        return render(request, 'samuv_site/relatorio.html', {'resposta': resposta})


def base(request):
    return render(request, 'samuv_site/base.html')


#código para trabalhar com multiplos formulários 
def form_redir(request):
    return render(request, 'samuv_site/pacientes.html')

def multiple_forms(request):
    if request.method == 'POST':
        paciente_form = PacienteForm(request.POST)
        anamenese_form = AnamneseForm(request.POST)
        habitosPessoais_form = HabitosPessoaisForm(request.POST)
        clinico_form = ClinicoForm(request.POST)
        observacao_form = ObservacaoForm(request.POST)

        if paciente_form.is_valid() or anamenese_form.is_valid() or habitosPessoais_form.is_valid() or clinico_form.is_valid() or observacao_form.is_valid():
            # Do the needful
            return HttpResponseRedirect(reverse('samuv_site:pacientes') )
    else:
        paciente_form = PacienteForm()
        anamenese_form = AnamneseForm()
        habitosPessoais_form = HabitosPessoaisForm()
        clinico_form = ClinicoForm()
        observacao_form = ObservacaoForm()
            
    return render(request, 'samuv_site/cadastrarPacinete.html', {
        'paciente_form': paciente_form,
        'anamnese_form': anamnese_form,
        'habitosPessoais_form': habitosPessoais_form,
        'clinico_form': clinico_form,
        'observacao_form': observacao_form
    })
# fim



class CadastrarPaciente(LoginRequiredMixin, MultiFormsView):
    #model = models.Paciente
    template_name = 'samuv_site/cadastrarPaciente.html'
    form_classes = {'pacienteForm': PacienteForm, 
                    'anamneseForm': AnamneseForm,
                    'habitosPessoaisForm': HabitosPessoaisForm,
                    'clinicoForm': ClinicoForm,
                    'observacaoForm': ObservacaoForm
                    }
    #success_url = reverse_lazy('samuv_site:url_cadastrarPaciente')
    success_urls = {'pacienteForm': reverse_lazy('samuv_site:url_cadastrarPaciente'),
                    'anamneseForm': reverse_lazy('samuv_site:pacientes'),
                    'habitosPessoaisForm': reverse_lazy('samuv_site:url_cadastrar'),
                    'clinicoForm': reverse_lazy('samuv_site:url_cadastrarDadosClinicos'),
                    'observacaoForm': reverse_lazy('samuv_site:url_cadastrarObersavao')
                    }

    '''
    def form_valid(self, form):
        paciente = form.save()
        messages.add_message(self.request,
                             messages.SUCCESS,
                             'Paciente cadastrado com sucesso')
        return redirect('samuv_site:pacientes')
    '''

    def paciente_form_valid(self, form):
        #title = form.cleaned_data.get('title')
        form_name = form.cleaned_data.get('action')
        return HttpResponseRedirect(self.get_success_url(form_name))

    def anamnese_form_valid(self, form):
        form_name = form.cleaned_data.get('action')
        return HttpResponseRedirect(self.get_success_url(form_name))

    def habitosPessoais_form_valid(self, form):
        form_name = form.cleaned_data.get('action')
        return HttpResponseRedirect(self.get_success_url(form_name))

    def clinico_form_valid(self, form):
        form_name = form.cleaned_data.get('action')
        return HttpResponseRedirect(self.get_success_url(form_name))

    def observacao_form_valid(self, form):
        form_name = form.cleaned_data.get('action')
        return HttpResponseRedirect(self.get_success_url(form_name)) 
    

class CadastrarAnamnese(LoginRequiredMixin, CreateView):
    model = models.Anamnese
    form_class = AnamneseForm
    template_name = 'samuv_site/cadastrarAnamnese.html'
    success_url = reverse_lazy('samuv_site:url_cadastrarAnamnese')

    def form_valid(self, form):
        anamnese = form.save()
        messages.add_message(self.request,
                             messages.SUCCESS,
                             'Anamnese cadastrada com sucesso')
        return redirect('samuv_site:pacientes')


class CadastrarObservacao(LoginRequiredMixin, CreateView):
    model = models.Observacao
    form_class = ObservacaoForm
    template_name = 'samuv_site/cadastrarObservacao.html'
    success_url = reverse_lazy('samuv_site:url_cadastrarObersavao')

    def form_valid(self, form):
        observacao = form.save()
        messages.add_message(self.request,
                             messages.SUCCESS,
                             'Obervação cadastrada com sucesso')
        return redirect('samuv_site:pacientes')


class CadastrarHabitosPessoais(LoginRequiredMixin, CreateView):
    model = models.HabitosPessoais
    form_class = HabitosPessoaisForm
    template_name = 'samuv_site/cadastrarHabitosPessoais.html'
    success_url = reverse_lazy('samuv_site:url_cadastrarHabitosPessoais')

    def form_valid(self, form):
        habitosPessoais = form.save()
        messages.add_message(self.request,
                             messages.SUCCESS,
                             'Habitos Pessoais cadastrados com sucesso')
        return redirect('samuv_site:pacientes')


class CadastrarDadosClinicos(LoginRequiredMixin, CreateView):
    model = models.Clinico
    form_class = ClinicoForm
    template_name = 'samuv_site/cadastrarDadosClinicos.html'
    success_url = reverse_lazy('samuv_site:url_cadastrarDadosClinicos')

    def form_valid(self, form):
        habitosPessoais = form.save()
        messages.add_message(self.request,
                             messages.SUCCESS,
                             'Dados Clinicos cadastrados com sucesso')
        return redirect('samuv_site:pacientes')


class AtualizarPaciente(LoginRequiredMixin, UpdateView):
    model = models.Paciente
    form_class = PacienteForm
    template_name = 'samuv_site/cadastrarPaciente.html'
    success_url = reverse_lazy('samuv_site:pacientes')

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request,
                             messages.SUCCESS,
                             'Paciente atualizado com sucesso')
        return redirect('samuv_site:pacientes')

        
@login_required(login_url=settings.LOGIN_URL)
def listarDadosPaciente(request, pk):
    if request.user.is_authenticated:
        requisicao = requests.get("http://127.0.0.1:8000/api_rest/pacientes/?format=json")
        paciente_informacao = json.loads(requisicao.content)
        requisicao2 = requests.get("http://127.0.0.1:8000/api_rest/atendimentos/?format=json")
        atendimento_informacao = json.loads(requisicao2.content)
        requisicao3 = requests.get("http://127.0.0.1:8000/api_rest/doencasPacientes/?format=json")
        doenca_informacao = json.loads(requisicao3.content)
        #paciente_informacao = models.Paciente.objects.filter(pk=pk)
        return render(request, 'samuv_site/listarDadosPaciente.html', {'paciente_informacao': paciente_informacao,
            'atendimento_informacao': atendimento_informacao, 'doenca_informacao': doenca_informacao})


@login_required(login_url=settings.LOGIN_URL)
def listarAnamneses(request, pk):
    anamnese_informacao = models.Anamnese.objects.all()
    return render(request, 'samuv_site/listarAnamneses', {'anamnese_informacao': anamnese_informacao})


class CadastrarFerida(LoginRequiredMixin, CreateView):
    model = models.Ferida
    form_class = FeridaForm
    template_name = 'samuv_site/cadastrarFerida.html'
    success_url = reverse_lazy('samuv_site:pacientes')

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request,
                             messages.SUCCESS,
                             'Ferida cadastrada com sucesso')
        return redirect('samuv_site:pacientes')


class CadastrarCaracteristicaFerida(LoginRequiredMixin, CreateView):
    model = models.CaracteristicaFerida
    form_class = CaracteristicaFeridaForm
    template_name = 'samuv_site/cadastrarCaracteristicaFerida.html'
    success_url = reverse_lazy('samuv_site:cadastrarCaracteristicaFerida')

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request,
                             messages.SUCCESS,
                             'Caracteristica cadastrada com sucesso')
        return redirect('samuv_site:pacientes')


class CadastrarAtendimento(LoginRequiredMixin, CreateView):
    model = models.Atendimento
    form_class = AtendimentoForm
    template_name = 'samuv_site/cadastrarAtendimento.html'
    success_url = reverse_lazy('samuv_site:cadastrarAtendimento')

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request,
                             messages.SUCCESS,
                             'Atendimento cadastrado com sucesso')
        return redirect('samuv_site:pacientes')


@login_required(login_url=settings.LOGIN_URL)
def excluirPaciente(request, pk):
    paciente = models.Paciente.objects.get(pk=pk)
    paciente.delete()
    return redirect('samuv_site:pacientes')


def segmentation_web_view(request):
    return render(request, 'samuv_site/segmentation_web/index.htm', {})


def password_reset(request):
    form = ResetForm()
    return render(request, 'registration/password_reset_form.html', {form:'form'})


@login_required(login_url=settings.LOGIN_URL)
def atendimentosPaciente(request, pk):
    if request.user.is_authenticated:
        atendimento_extra = models.AtendimentoExtra.objects.filter(ferida__pk=pk).all().order_by('-pk')
        atendimento_informacao = models.Atendimento.objects.filter(doencaPaciente__paciente__pk=pk).all().order_by('-pk')
        atendimento_tecnica = models.AtendimentoTecnica.objects.filter(tecnica__pk=pk).all().order_by('-pk')
        return render(request, 'samuv_site/atendimentosPaciente.html', {'atendimento_informacao': atendimento_informacao,
            'atendimento_extra': atendimento_extra, 'atendimento_tecnica': atendimento_tecnica})
    #paciente_dados = models.Paciente.objects.all()
    #atendimentosPaciente = models.Atendimento.objects.filter(ferida__pk=pk).all()
    #return render(request, 'samuv_site/atendimentosPaciente.html', {'atendimentosPaciente': atendimentosPaciente,
     #       'paciente_dados': paciente_dados})
    #if request.user.is_authenticated:
     #   requisicao = requests.get("http://127.0.0.1:8000/api_rest/atendimentos/?format=json")
      #  atendimento_informacao = json.loads(requisicao.content)
       # return render(request, 'samuv_site/atendimentosPaciente.html', {'atendimento_informacao': atendimento_informacao})


@login_required(login_url=settings.LOGIN_URL)
def feridasPaciente(request, pk):
    if request.user.is_authenticated:
        atendimento_extra = models.AtendimentoExtra.objects.filter(ferida__pk=pk).all().order_by('-pk')
        #atendimento_tecnica = models.AtendimentoTecnica.objects.all(tecnica__pk=pk).all().order_by('-pk')
        return render(request, 'samuv_site/feridasPaciente.html', {'atendimento_extra': atendimento_extra})
    #feridas = models.Ferida.objects.filter(paciente__pk=pk).all().order_by('-pk')
    #doencaPaciente_informacao = models.DoencaPaciente.objects.get(paciente__pk=pk)
    #return render(request, 'samuv_site/feridasPaciente.html', {'doencaPaciente_informacao': doencaPaciente_informacao})
    #if request.user.is_authenticated:
     #   requisicao = requests.get("http://127.0.0.1:8000/api_rest/atendimentos_extras/?format=json")
      #  feridas = json.loads(requisicao.content)
       # return render(request, 'samuv_site/feridasPaciente.html', {'feridas': feridas})

@login_required(login_url=settings.LOGIN_URL)
def analiseAtendimento(request, pk):
    if request.user.is_authenticated:
        atendimento_informacao = models.Atendimento.objects.filter(doencaPaciente__paciente__pk=pk).all().order_by('-pk')
        atendimento_tecnica = models.AtendimentoTecnica.objects.filter(tecnica__pk=pk).all().order_by('-pk')
        atendimento_extra = models.AtendimentoExtra.objects.filter(ferida__pk=pk).all().order_by('-pk')
        return render(request, 'samuv_site/analise.html', {'atendimento_informacao': atendimento_informacao,
            'atendimento_tecnica': atendimento_tecnica, 'atendimento_extra': atendimento_extra})
    #atendimento = models.Atendimento.objects.get(pk=pk)
    #caracteristica = None
    #ferida = models.Ferida.objects.filter(paciente__pk=pk).all().order_by('-pk')
    #tecnica = models.Tecnica.objects.all()

    #dataset = Atendimento.objects \
     #   .values('ferida') \
      #  .annotate(medida=Count('ferida', filter=Q(dataset.caracteristica.area==3.0))) \
       # .order_by('ferida')

    #if atendimento.imagemAnalisada:
     #   caracteristica = models.CaracteristicaFerida.objects.get(pk=atendimento.caracteristica.pk)

    #return render(request, 'samuv_site/analise.html', {'atendimento': atendimento, 'caracteristica': caracteristica, 
     #       'ferida': ferida})


User = get_user_model()

class Grafico(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'samuv_site/chart.html', {"clientes": 10})


def get_data(request, *args, **kwargs):
    data = {
        "vendas": 100,
        "clientes": 10,
    }
    return JsonResponse(data) #http response


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        qs_count = User.objects.all().count()
        labels: ["Users", "Blue", "Yellow", "Green", "Purple", "Orange"]
        default_items = [qs_count, 1234, 1233, 32, 12, 67, 89]
        data = {
            "labels": labels,
            "default": default_items,
            #"users": User.objects.all().count(),
        }
        return Response(data)


class ListaPaciente(APIView):

    def get(self, request):
        pacientes = models.Paciente.objects.all()
        serializer = PacienteSerializer(pacientes, many=True)
        return Response(serializer.data)