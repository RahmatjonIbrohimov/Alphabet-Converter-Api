from django.http import HttpResponse
from django.shortcuts import redirect
from rest_framework.generics import CreateAPIView, ListAPIView
from .models import ConvertTextModel
from .serializers import ConvertTextSerializer, ConvertFileSerializer


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

