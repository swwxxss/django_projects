from django import forms

class CalculatorForm(forms.Form):
    first_number = forms.FloatField(label='Перше число')
    second_number = forms.FloatField(label='Друге число')
    operation = forms.ChoiceField(choices=[
        ('+', 'Додати'),
        ('-', 'Відняти'),
        ('*', 'Помножити'),
        ('/', 'Поділити'),
    ])