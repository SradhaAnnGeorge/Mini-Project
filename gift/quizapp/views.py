from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import QuizCategory, Question, Answer

class QuizCategoryListView(ListView):
    model = QuizCategory
    template_name = 'quiz/category_list.html'
    context_object_name = 'categories'

class QuestionListView(ListView):
    model = Question
    template_name = 'quiz/question_list.html'
    context_object_name = 'questions'

class QuestionDetailView(DetailView):
    model = Question
    template_name = 'quiz/question_detail.html'
    context_object_name = 'question'

def quiz_category_detail(request, category_id):
    category = get_object_or_404(QuizCategory, id=category_id)
    questions = category.category.all()  # Access related questions using the 'category' reverse relation
    context = {'category': category, 'questions': questions}
    return render(request, 'quiz/quiz_category_detail.html', context)

