from django.shortcuts import render
from mix_other.models import Question


def home_screen_view(request):

    context = {}
    questions = Question.objects.all()
    context['questions'] = questions
 
    return render(request, "personal/home.html", context)