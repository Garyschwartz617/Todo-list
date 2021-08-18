from django import forms
from .models import Todo, Category

class TodoForm(forms.Form):
    title = forms.CharField(max_length=80)
    details = forms.CharField(max_length=300)
    has_been_done = forms.BooleanField(required=False)
    date_completion = forms.DateTimeField(required=False)
    deadline_date = forms.DateTimeField()
    category = forms.ModelChoiceField(queryset=Category.objects.all())

