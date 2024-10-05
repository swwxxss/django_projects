from django.shortcuts import render
from .forms import CalculatorForm

def calculator_view(request):
    result = None
    if request.method == 'POST':
        form = CalculatorForm(request.POST)
        if form.is_valid():
            first_number = form.cleaned_data['first_number']
            second_number = form.cleaned_data['second_number']
            operation = form.cleaned_data['operation']

            if operation == '+':
                result = first_number + second_number
            elif operation == '-':
                result = first_number - second_number
            elif operation == '*':
                result = first_number * second_number
            elif operation == '/':
                result = first_number / second_number if second_number != 0 else 'Помилка: Ділення на нуль!'
    else:
        form = CalculatorForm()

    return render(request, 'calculator/calculator.html', {'form': form, 'result': result})