from django.contrib import admin
from . import models


class ImagemAdmin(admin.ModelAdmin):
    list_display = ['atendimento', 'doenca', 'imageName',]

    class Meta:
        model = models.Imagem

    def doenca(self, obj):
        return obj.atendimento.ferida


admin.site.register(models.Clinica)
admin.site.register(models.Profissional)
admin.site.register(models.ClinicaProfissional)
admin.site.register(models.Paciente)
admin.site.register(models.Anamnese)
admin.site.register(models.Observacao)
admin.site.register(models.HabitosPessoais)
admin.site.register(models.Clinico)
admin.site.register(models.Doenca)
admin.site.register(models.DoencaPaciente)
admin.site.register(models.Ferida)
admin.site.register(models.CaracteristicaFerida)
admin.site.register(models.Tecnica)
admin.site.register(models.Agenda)
admin.site.register(models.Noticia)
admin.site.register(models.Atendimento)
admin.site.register(models.AtendimentoExtra)
admin.site.register(models.AtendimentoTecnica)
admin.site.register(models.Imagem, ImagemAdmin)
