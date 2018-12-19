import pytz
import json
from datetime import datetime
from api_rest import serializers
from django.db import transaction
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from samuv_analise import views as analise_views
from samuv_site import models


# LOGIN NO SISTEMA
class LoginServiceView(APIView):

    def post(self, request, format=None):
        userName = request.data.get('login')
        password = request.data.get('senha')
        if "@" in userName:
            user = models.Profissional.objects.get(email=userName, senha=password)
        if "@" not in userName:
            user = models.Profissional.objects.get(login=userName, senha=password)

        if user != None:
            profissional = models.Profissional.objects.get(nomeProfissional=user)
            serializer = serializers.ProfissionalSerializer(profissional)

        return Response(serializer.data)


# MÉTODOS DE ACESSO AOS MODELS
"""
class UsuarioList(generics.ListCreateAPIView):
    queryset = models.Usuario.objects.all()
    serializer_class = serializers.UsuarioSerializer


class UsuarioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Usuario.objects.all()
    serializer_class = serializers.UsuarioSerializer
"""

class AnamneseDetail(generics.ListCreateAPIView):
    queryset = models.Anamnese.objects.all()
    serializer_class = serializers.AnamneseSerializer


class AnamneseList(generics.ListCreateAPIView):
    queryset = models.Anamnese.objects.all()
    serializer_class = serializers.AnamneseSerializer


class PacienteList(generics.ListCreateAPIView):
    queryset = models.Paciente.objects.all()
    serializer_class = serializers.PacienteSerializer


class PacienteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Paciente.objects.all()
    serializer_class = serializers.PacienteSerializer


class ProfissionalList(generics.ListCreateAPIView):
    queryset = models.Profissional.objects.all()
    serializer_class = serializers.ProfissionalSerializer


class ProfissionalDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Profissional.objects.all()
    serializer_class = serializers.ProfissionalSerializer


class FeridaList(generics.ListCreateAPIView):
    queryset = models.Ferida.objects.all()
    serializer_class = serializers.FeridaSerializer


class FeridaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Ferida.objects.all()
    serializer_class = serializers.FeridaSerializer


class CadastrarFeridaServiceView(APIView):

    def post(self, request, format=None):
        if request.data.get('paciente_id') == None:
            return "Paciente é obrigatório!"

        if request.data.get('apelido') == None:
            return "Apelido é obrigatório!"

        Apelido = request.data.get('apelido')
        Paciente = models.Paciente.objects.get(pk=request.data.get('paciente_id'))

        ferida = models.Ferida.objects.create(paciente=Paciente, apelido=Apelido)

        serializer = serializers.FeridaSerializer(ferida)
        return Response(serializer.data)


class AtualizarFeridaServiceView(APIView):

    def post(self, request, format=None):
        if request.data.get('ferida_id') == None:
            return "Ferida é obrigatória!"

        if request.data.get('paciente_id') == None:
            return "Paciente é obrigatório!"

        if request.data.get('apelido') == None:
            return "Apelido é obrigatório!"

        Apelido = request.data.get('apelido')
        Paciente = models.Paciente.objects.get(pk=request.data.get('paciente_id'))

        ferida = models.Ferida.objects.get(pk=request.data.get('ferida_id'))
        ferida.apelido = Apelido
        ferida.paciente = Paciente

        ferida.save()

        serializer = serializers.FeridaSerializer(ferida)
        return Response(serializer.data)


class TecnicaList(generics.ListCreateAPIView):
    queryset = models.Tecnica.objects.all()
    serializer_class = serializers.TecnicaSerializer


class TecnicaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Tecnica.objects.all()
    serializer_class = serializers.TecnicaSerializer


class DoencaList(generics.ListCreateAPIView):
    queryset = models.Doenca.objects.all()
    serializer_class = serializers.DoencaSerializer

class DoencaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Doenca.objects.all()
    serializer_class = serializers.DoencaSerializer


class DoencaPacienteList(generics.ListCreateAPIView):
    queryset = models.DoencaPaciente.objects.all()
    serializer_class = serializers.DoencaPacienteSerializer


class DoencaPacienteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.DoencaPaciente.objects.all()
    serializer_class = serializers.DoencaPacienteSerializer


class AtendimentoList(generics.ListCreateAPIView):
    queryset = models.Atendimento.objects.all()
    serializer_class = serializers.AtendimentoSerializer


class AtendimentoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Atendimento.objects.all()
    serializer_class = serializers.AtendimentoSerializer


class AgendaList(generics.ListCreateAPIView):
    queryset = models.Agenda.objects.all()
    serializer_class = serializers.AgendaSerializer


class AgendaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Agenda.objects.all()
    serializer_class = serializers.AgendaSerializer


class AtendimentoExtraList(generics.ListCreateAPIView):
    queryset = models.AtendimentoExtra.objects.all()
    serializer_class = serializers.AtendimentoExtraSerializer

class AtendimentoExtraDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.AtendimentoExtra.objects.all()
    serializer_class = serializers.AtendimentoExtraSerializer



# INFORMAÇÕES PARA O MOBILE
class ProfissionalPorUsuarioServiceView(APIView):

    def get(self, request, usuario_id, format=None):
        user = models.Usuario.objects.get(idUsuario=usuario_id)
        profissional = models.Profissional.objects.get(usuario=user)
        serializer = serializers.ProfissionalSerializer(profissional)
        return Response(serializer.data)


class FeridasPorPacienteServiceView(APIView):

    def post(self, request, format=None):
        paciente_selecionado = models.Paciente.objects.get(pk=request.data.get('paciente_id'))
        feridas = models.Ferida.objects.filter(paciente=paciente_selecionado)

        serializer = serializers.FeridaSerializer(feridas, many=True)
        return Response(serializer.data)



class AtendimentosPorFeridaServiceView(APIView):

    def post(self, request, format=None):
        ferida_selecionada = models.Ferida.objects.get(pk=request.data.get('ferida_id'))
        atendimentos = models.Atendimento.objects.filter(ferida=ferida_selecionada)

        serializer = serializers.AtendimentoSerializer(atendimentos, many=True)
        return Response(serializer.data)


#to do
class AtendimentosPorPacienteServiceView(APIView):

    def get(self, request):
        atendimento = models.Atendimento.objects.get(pk=request.data.get('atendimento_id'))
        serializer = serializers.AtendimentoSerializer(atendimento)
        return Response(serializer.data)


#to do
class PacientePorIdServiceView(APIView):

    def get(self, request):
        paciente = models.Paciente.objects.get(pk=request.data.get('paciente_id'))
        serializer = serializers.PacientePorIdServiceView(paciente)
        return Response(serializer.data)


class ImagemPorAtendimentoServiceView(APIView):

    def get(self, request, atendimento_id, format=None):
        image = models.Imagem.objects.get(atendimento=atendimento_id)
        serializer = serializers.ImagemSerializer(image)
        return Response(serializer.data)


class TecnicasPorAtendimentoServiceView(APIView):

    def get(self, request, atendimento_id, format=None):
        AtendimentosTecnicas = models.AtendimentoTecnica.objects.filter(atendimento=atendimento_id)

        tecnicas = []
        for cursor in AtendimentosTecnicas:
            tecnicas.append(cursor.tecnica)

        serializer = serializers.TecnicaSerializer(tecnicas, many=True)
        return Response(serializer.data)


class IniciarAtendimentoServiceView(APIView):

    def post(self, request, format=None):
        Profissional = models.Profissional.objects.get(id=request.data.get('profissional_id'))
        Ferida = models.Ferida.objects.get(pk=request.data.get('ferida_id'))
        Descricao = request.data.get('descricao')

        now = datetime.utcnow().replace(tzinfo=pytz.UTC)

        novoAtendimento = models.Atendimento.objects.create(profissional=Profissional, ferida=Ferida,
                                                            dataHora=now, nota=Descricao)

        imageName = request.data.get('imageName')
        foto = request.FILES['foto']
        imagem = models.Imagem.objects.create(atendimento=novoAtendimento, imageName=imageName, foto=foto)
        imagem.save()

        tecnicasJson = json.loads(request.data.get('tecnicas'))
        for tec in tecnicasJson:
            id = int(tec['pk'])
            Tecnica = models.Tecnica.objects.get(pk=id)
            AtendimentoTecnica = models.AtendimentoTecnica.objects.create(atendimento=novoAtendimento, tecnica=Tecnica)
            AtendimentoTecnica.save()

        serializer = serializers.AtendimentoSerializer(novoAtendimento)
        return Response(serializer.data)


class AtendimentosPorPacienteServiceView(APIView):
    def get(self, request, pk):
        atendimentos = models.Atendimento.objects.filter(ferida__paciente__id=pk).all()
        serializer = serializers.AtendimentoSerializer(atendimentos, many=True)
        return Response(serializer.data, 200)


class AtendimentoDetail(APIView):
    def get(self, request):
        queryset = models.Atendimento.objects.all()
        serializer = serializers.AtendimentoSerializer(queryset, many=True)
        return Response(serializer.data, 200)


class PacientesComAtendimentoServiceView(APIView):
    def get(self, request):
        atendimentos = models.Atendimento.objects.all()
        pacientes_list = []
        for a in atendimentos:
            if a.ferida.paciente not in pacientes_list:
                p = models.Paciente.objects.get(id=a.ferida.paciente.pk)
                pacientes_list.append(p)
        serializer = serializers.PacienteSerializer(pacientes_list, many=True)
        return Response(serializer.data)


#class DoencaPacienteDetail(APIView):
 #   def get(self, request):
  #      queryset = models.DoencaPaciente.objects.all()
   #     serializer = serializers.DoencaPacienteSerializer(queryset, many=True)
    #    return Response(serializer.data)


# MÉTODOS DA ANÁLISE DE IMAGENS
class ImagemCadastradaBase64ServiceView(APIView):
    def post(self, request):
        imagem = models.Imagem.objects.filter(atendimento__pk=request.data.get("pk")).first()
        imageBase64 = analise_views.convertImageBase64(imagem.foto)
        return Response(imageBase64)


class ImagemSegmentadaBase64ServiceView(APIView):
    def post(self, request):
        atendimento = models.Atendimento.objects.get(id=request.data.get("pk"))
        imagem = models.Imagem.objects.filter(atendimento=atendimento).first()
        imageBase64 = str(analise_views.convertImageBase64(imagem.segmented_image)["img64"])[2:-1]
        imageBase64 = "data:image/png;base64, " + imageBase64
        area = atendimento.caracteristica.area

        return Response([{"img64": str(imageBase64)}, {"area", area}])


class AnalisarImagemBase64ServiceView(APIView):
    def post(self, request):
        image_data = request.data.get("imagem")
        atendimentoId = request.data.get("atendimentoId")

        # ARMAZENAR IMAGEM SEGMENTADA
        imagem = models.Imagem.objects.filter(atendimento__pk=atendimentoId).first()
        new_segmented_img_url = analise_views.SegmentarImagem(image_data, imagem)
        imagem.segmented_image = new_segmented_img_url
        imagem.save()

        # ANALISAR IMAGEM SEGMENTADA
        imagem_original_url = str(imagem.foto.file).replace('\\', '/')
        analise = analise_views.AnalisarImagem(imagem_original_url, imagem.segmented_image.file)
        area = analise['area']
        # Cor = analise['cor'] Aguardando implementação de Sobral

        # ATUALIZAR ATENDIMENTO
        atendimento = models.Atendimento.objects.get(id=atendimentoId)
        atendimento.imagemAnalisada = True

        caracteristica = None
        if not atendimento.caracteristica:
            caracteristica = models.CaracteristicaFerida.objects.create(area=area, cor=None)
        else:
            caracteristica = models.CaracteristicaFerida.objects.get(pk=atendimento.caracteristica.pk)
            caracteristica.area = area
        caracteristica.save()

        atendimento.caracteristica = caracteristica
        atendimento.save()

        return Response(analise)


class CaracteristicaServiceView(APIView):
    def post(self, request):
        atendimentoId = request.data.get("pk")
        caracteristica = models.CaracteristicaFerida.objects.filter(atendimento=atendimentoId).first();
        serializer = serializers.CaracteristicaFeridaSerializer(caracteristica)
        return Response(serializer.data)


