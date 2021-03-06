import json
from django.shortcuts import render, get_object_or_404
from django.core.serializers.json import DjangoJSONEncoder

from topics.models import *
from news.models import *
# Create your views here.
def index(request):
    data = {}
    data["corpus"] = Corpus.objects.all()[0]
    data["topics"] = data["corpus"].getTopicsByRank()
    data["topics_js"] = json.dumps(data["corpus"].getYearsTopics())
    return render(request,'Tome/index.html', data)
