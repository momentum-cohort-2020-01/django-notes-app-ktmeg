from django.shortcuts import render
from django.http import HttpResponse

import data

def notes_list(request):
  notes = data.NOTES
  return render(request, 'core/notes_list.html', {'notes': notes})
  # return HttpResponse("Hello, world")

def notes_detail(request, pk):
  note = data.NOTES[str(pk)]
  return render(request, 'core/notes_detail.html', {'note': note})

