from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Choice, Question
from django.template import loader
from django.contrib.auth.forms import AuthenticationForm
import mimetypes
from .models import ExerTime

def get_data(request):
    #Working on this - HAN
    if request.method=="POST":
        print("checkpoint")

class IndexView(generic.ListView):
    template_name = 'exercise/index.html'
    context_object_name = 'latest_question_list'
    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'exercise/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'exercise/results.html'


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('exercise/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'exercise/index.html', context)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'exercise/detail.html', {'question': question})

# class TimerView(generic.TimerView):
#     model = TotalTime
#     template_name = 'exercise/timer.html'

def timer(request):
    print ("checkpoint")
    totaltime = 0
    setno = 0
    breakt = 0
    exerciset = 0
    setno = (request.POST.get('setno-anw', ''))
    breakt = (request.POST.get('break-anw', ''))
    exerciset = (request.POST.get('exercise-anw', ''))
    if (setno == '' or breakt == '' or exerciset == '' ):
        totaltime = 0
    else: 
        totaltime = int(setno)*(int(breakt)-1)+int(setno)*int(exerciset)
    exertime_list =  ExerTime.objects.order_by('-setno') #WORKING ON THIS -HAN
    print (exertime_list) #WORKING ON THIS -HAN
    request.session['totaltime'] = totaltime
    print (totaltime)
    print (request.session['totaltime'])
    #return render(request, 'exercise/timer.html')
    time = {"totaltime": totaltime}
    #time = {"totaltime": request.session.get('totaltime')}
    return render(request, 'exercise/timer.html', time)

def showtimer(request):
    setno = (request.POST.get('setno-anw', ''))
    breakt = (request.POST.get('break-anw', ''))
    exerciset = (request.POST.get('exercise-anw', ''))
    if (setno == '' or breakt == '' or exerciset == '' ):
        totaltime = 0
    else: 
        totaltime = int(setno)*(int(breakt)-1)+int(setno)*int(exerciset)
    time = {"totaltime": totaltime}
    #time = {"totaltime": request.session.get('totaltime')}
    return render(request, 'exercise/showtimer.html', time)



def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'exercise/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'exercise/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('exercise:results', args=(question.id,)))