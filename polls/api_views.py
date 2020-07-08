from rest_framework import viewsets
from .serializers import ChoiceSerializer, QuestionSerializer
from .models import Choice, Question
from django.utils import timezone


class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.filter(pub_date__lte=timezone.now())
    serializer_class = QuestionSerializer
