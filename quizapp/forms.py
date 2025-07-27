
from django.forms import ModelForm,ValidationError
from .models import Survey
import json

class SurveyForm(ModelForm):
    class Meta:
        model = Survey
        fields = ('questions_json',)
    
    def get_initial_for_field(self, field, field_name):
        return super().get_initial_for_field(field, field_name)
    
    def clean(self):
        cleaned_data = super().clean()
        questions_json = cleaned_data.get('questions_json')
        try:
            question_data=json.loads(questions_json)
        except Exception as e:
            raise ValidationError("Invalid JSON")