from django.shortcuts import render, get_object_or_404,redirect
from .models import Question, Choice
from django.utils import timezone
from .forms import ChoiceForm


# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})


def question_list(request):
    questions = Question.objects.all()
    return render(request, 'poll/question_list.html', {'questions': questions})

def question_create(request):
    if request.method == "POST":
        question_text = request.POST.get("question_text")
        pub_date = timezone.now()
        Question.objects.create(question_text=question_text, pub_date=pub_date)
        return redirect('question_list')
    return render(request, 'poll/question_form.html')

def question_delete(request,pk):
    question=get_object_or_404(Question, pk=pk)
    if request.method=='POST':
        question.delete()
        return redirect('question_list')
    return render(request, 'poll/question_delete.html',{'question': question})

def choice_create(request):
    if request.method=='POST':
        form=ChoiceForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect('question_list')
    else:
        form = ChoiceForm()
    return render(request, 'poll/choice_form.html',{'form':form})

def choice_update(request, pk):
    choice = get_object_or_404(Choice, pk=pk)
    if request.method == 'POST':
        form = ChoiceForm(request.POST, instance=choice)
        if form.is_valid():
            form.save()
            return redirect('question_list')
    else:
        form = ChoiceForm(instance=choice)
    
    return render(request, 'poll/choice_form.html', {'form': form})

def choice_delete(request, pk):
    choice=get_object_or_404(Choice, pk=pk)
    if request.method=='POST':
        choice.delete()
        return redirect('question_list')
    return render(request, 'poll/choice_delete.html', {'choice':choice})
