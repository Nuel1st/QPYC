from django import forms
from .models import Song

class SongForm(forms.ModelForm):
    # search_query = forms.CharField(required=False, label='Search')
    
    class Meta:
        model = Song
        fields = ['title', 'file_type', 'file']

    def clean(self):
        cleaned_data = super().clean()
        file_type = cleaned_data.get('file_type')
        file = cleaned_data.get('file')

        if file_type == 'audio' and not file.name.endswith('.mp3'):
            raise forms.ValidationError('Please upload an MP3 audio file.')
        elif file_type == 'docx' and not file.name.endswith('.docx'):
            raise forms.ValidationError('Please upload a DOCX document.')

        return cleaned_data
