import os
from django.db import models
from datetime import datetime
from django import forms

from django.dispatch import receiver
from django.utils import timezone
#from multiselectfield import MultiSelectField

class Clinica(models.Model):
    nome = models.CharField(max_length=250, blank=False, null=False, default="")
    endereco = models.CharField(max_length=250, blank=False, null=False, default="")
    
    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Clinica"
        verbose_name_plural = "Clinicas"


class Profissional(models.Model):
    idProfissional = models.AutoField('auth.User', primary_key=True, blank=False, null=False)
    nomeProfissional = models.CharField(max_length=250, blank=True, null=True, default="")
    login = models.CharField(max_length=20, unique=True, blank=False, null=False, default="")
    email = models.EmailField()
    senha = models.CharField(max_length=20, blank=False, null=False, default="")

    def __str__(self):
        return self.nomeProfissional

    class Meta:
        verbose_name = "Profissional"
        verbose_name_plural = "Profissionais"


class ClinicaProfissional(models.Model):
    clinica = models.ForeignKey(Clinica, on_delete=models.CASCADE, default="")
    profissional = models.ForeignKey(Profissional, on_delete=models.CASCADE, default="")

    class Meta:
        verbose_name = "Clinica_X_Profissional"
        verbose_name_plural = "Clinicas_X_Profissionais"


class Anamnese(models.Model):
    peso = models.FloatField(default=0)
    altura = models.FloatField(default=0)
    antecedentesPessoais = models.CharField(max_length=250, blank=False, null=False, default="")
    medicamentosEmUso = models.CharField(max_length=250, blank=False, null=False, default="")
    historiaUlcera = models.CharField(max_length=250, blank=False, null=False, default="")
    inicioPrimeiraUlcera = models.CharField(max_length=250, blank=False, null=False, default="")
    fechamentoUlcera = models.CharField(max_length=250, blank=False, null=False, default="")
    ulceraAtual = models.CharField(max_length=250, blank=False, null=False, default="")
    presencaDeDor = models.CharField(max_length=250, blank=False, null=False, default="")
    alivioDaDor = models.CharField(max_length=250, blank=False, null=False, default="")
    tempoTratamento = models.CharField(max_length=250, blank=False, null=False, default="")
    localTratamento = models.CharField(max_length=250, blank=False, null=False, default="")
    frequenciaTrocaCurativos = models.CharField(max_length=250, blank=False, null=False, default="")
    trocaCurativosFinalDeSemana = models.CharField(max_length=250, blank=False, null=False, default="")
    interrupcaoTratamento = models.CharField(max_length=250)
    motivoInterrupcao = models.CharField(max_length=250, blank=False, null=False, default="")
    terapiaCompressiva = models.CharField(max_length=250, blank=False, null=False, default="")
    cirurgiaVarize = models.CharField(max_length=250, blank=False, null=False, default="")
    profissionalAcompanhante = models.CharField(max_length=250, blank=False, null=False, default="")
    acessoCef = models.CharField(max_length=250, blank=False, null=False, default="")
    internacao = models.CharField(max_length=250)
    culturaSecrecao = models.CharField(max_length=250)

    def __str__(self):
        return self.profissionalAcompanhante

    class Meta:
        verbose_name = "Anamnese"
        verbose_name_plural = "Anamneses"


class Observacao(models.Model):
    localizacaoUlcera = models.CharField(max_length=250, blank=False, null=False)
    condicaoPele = models.CharField(max_length=250, blank=False, null=False, default="")
    condicaoBordas = models.CharField(max_length=250, blank=False, null=False, default="")
    condicaoLeito = models.CharField(max_length=250, blank=False, null=False, default="")
    percentualLeito = models.FloatField(default=0)
    tipoExsudato = models.CharField(max_length=250, blank=False, null=False, default="")
    quantidade = models.IntegerField(default=0)
    odor = models.CharField(max_length=250, blank=False, null=False, default="")
    perdaTecidual = models.CharField(max_length=250, blank=False, null=False, default="")
    maiorExtensaoVertical = models.CharField(max_length=250, blank=False, null=False, default="")
    maiorExtensaoHorizontal = models.CharField(max_length=250, blank=False, null=False, default="")
    profundidade = models.FloatField(default=0)
    maiorProfundidade = models.FloatField(default=0)
    sensibilidade = models.CharField(max_length=250, blank=False, null=False, default="")
    zonaPeDireito = models.CharField(max_length=250, blank=False, null=False, default="")
    zonaPeEsquerdo = models.CharField(max_length=250, blank=False, null=False, default="")
    temperatura = models.FloatField(default=0)
    parestesia = models.CharField(max_length=250, blank=False, null=False, default="")
    hipoestesia = models.CharField(max_length=250, blank=False, null=False, default="")
    pulsoPedioso = models.CharField(max_length=250, blank=False, null=False, default="")
    pulsoPopliteo = models.CharField(max_length=250, blank=False, null=False, default="")
    pulsoFemoral = models.CharField(max_length=250, blank=False, null=False, default="")
    tibiaPosterior = models.CharField(max_length=250, blank=False, null=False, default="")
    sinaisDeInfeccao = models.CharField(max_length=250, blank=False, null=False, default="")

    def __str__(self):
        return self.localizacaoUlcera

    class Meta:
        verbose_name = "Oberservação"
        verbose_name_plural = "Observações"


class HabitosPessoais(models.Model):
    numeroRefeicoesDia = models.IntegerField(default=0)
    habitosAlimentares = models.CharField(max_length=250, blank=False, null=False, default="")
    coposAguaDia = models.IntegerField(default=0)
    banhosDia = models.IntegerField(default=0)
    horasSono = models.IntegerField(default=0)
    etilismo = models.CharField(max_length=250, blank=False, null=False, default="")
    tabagismo = models.CharField(max_length=250, blank=False, null=False, default="")
    alergiaTopica = models.CharField(max_length=250, blank=False, null=False, default="")
    atividadeDomesticaPorDia = models.CharField(max_length=250, blank=False, null=False, default="")

    def __str__(self):
        return self.habitosAlimentares

    class Meta:
        verbose_name = "Hábito Pessoal"
        verbose_name_plural = "Hábitos Pessoais"


class Clinico(models.Model):
    diagnosticoUsuario = models.CharField(max_length=250, blank=False, null=False, default="")
    diagnosticoEquipe = models.CharField(max_length=250, blank=False, null=False)
    diagnosticoPesquisadora = models.CharField(max_length=250, blank=False, null=False)
    resultadoExames = models.CharField(max_length=250, blank=False, null=False)

    def __str__(self):
        return self.resultadoExames

    class Meta:
        verbose_name = "Resultado Clinico"
        verbose_name_plural = "Resultados Clinicos"


class Paciente(models.Model):
    nomeCompleto = models.CharField(max_length=250, blank=False, null=False)
    sexo = models.CharField(max_length=250)
    dataNascimento = models.DateField(null=False, blank=False)
    dataCadastro = models.DateTimeField(null=False, blank=False, default=timezone.now)
    cpf = models.CharField(unique=True, max_length=14, null=True, blank=True)
    foto = models.ImageField(upload_to='imagens/', null=True, blank=True)
    idade = models.IntegerField()
    estadoCivil = models.CharField(max_length=250, blank=False, null=False, default="")
    numeroFilhos = models.IntegerField(default=0)
    religiao = models.CharField(max_length=250, blank=False, null=False, default="")
    escolaridade = models.CharField(max_length=250, blank=False, null=False, default="")
    profissao = models.CharField(max_length=250, blank=False, null=False, default="")
    rendaFamiliar = models.FloatField(default=0)
    habilitacao = models.CharField(max_length=250, blank=False, null=False, default="")
    condicaoSaneamento = models.CharField(max_length=250, blank=False, null=False, default="")
    anamnese = models.ForeignKey(Anamnese, on_delete=models.CASCADE, blank=True, null=True, default="")
    observacao = models.ForeignKey(Observacao, on_delete=models.CASCADE, blank=True, null=True, default="")
    clinico = models.ForeignKey(Clinico, on_delete=models.CASCADE, blank=True, null=True, default="")
    habitosPessoais = models.ForeignKey(HabitosPessoais, on_delete=models.CASCADE, blank=True, null=True, default="")

    def __str__(self):
        return self.nomeCompleto

    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"

    def clean_cpf(self):
        if hasattr(self.instance, 'cpf') and self.cleaned_data.get('cpf'):
            try:
                func = Paciente.objects.get(
                    cpf=self.cleaned_data.get('cpf'))
                if hasattr(self.instance, 'id') and self.instance.id:
                    if self.instance.id == func.id:
                        raise Paciente.DoesNotExist
                raise forms.ValidationError(
                    u'CPF pertence ao paciente {}'.format(
                        func.__str__()))
            except Paciente.DoesNotExist:
                return self.cleaned_data.get('cpf')
        return self.cleaned_data.get('cpf')


class Doenca(models.Model):
    nome = models.CharField(max_length=250, blank=False, null=False, default="")
    cid = models.IntegerField(default="")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Doença"
        verbose_name_plural = "Doenças"


class DoencaPaciente(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, default="")
    doenca = models.ForeignKey(Doenca, on_delete=models.CASCADE, default="")

    def __str__(self):
        return self.paciente.nomeCompleto + ' Doença: ' + self.doenca.nome

    class Meta:
        verbose_name = "Doença_X_Paciente"
        verbose_name_plural = "Doenças_X_Pacientes"



class Ferida(models.Model):
    doencaPaciente = models.ForeignKey(DoencaPaciente, on_delete=models.CASCADE, default="")
    apelido = models.CharField(max_length=20, blank=True, null=False)

    def __str__(self):
        return self.apelido

    class Meta:
        verbose_name = "Ferida"
        verbose_name_plural = "Feridas"



class CaracteristicaFerida(models.Model):
    area = models.FloatField(blank=True, null=True)
    cor = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        verbose_name = "Característica da ferida"
        verbose_name_plural = "Características das feridas"


class Tecnica(models.Model):
    nome = models.CharField(max_length=50, blank=True, null=False)
    descricao = models.CharField(max_length=50, blank=True, null=False, default="")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Técnica"
        verbose_name_plural = "Técnicas"


class Agenda(models.Model):
    nota = models.CharField(max_length=250, blank=True, null=True)
    dataAgenda = models.DateField(null=False, blank=False)

    def __str__(self):
        return self.nota

    class Meta:
        verbose_name = "Agenda"
        verbose_name_plural = "Agendas"


class Noticia(models.Model):
    informacao = models.CharField(max_length=250, blank=True, null=True)
    dataNoticia = models.DateField(null=False, blank=False)    

    def __str__(self):
        return self.informacao

    class Meta:
        verbose_name = "Noticia"
        verbose_name_plural = "Noticias"


class Atendimento(models.Model):
    dataHora = models.DateTimeField(null=False, blank=False, default=timezone.now)
    nota = models.CharField(max_length=250, blank=True, null=True)
    imagemAnalisada = models.CharField(max_length=250, blank=True, null=True)
    doencaPaciente = models.ForeignKey(DoencaPaciente, on_delete=models.CASCADE, )
    clinicaProfissional = models.ForeignKey(ClinicaProfissional, on_delete=models.CASCADE,)
    agenda = models.ForeignKey(Agenda, on_delete=models.CASCADE, )
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE, )

    #def __str__(self):
     #   return str(self.pk) + ' - ' + self.profissional.usuario.nomeUsuario + ', ' + str(
      #      self.dataHora.strftime("%d/%m/%Y %I:%M:%S"))
    def __str__(self):
        return self.nota

    class Meta:
        verbose_name = "Atendimento"
        verbose_name_plural = "Atendimentos"


class AtendimentoTecnica(models.Model):
    atendimento = models.ForeignKey(Atendimento, on_delete=models.CASCADE, )
    tecnica = models.ForeignKey(Tecnica, on_delete=models.CASCADE, )

    class Meta:
        verbose_name = "Técnica_X_Atendimento"
        verbose_name_plural = "Técnicas_X_Atendimentos"


class AtendimentoExtra(models.Model):
    atendimento = models.ForeignKey(Atendimento, blank=True, null=True, on_delete=models.CASCADE, )
    ferida = models.ForeignKey(Ferida, blank=True, null=True, on_delete=models.CASCADE, )
    caracteristicaFerida = models.ForeignKey(CaracteristicaFerida, blank=True, null=True, on_delete=models.CASCADE, )

    class Meta:
        verbose_name = "Atendimento_X_Extra"
        verbose_name_plural = "Atendimentos_X_Extras"


class Imagem(models.Model):
    atendimento = models.ForeignKey(Atendimento, on_delete=models.CASCADE, null=False)
    imageName = models.CharField(max_length=80, default='IMG' + datetime.now().strftime("%d%m%Y%I%M%S"))
    foto = models.ImageField(upload_to='imagens/')
    segmented_image = models.ImageField(upload_to='imagens_segmentadas/', blank=True, null=True)

    def __str__(self):
        return self.imageName

    class Meta:
        verbose_name = "Imagem"
        verbose_name_plural = "Imagens"


@receiver(models.signals.pre_save, sender=Imagem)
def auto_delete_file_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False

    atendimento = Atendimento.objects.get(pk=instance.atendimento.pk)
    atendimento.imagemAnalisada = False
    atendimento.save()

    old_file = Imagem.objects.get(pk=instance.pk).segmented_image
    try:
        if os.path.isfile(old_file.path.replace('\\', '/')):
            os.remove(old_file)
        return True
    except:
        return False


