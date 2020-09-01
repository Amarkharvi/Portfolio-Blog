from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from ckeditor_uploader.fields import RichTextUploadingField
from .models import Post,Category



class CommentForm(forms.Form):
    author = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Your Name"
        })
    )
    body = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Leave a comment!"
        })
    )

class PostForm(forms.ModelForm):
    categories=forms.ModelChoiceField(queryset=Category.objects.all())
    class Meta:
        model=Post
        fields=['title','body','categories']
   

class UpdatePost(forms.ModelForm):
    categories=forms.ModelChoiceField(queryset=Category.objects.all())
    
    class Meta:
        model=Post
        fields=['title','body','categories']

class DeletePost(forms.ModelForm):
    class Meta:
        model=Post
        fields=[]
    