from .models import Company, Tool, ToolEntry
from django import forms

class CompanyForm(forms.ModelForm):

    class Meta:
        model = Company
        fields = ['title', 'logo', 'section', 'description', 'wiki', 'url']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Company\'s title'}),
            'section': forms.TextInput(attrs={'placeholder': 'What is the section your company is active at?'}),
            'description': forms.Textarea(attrs={'placeholder': 'Give us a few words about your company'}),
            'wiki': forms.TextInput(attrs={'placeholder': 'Wiki for your company'}),
            'url': forms.TextInput(attrs={'placeholder': 'i.e. www.domain.com'}),
        }

class ToolForm(forms.ModelForm):

    class Meta:
        model = Tool
        fields = ['title']
        widgets = {
        'title': forms.TextInput(attrs={'placeholder': 'Tool\'s title'}),
        }

class ToolEntryForm(forms.ModelForm):

    class Meta:
        model = ToolEntry
        fields = ['title']
        widgets = {
        'title': forms.TextInput(attrs={'placeholder': 'Entry\'s title'}),
        }
