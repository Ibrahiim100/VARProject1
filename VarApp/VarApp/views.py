from django.http import HttpResponse
from django.template import loader
from .index import analyze_sentiment
from .models import SentimentVARModel
from django.forms.models import model_to_dict
from django.shortcuts import render


def VarApp(request):
  all_objects = SentimentVARModel.objects.all()
  for item in all_objects.values('game','decision', 'commentary','result', 'date'):
    result = analyze_sentiment(item['commentary'])
    record = SentimentVARModel.objects.get(commentary=item['commentary'])
    record.result = result
    record.save() #updates the result field with the result of the sentiment analysis
    print("YESSS", result)
  
  # object = FooForm(data=model_to_dict(SentimentVARModel.objects.get(pk=object_id)))
  return render(request, 'index.html', {'all_objects': all_objects})


  
