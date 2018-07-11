from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .forms import SequenceForm

from seq_calcs import sequence_calc

def get_sequence(request):
    return render(request, 'seq_calcs/seq_calcs.html', {'form': SequenceForm()})

def show_results(request):
    if 'input_sequence' in request.GET:
        input_sequence = request.GET['input_sequence']
        if "reverse_complement" in request.GET:
            output_sequence = sequence_calc.reverse_complement(input_sequence)
        elif "complement" in request.GET:
            output_sequence = sequence_calc.complement(input_sequence)
        elif "melting_temp" in request.GET:
            output_sequence = sequence_calc.melting_temp(input_sequence)
        elif "gc_content" in request.GET:
            output_sequence = sequence_calc.gc_content(input_sequence) 
        else:
            output_sequence = "Invalid option"
    else:
        output_sequence = 'Invalid sequence'
        print(output_sequence)

    return HttpResponse(output_sequence)

def index(request):
    return get_sequence(request)
