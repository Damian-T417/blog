from django import forms

from blog.models import Post, Tag


class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class TagForm(forms.ModelForm):

    class Meta():
        model = Tag
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(TagForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
