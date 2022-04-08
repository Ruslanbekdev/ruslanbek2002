from turtle import title
from django import forms
from .models import Articles

class ArticleCreatedForm(forms.ModelForm):
    class Meta:
        model = Articles
        fields = ("author", "title","image", "content", "tags")
        exclude = ['author']
    def __init__(self, *args, **kwargs):
        super(ArticleCreatedForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        
class ArticleCreatedFormold(forms.Form):
    title = forms.CharField()
    content = forms.CharField(widget = forms.Textarea)

    def clean_title(self):
        data = self.cleaned_data
        title = data.get('title')
        query = Articles.objects.filter(title__iexact = title)
        if query:
            raise forms.ValidationError('title is alredy used !!')
        # if title.lower() == 'new title':
        #     raise forms.ValidationError('new title is alredy use !!')
        return title
    def clean(self):
        data = self.cleaned_data
        title = data.get('title')
        content = data.get('content')
        if not title.istitle() and  not content.istitle():
            # raise forms.ValidationError('Please fisrt word must be upper !!')
            self.add_error('title', 'Please fisrt word must be upper !!- TITLE'),
            self.add_error('content', 'Please fisrt word must be upper !!- CONTENT'),
        return data
