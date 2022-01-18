from django import forms
from .models import Song_list_m, Categories_m

class Song_list_f(forms.ModelForm):
    class Meta:
        model = Song_list_m
        fields = ['ID', 'Title', 'Category','Alter_ID', 'DM_ID', 'SC_ID', 'default_id']
    def clean_Title(self):
        return self.cleaned_data['Title'].title()

class Categories_f(forms.ModelForm):
    class Meta:
        model = Categories_m
        fields = '__all__'
    def clean_Category(self):
        return self.cleaned_data['Category'].title()
