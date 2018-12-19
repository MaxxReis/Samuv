from rest_framework import serializers
from samuv_site import models
from django.contrib.auth.models import User
from samuv_web import settings


class ProfissionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Profissional
        fields = ('__all__')
        depth = 1


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')
        depth = 1


class ClinicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Clinica
        fields = ('__all__')
        depth = 1


class ClinicaProfissionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ClinicaProfissional
        fields = ('__all__')
        depth = 1


class TecnicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tecnica
        fields = ('pk', 'nome')
        depth = 1


class AnamneseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Anamnese
        fields = ('__all__')
        depth = 1


class PacienteSerializer(serializers.ModelSerializer):
    #dataNascimento = serializers.DateTimeField(format=settings.DATE_FORMAT)

    class Meta:
        model = models.Paciente
        fields = ('__all__')
        depth = 1


class PacientePorIdSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Paciente
        fields = ('__all__')
        depth = 1


class DoencaSerializer(serializers.ModelSerializer):
    #paciente = PacienteSerializer()

    class Meta:
        model = models.Doenca
        fields = ('__all__')
        depth = 1


class DoencaPacienteSerializer(serializers.ModelSerializer):
    paciente = PacienteSerializer()
    doenca = DoencaSerializer()

    class Meta:
        model = models.DoencaPaciente
        fields = ('__all__')
        depth = 1


class FeridaSerializer(serializers.ModelSerializer):
    doencaPaciente = DoencaPacienteSerializer()

    class Meta:
        model = models.Ferida
        fields = ('__all__')
        depth = 1


class CaracteristicaFeridaSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.CaracteristicaFerida
        fields = ('id', 'area', 'cor',)
        depth = 1


class AgendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Agenda
        fields = ('__all__')
        depth = 1


class NoticiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Noticia
        fields = ('__all__')
        depth = 1


class AtendimentoSerializer(serializers.ModelSerializer):
    doencaPaciente = DoencaPacienteSerializer()
    clinicaProfissional = ClinicaProfissionalSerializer()
    agenda = AgendaSerializer()
    noticia = NoticiaSerializer()
    dataHora = serializers.DateTimeField(format=settings.DATETIME_FORMAT)

    class Meta:
        model = models.Atendimento
        fields = ('__all__')
        depth = 1


class AtendimentoTecnicaSerializer(serializers.ModelSerializer):
    tecnica = TecnicaSerializer()
    atendimento = AtendimentoSerializer()

    class Meta:
        model = models.AtendimentoTecnica
        fields = ('id', 'atendimento', 'tecnica')
        depth = 1


class AtendimentoExtraSerializer(serializers.ModelSerializer):
    atendimento = AtendimentoSerializer()
    ferida = FeridaSerializer()
    caracteristicaFerida = CaracteristicaFeridaSerializer()

    class Meta:
        model = models.AtendimentoExtra
        fields = ('__all__')
        depth = 1


class ImagemSerializer(serializers.HyperlinkedModelSerializer):
    atendimento = AtendimentoSerializer()

    class Meta:
        model = models.Imagem
        fields = ('id', 'imageName', 'atendimento', 'foto', 'segmented_image')
        depth = 1


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Imagem
        fields = '__all__'
