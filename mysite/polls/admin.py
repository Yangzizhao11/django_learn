from django.contrib import admin
from .models import Question
from .models import Choice, Question, QuestionImage

class ChoiceInline(admin.StackedInline):
    model = Choice
    # prevent extra when edit question
    def get_extra(self, _, obj=None, **__):
        return 0 if obj else 3

class ImageAdmin(admin.ModelAdmin):
    list_display = ["title", "image"]


class QuestionAdmin(admin.ModelAdmin):
    list_display = ["question_text", "pub_date", "was_published_recently"]
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)

admin.site.register(QuestionImage, ImageAdmin)

admin.site.register(Choice)