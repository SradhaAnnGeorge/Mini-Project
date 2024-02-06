from django.contrib import admin

from .models import QuizCategory, Question, Answer

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]

class QuizCategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'created_at', 'updated_at')

class AnswerAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer', 'is_correct', 'created_at', 'updated_at')

admin.site.register(QuizCategory, QuizCategoryAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer,AnswerAdmin)
