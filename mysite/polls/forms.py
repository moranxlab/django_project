from django import forms
from .models import Question
from django.contrib.auth.models import User


class QuestionForms(forms.form):
    question_text = forms.CharField(label='Question Text', max_length=200)
    pub_date = forms.DateField(label='Date Published', input_formats=['%Y-%m-%s'])


class Add_user(forms.ModelForm):
    class Meta:
        model = User
        fields = ['usermam','password','first_name','last_name','email','is_active']    


        { 

            

        }  