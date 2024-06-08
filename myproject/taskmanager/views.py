from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from celery.result import AsyncResult
from .tasks import scrape_data
from .serializers import StartScrapingSerializer

class Start_Scraping(APIView):
    def post(self, request):
        serializer = StartScrapingSerializer(data=request.data)
        if serializer.is_valid():
            coin_acronyms = serializer.validated_data['coins']
            job = scrape_data.apply_async(args=[coin_acronyms])
            return Response({'job_id': job.id}, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Scraping_Status(APIView):
    def get(self, request, job_id):
        result = AsyncResult(job_id)
        if result.state == 'PENDING':
            return Response({'state': result.state, 'data': None})
        elif result.state != 'FAILURE':
            return Response({'state': result.state, 'data': result.result})
        else:
            return Response({'state': result.state, 'data': str(result.info)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
