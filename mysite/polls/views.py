from django.shortcuts import render, get_object_or_404
from django.views import View   
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User

from models import Question, Choice 
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list' :latest_question_list}
    return render(request=request, template_name='polls/index.html', context=context)
# Create your views here.
def detail(request, question_id):
        question = get_object_or_404(Question, pk = question_id)
        return render(request=request, template_name='polls/detail.html', context={'question':question})



class NewQuestion(view):
    def post(self, request):
     form = QuestionForm(request.POST)
    if form.is_valid():
        question_text = form.cleaned_data['question_text']
        pub_date = form.cleaned_data['pub_date']
        # q = Question(question_text, pub_date)\
        # q.save()
        Question.objects.create(question_text=question_text, pub_date=pub_date)
        HttpResponseRedirect(reverse('polls:index'))


    def get(self, request):
        form = QuestionForm()
        return render(request=request, tamplate_name='polls/question_form.html', context={'form':form})





class vote(View):
    def post(self, request, question_id):
        question = get_object_or_404(Question,pk=request_id)
        choice = question.choice_set.get(pk= request.post['choice'])
        choice.vote = choice.votes +1
        choice.save()
        return HttpResponseRedirect(reverse('polls:detail', args=(question_id)))
    def get(self, request, question_id):
        return HttpResponse('this was a get request')    



def register(request):
    if request.methods=='POST':
            form = UserForm()      






























































class LogInUser(view):
    def get

