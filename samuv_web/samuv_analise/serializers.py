from rest_framework import serializers


# class CoresSerializer(serializers.ModelSerializer):
#     Incluir aqui os campos que serão exibidos pela analise de cores.


class AnaliseImagemSerializer(serializers.Serializer):
    area = serializers.FloatField()
    # cores = CoresSerializer()