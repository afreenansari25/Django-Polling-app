from django.contrib import admin
from django.forms import inlineformset_factory
from .models import Question, Choice

admin.site.site_header = 'Pollster Admin'
admin.site.site_title = 'Pollster Admin area'
admin.site.index_title = 'Welcome to pollster Admin area'

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields':['question_text']}),
        ('Date Information', {'fields':['pub_date'], 'classes': ['collaps']}),
    ]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)

#admin.site.register(Question)
#admin.site.register(Choice)
