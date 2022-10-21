from django.forms import ModelForm, Textarea, DateInput
from .models import Entry


class EntryForm(ModelForm):
    class Meta:
        model = Entry
        fields = ['headline', 'body_text', 'pub_date', 'authors']
        widgets = {
            'body_text': Textarea(attrs={'cols': 80, 'rows': 10}),
            'pub_date': DateInput(attrs={'type': 'date'}),
        }