from django import forms
from .models import Task, User

class AddTaskForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=User.objects.all(), empty_label=None, widget=forms.Select(attrs={'class': 'form-control'}))
    due_date = forms.DateField(widget=forms.DateInput(attrs={'placeholder': 'Due Date', 'class': 'form-control', 'type': 'date'}))

    class Meta:
        model = Task
        fields = ['user', 'task_description', 'due_date', 'priority', 'status', 'categories']
        widgets = {
            'task_description': forms.Textarea(attrs={'placeholder': 'Task Description', 'class': 'form-control'}),
            'due_date': forms.DateInput(attrs={'placeholder': 'Due Date', 'class': 'form-control'}),
            'priority': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'categories': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }


class TaskFilterForm(forms.Form):
    start_due_date = forms.DateField(label='Start Due Date', required=False)
    end_due_date = forms.DateField(label='End Due Date', required=False)
    