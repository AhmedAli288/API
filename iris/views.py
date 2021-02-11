from django.shortcuts import render
from django.http import JsonResponse
import json
from rest_framework.response import Response
from rest_framework.decorators import api_view, APIView
from .apps import model
from rest_framework.exceptions import ParseError
from rest_framework.parsers import FileUploadParser
from rest_framework import status
from rest_framework.parsers import MultiPartParser
from rest_framework.decorators import parser_classes

from .tess import OCR
# Create your views here.

# For Files


@api_view(['POST'])
@parser_classes((MultiPartParser, ))
def post(request):

    result = OCR(request)

    return Response(result, status=status.HTTP_201_CREATED)


# For Iris

@api_view(['POST'])
def iris(data):
    results = json.loads(data.body)
    print(results)

    inputs = []

    inputs.append(results.get("SL"))
    inputs.append(results.get("SW"))
    inputs.append(results.get("PL"))
    inputs.append(results.get("PW"))

    result = model.predict([inputs])

    return JsonResponse(result[0], safe=False)
