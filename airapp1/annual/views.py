from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import AnnualMean, DailyMean
from rest_framework.views import APIView
from .serializers import AnnualSerializer, DailySerializer
from rest_framework.response import Response


#Annual app
class homeview(ListView):
    template_name = 'annual_means/home.html'

    def get_queryset(self):
        return AnnualMean.objects.values("Site", "url").distinct()

    
def detail(request, url):
    sit = AnnualMean.objects.filter(url=url).first()
    #question = Question.objects.get(pk = question_id)
    return render(request, 'annual_means/detail.html', {'sit':sit})


#APIs
class annual_means(APIView):
    def get(self, request):
        means = AnnualMean.objects.all()
        serializer = AnnualSerializer(means, many=True)
        return Response(serializer.data)

    
class site_annual_means(APIView):
    def get(self, request, url):
        means = AnnualMean.objects.filter(url=url)
        serializer = AnnualSerializer(means, many=True)
        return Response(serializer.data)

    
class pollutant_annual_means(APIView):
    def get(self, request, poll):
        means = AnnualMean.objects.filter(poll=poll)
        serializer = DailySerializer(means, many=True)
        return Response(serializer.data)

    
class daily_means(APIView):
    def get(self, request):
        means = DailyMean.objects.all()
        serializer = DailySerializer(means, many=True)
        return Response(serializer.data)

    
class site_daily_means(APIView):
    def get(self, request, url):
        means = DailyMean.objects.filter(url=url)
        serializer = DailySerializer(means, many=True)
        return Response(serializer.data)

    
class pollutant_daily_means(APIView):
    def get(self, request, poll):
        means = DailyMean.objects.filter(poll=poll)
        serializer = DailySerializer(means, many=True)
        return Response(serializer.data)
    
