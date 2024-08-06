from django import forms
from .models import QuestionImage
 
class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = QuestionImage
        fields = ['question', 'title', 'image']
