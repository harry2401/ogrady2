from django                                 import forms
from .models                                import Site, Photo,  EnquiryB, Bookmark

class SiteadvertForm(forms.ModelForm):
    class Meta:
        model = Site
        fields = ( 'notice' ,)

class SitenoteForm(forms.ModelForm):
    class Meta:
        model = Site
        fields = ('note',)

class PhotoInsertForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('title', 'cover')

class PhotopriorityForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('priority',)

class PhototitleForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('title',)

class BookmarkInsertForm(forms.ModelForm):
    class Meta:
        model = Bookmark
        fields = ('title', 'address')

class BookmarkpriorityForm(forms.ModelForm):
    class Meta:
        model = Bookmark
        fields = ('priority',)

class BookmarktitleForm(forms.ModelForm):
    class Meta:
        model = Bookmark
        fields = ('title',)

class EnquiryInsertForm(forms.ModelForm):
    class Meta:
        model = EnquiryB
        fields = ('content',)

class EnquirypriorityForm(forms.ModelForm):
    class Meta:
        model = EnquiryB
        fields = ('priority',)

"""
class PhotoauthorUpdateForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('author',)
"""
