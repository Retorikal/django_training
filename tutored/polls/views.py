from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    
    template = 'polls/index.html'
    context = {
        'latest_question_list': latest_question_list,
    }

    #return HttpResponse(template.render(context, request))
    return render(request, template, context)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except:
        raise Http404("Question does not exist")

    template = 'polls/detail.html'
    context = {
        'question': question,
    }

    #return HttpResponse("You're looking at question %s." % question_id)
    return render(request, template, context)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    numArray = {1, 5, 6, 7, 9}
    title = 'uwu'

    template = 'polls/vote.html'
    context = {
        'numArray': numArray,
        'title': title,
    }

    #return HttpResponse("You're voting on question %s." % question_id)
    return render(request, template, context)