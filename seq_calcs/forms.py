from django import forms

class SequenceForm(forms.Form):
    input_sequence = forms.CharField(label="", help_text="Input Sequence",  max_length=5000, widget=forms.Textarea, required=False)
