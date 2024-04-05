from django.shortcuts import render
from polls.models import Question

def index(request):
    examplo = Question.objects.order_by("-pub_date")[:1].first()
    contextlo = {"examplo": examplo}
    return render(request, "main/index.html", contextlo)

# Create your views here.
