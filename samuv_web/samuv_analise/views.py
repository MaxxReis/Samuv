# -*- coding: utf-8 -*-
import base64
import io

import numpy as np
import cv2
from samuv_web import settings
from . import segmentation, area_measure
from samuv_analise import serializers


# A implementação do serializer não está 100% correta mas
# podemos usar um objeto por enquanto.
# Inclua nos atributos e no init os dados que você vai
# passar para o serializer.


class ImagemAnalisada(object):
    def __init__(self, area):
        self.area = area


def convertImageBase64(imagem):
    imagem = str(imagem.file).replace('\\', '/')
    base64image = ''
    with open(imagem, "rb") as imageFile:
        base64image = base64.b64encode(imageFile.read())
    data = {"img64": base64image}
    return data


# CORREÇÕES DA ANÁLISE
def SegmentarImagem(image_data, imagem):
    image_data = bytes(image_data, 'utf-8')
    imagename = imagem.foto.path.split('\\')[-1].split('.')[0]
    code = base64.decodebytes(image_data)
    url = imagename + "_segmentada.png"
    url = settings.MEDIA_ROOT + "\imagens_segmentadas\\" + url
    url = url.replace('\\', '/')
    with open(url, "wb") as fh:
        fh.write(code)
    img_mask = cv2.imread(url)
    imagem = cv2.imread(imagem.foto.path)
    result_image = area_measure.segment_image(imagem, img_mask)
    cv2.imwrite(str(url), result_image)
    return url


def AnalisarImagem(image, segmented_image):
    segmented_image = str(segmented_image).replace('\\', '/')
    segmented_image = cv2.imread(segmented_image)
    image = cv2.imread(image)

    pixels_per_metric = area_measure.get_pixel_per_metric(segmented_image)
    area = area_measure.measure(segmented_image, pixels_per_metric)
    # cor = seu_metodo(segmented_image, pixel_per_metric)
    # ^ Chamar a classe/método para anélise de cores e textura passando a imagem segmentada e
    # o valor do pixel_per_metric. Dentro do seu método utilize o comando:
    # area_measure.measure(sua_imagem, pixels_per_metric) para receber a área em cm como float

    imagem = ImagemAnalisada(area=area)
    # image.cor = XXXXXX <-- Incluir os campos da analise de cor

    serializer = serializers.AnaliseImagemSerializer(imagem)
    return serializer.data
