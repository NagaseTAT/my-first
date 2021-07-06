from django import forms
from .models import InfoModelForm

class TestForm(forms.Form):
    text = forms.CharField(label='文字入力')
    num = forms.IntegerField(label='数量')

class InfoModelFormAdd(forms.ModelForm):
    class Meta:
        model = InfoModelForm
        fields = ['name', 'mail', 'gender', 'department', 'year', 'created_at']
