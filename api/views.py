from django.http import HttpResponse
from django.shortcuts import redirect
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import ConvertTextModel
from .serializers import ConvertTextSerializer, ConvertFileSerializer
from .convert import to_latin, to_ciril

# Create your views here.
def home(request):
    return HttpResponse('Salam alekum!')


# class ReadFileViews(APIView):
#


class AddTextView(CreateAPIView):
    queryset = ConvertTextModel.objects.all()
    serializer_class = ConvertTextSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return redirect('api')


class AddFileView(CreateAPIView):
    queryset = ConvertTextModel.objects.all()
    serializer_class = ConvertTextSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return redirect('api')


class HomeViews(ListAPIView):
    queryset = ConvertTextModel.objects.order_by('-date')[:1]
    serializer_class = ConvertTextSerializer


class toLatinView(APIView):
    def get(self, request, *args, **kwargs):
        last_text = ConvertTextModel.objects.last().text
        convert = to_latin(last_text)
        return Response({'convert': convert})
