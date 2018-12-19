from django.forms import ModelForm, ChoiceField, RadioSelect, TextInput, CharField, DateField, PasswordInput, DateInput,\
    IntegerField, FloatField, ModelChoiceField, DateTimeField #BooleanField
from .models import Paciente, Anamnese, Observacao, HabitosPessoais, Clinico, Ferida, Atendimento, CaracteristicaFerida,\
    Profissional, Tecnica
from django.contrib.auth import models as auth_models
from django.contrib.auth import forms as auth_forms
from django import forms

'''
from django.utils.translation import ugettext as _
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
'''


class MultipleForm(forms.Form):
    action = forms.CharField(max_length=60, widget=forms.HiddenInput())


class ClinicoForm(MultipleForm):
    diagnosticoUsuario = CharField(widget=TextInput(attrs={'class': 'form-control'}), label='Diagnostico do Usuário')
    diagnosticoEquipe = CharField(widget=TextInput(attrs={'class': 'form-control'}), label='Diagnostico da Equipe Médica')
    diagnosticoPesquisadora = CharField(widget=TextInput(attrs={'class': 'form-control'}), label='Diagnostico do(a) pesquisador(a)')
    resultadoExames = CharField(widget=TextInput(attrs={'class': 'form-control'}), label='Resultado dos Exames')

    class Meta:
        model = Clinico
        fields = ['diagnosticoUsuario', 'diagnosticoEquipe', 'diagnosticoPesquisadora', 'resultadoExames']


etilismo = (
    ('S', 'Sim'), ('N', 'Não'),
)

tabagismo = (
    ('S', 'Sim'), ('N', 'Não'),
)

alergiaTopica = (
    ('S', 'Sim'), ('N','Não'),
)

class HabitosPessoaisForm(MultipleForm):
    numeroRefeicoesDia = IntegerField(widget=TextInput(attrs={'class': 'form-control'}), label='Número de Refeições ao Dia')
    habitosAlimentares = CharField(widget=TextInput(attrs={'class': 'form-control'}), label='Habitos Alimentares')
    coposAguaDia = IntegerField(widget=TextInput(attrs={'class': 'form-control'}), label='Copos de Água por Dia')
    banhosDia = IntegerField(widget=TextInput(attrs={'class': 'form-control'}), label='Quantidade de Banhos por Dia')
    horasSono = IntegerField(widget=TextInput(attrs={'class': 'form-control'}), label='Quantidade de Horas de Sono por Dia')
    etilismo = ChoiceField(widget=RadioSelect, choices=etilismo, label='Etilismo')
    tabagismo = ChoiceField(widget=RadioSelect, choices=tabagismo, label='Tabagismo')
    alergiaTopica = ChoiceField(widget=RadioSelect, choices=alergiaTopica, label='Alergia Tópica')
    atividadeDomesticaPorDia = CharField(widget=TextInput(attrs={'class': 'form-control'}), label='Atividade Domestica por Dia')

    class Meta:
        model = HabitosPessoais
        fields = ['numeroRefeicoesDia', 'habitosAlimentares','coposAguaDia', 'banhosDia', 'horasSono', 'etilismo',
                  'tabagismo', 'alergiaTopica', 'atividadeDomesticaPorDia']


odor = (
    ('S', 'Sim'), ('N', 'Não'),
)

perdaTecidual = (
    ('S', 'Sim'), ('N', 'Não'),
)

sensibilidade = (
    ('S', 'Sim'), ('N', 'Não'),
)

zonaPeDireito = (
    ('S', 'Sim'), ('N', 'Não'),
)

zonaPeEsquerdo = (
    ('S', 'Sim'), ('N', 'Não'),
)

class ObservacaoForm(MultipleForm):
    localizacaoUlcera = CharField(widget=TextInput(attrs={'class': 'form-control'}), label='Localização da Úlcera')
    condicaoPele = CharField(widget=TextInput(attrs={'class': 'form-control'}), label='Condição da Pele')
    condicaoBordas = CharField(widget=TextInput(attrs={'class': 'form-control'}), label='Condição da Borda')
    condicaoLeito = CharField(widget=TextInput(attrs={'class': 'form-control'}), label='Condição Leito')
    percentualLeito = FloatField(widget=TextInput(attrs={'class': 'form-control'}), label='Percentual do Leito')
    tipoExsudato = CharField(widget=TextInput(attrs={'class': 'form-control'}), label='Tido de Exsudato')
    quantidade = CharField(widget=TextInput(attrs={'class': 'form-control'}), label='Quantidade **')
    odor = ChoiceField(widget=RadioSelect, choices=odor, label='Odor')
    perdaTecidual = ChoiceField(widget=RadioSelect, choices=perdaTecidual, label='Perda Tecidual')
    maiorExtensaoVertical = FloatField(widget=TextInput(attrs={'class': 'form-control'}), label='Maior Extensão Vertical')
    maiorExtensaoHorizontal = CharField(widget=TextInput(attrs={'class': 'form-control'}), label='Maior Extensão Horizontal')
    profundidade = FloatField(widget=TextInput(attrs={'class': 'form-control'}), label='Profundidade da Úlcera')
    maiorProfundidade = FloatField(widget=TextInput(attrs={'class': 'form-control'}), label='Maior Profundidade da Úlcera')
    sensibilidade = ChoiceField(widget=RadioSelect, choices=sensibilidade, label='Sensibilidade')
    zonaPeDireito = ChoiceField(widget=RadioSelect, choices=zonaPeDireito, label='Zona do Pé Direito')
    zonaPeEsquerdo = ChoiceField(widget=RadioSelect, choices=zonaPeEsquerdo, label='Zona do Pé Esquerdo')
    temperatura = FloatField(widget=TextInput(attrs={'class': 'form-control'}), label='Temperatura')
    parestesia = CharField(widget=TextInput(attrs={'class': 'form-control'}), label='Parestesia')
    hipoestesia = CharField(widget=TextInput(attrs={'class': 'form-control'}), label='Hipoestesia')
    pulsoPedioso = CharField(widget=TextInput(attrs={'class': 'form-control'}), label='Pulso Pedioso')
    pulsoPopliteo = CharField(widget=TextInput(attrs={'class': 'form-control'}), label='Pulso Popliteo')
    pulsoFemoral = CharField(widget=TextInput(attrs={'class': 'form-control'}), label='Pulso Femoral')
    tibiaPosterior = CharField(widget=TextInput(attrs={'class': 'form-control'}), label='Tibia Posterior')
    sinaisDeInfeccao = CharField(widget=TextInput(attrs={'class': 'form-control'}), label='Sinais de Infecção')

    class Meta:
        model = Observacao
        fields = ['localizacaoUlcera', 'condicaoPele', 'condicaoBordas', 'condicaoLeito', 'percentualLeito',
                  'tipoExsudato', 'quantidade', 'odor', 'perdaTecidual', 'maiorExtensaoVertical', 'maiorExtensaoHorizontal',
                  'profundidade', 'maiorProfundidade', 'sensibilidade', 'zonaPeDireito', 'zonaPeEsquerdo', 'temperatura',
                  'parestesia', 'hipoestesia', 'pulsoPedioso', 'pulsoPopliteo', 'pulsoFemoral', 'tibiaPosterior', 'sinaisDeInfeccao']


internacao = (
    ('S', 'Sim'), ('N', 'Não'),
)

culturaSecrecao = (
    ('S', 'Sim'), ('N', 'Não'),
)

interrupcaoTratamento = (
    ('S', 'Sim'), ('N', 'Não'),   
)

class AnamneseForm(MultipleForm):
    peso = FloatField(widget=TextInput(attrs={'class': 'form-control'}), label='Peso')
    altura = FloatField(widget=TextInput(attrs={'class': 'form-control'}), label='Altura')
    antecedentesPessoais = CharField(widget=TextInput(attrs={'class': 'form-control'}), label='Antecedentes Pessoais')
    medicamentosEmUso =  CharField(widget=TextInput(attrs={'class': 'form-control'}), label='Medicamentos em uso')
    historiaUlcera = CharField(widget=TextInput(attrs={'class': 'form-control'}), label='Historia da Ulcera')
    inicioPrimeiraUlcera = CharField(widget=TextInput(attrs={'class': 'form-control'}), label='Inicio da Primeira Ulcera')
    fechamentoUlcera = CharField(widget=TextInput(attrs={'class': 'form-control'}), label='Fechamento da Ulcera')
    ulceraAtual = CharField(widget=TextInput(attrs={'class': 'form-control'}), label='Ulcera Atual')
    presencaDor = CharField(widget=TextInput(attrs={'class': 'form-control'}), label='Presença de Dor')
    alivioDor = CharField(widget=TextInput(attrs={'class': 'form-control'}), label='Alivio da Dor')
    tempoTratamento = CharField(widget=TextInput(attrs={'class': 'form-control'}), label='Tempo de Tratamento')
    localTratamento = CharField(widget=TextInput(attrs={'class': 'form-control'}), label='Local de Tratamento')
    frequenciaTrocaCurativos = CharField(widget=TextInput(attrs={'class': 'form-control'}), label='Frequência de Troca de Curativos')
    trocaCurativoFinalDeSemana = CharField(widget=TextInput(attrs={'class': 'form-control'}), label='Frequência de Troca de Curativos no Final de Semana')
    interrupcaoTratamento = ChoiceField(widget=RadioSelect, choices=interrupcaoTratamento, label='Interrupção do Tratamento')
    motivoInterrupcao = CharField(widget=TextInput(attrs={'class': 'form-control'}), label='Motivo da Interrupção')
    terapiaCompressiva = CharField(widget=TextInput(attrs={'class': 'form-control'}), label='Terapia Compressiva')
    cirurgiaVarize = CharField(widget=TextInput(attrs={'class': 'form-control'}), label='Cirurgia de Varize')
    profissionalAcompanhante = CharField(widget=TextInput(attrs={'class': 'form-control'}), label='Profissional Acompanhante')
    acessoCef = CharField(widget=TextInput(attrs={'class': 'form-control'}), label='Acesso ao CEF')
    internacao = ChoiceField(widget=RadioSelect, choices=internacao, label='Internação')
    culturaSecrecao = ChoiceField(widget=RadioSelect, choices=culturaSecrecao, label='Cultura de Secreção')

    class Meta:
        model = Anamnese
        fields = ['peso', 'altura', 'antecedentesPessoais', 'medicamentosEmUso', 'historiaUlcera', 'inicioPrimeiraUlcera',
                'fechamentoUlcera', 'ulceraAtual', 'presencaDor', 'alivioDor', 'tempoTratamento', 'localTratamento', 'frequenciaTrocaCurativos',
                'interrupcaoTratamento', 'motivoInterrupcao', 'terapiaCompressiva', 'cirurgiaVarize', 'profissionalAcompanhante', 'acessoCef',
                'internacao', 'culturaSecrecao']
    

escolhaSexo = (
    ('F', 'Feminino'), ('M', 'Masculino'),
)

class PacienteForm(MultipleForm):
    nomeCompleto = CharField(widget=TextInput(attrs={'class': 'form-control'}), label='Nome Completo')
    cpf = CharField(widget=TextInput(attrs={'class': 'form-control'}), label='CPF')
    sexo = ChoiceField(widget=RadioSelect, choices=escolhaSexo, label='Sexo')
    dataNascimento = DateField(widget=DateInput(attrs={'class': 'form-control'}, format='%d/%m/%Y'), input_formats=('%d/%m/%Y',), label='Data de Nascimento')
    idade = IntegerField(widget=TextInput(attrs={'class': 'form-control'}), label='Idade')
    estadoCivil = CharField(widget=TextInput(attrs={'class': 'form-control'}), label='Estado Civil')
    numeroFilhos = IntegerField(widget=TextInput(attrs={'class': 'form-control'}), label='Numero De Filhos')
    religiao = CharField(widget=TextInput(attrs={'class': 'form-control'}), label='Religião')
    escolaridade = CharField(widget=TextInput(attrs={'class': 'form-control'}), label='Escolaridade')
    profissao = CharField(widget=TextInput(attrs={'class': 'form-control'}), label='Profissão')
    rendaFamiliar = FloatField(widget=TextInput(attrs={'class': 'form-control'}), label='Renda Familiar')
    habilitacao = CharField(widget=TextInput(attrs={'class': 'form-control'}), label='Habilitação')
    condicaoSaneamento = CharField(widget=TextInput(attrs={'class': 'form-control'}), label='Condição de Saneamento')

    class Meta:
        model = Paciente
        fields = ['nomeCompleto', 'cpf', 'sexo', 'dataNascimento', 'idade', 'estadoCivil', 'numeroFilhos', 'religiao',
        'escolaridade', 'profissao', 'rendaFamiliar', 'habilitacao', 'condicaoSaneamento']


class FeridaForm(ModelForm):
    paciente = ModelChoiceField(queryset=Paciente.objects.all())
    apelido = CharField(widget=TextInput(attrs={'class': 'form-control'}), label='Apelido')

    class Meta:
        model = Ferida
        fields = ['paciente', 'apelido']


class CaracteristicaFeridaForm(ModelForm):
    area = FloatField(widget=TextInput(attrs={'class': 'form-control'}), label='Area da ferida')
    cor = CharField(widget=TextInput(attrs={'class': 'form-control'}), label='Cor da Ferida')

    class Meta:
        model = CaracteristicaFerida
        fields = ['area', 'cor']


imagemAnalisada = (
    ('S', 'Sim'), ('N', 'Não'),
)

class AtendimentoForm(ModelForm):
    #profissional = ModelChoiceField(queryset=Profissional.objects.all())
    #ferida = ModelChoiceField(queryset=Ferida.objects.all())
    #caracteristica = ModelChoiceField(queryset=CaracteristicaFerida.objects.all())
    #tecnica = ModelChoiceField(queryset=Tecnica.objects.all())
    #dataHora = DateTimeField(auto_now=False, auto_now_add=False)
    nota = CharField(widget=TextInput(attrs={'class': 'form-control'}), label='Nota')
    imagemAnalisada = ChoiceField(widget=RadioSelect, choices=imagemAnalisada, label='Imagem Analisada')

    class Meta:
        model = Atendimento
        fields = ['nota', 'imagemAnalisada']


class LoginForm(auth_forms.AuthenticationForm):
    username = CharField(widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Usuário'}))
    password = CharField(widget=PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Senha'}))

    class Meta:
        model = auth_models.User
        fields = ['username', 'password']


class ResetForm(ModelForm):
    class Meta:
        model = Profissional
        fields = ['email']

