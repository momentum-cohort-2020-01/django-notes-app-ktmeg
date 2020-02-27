from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Note
from .forms import NoteForm

def notes_list(request):
    notes = Note.objects.all()
    return render(request, 'core/notes_list.html', {'notes': notes})
    # return HttpResponse("Hello, world")

def notes_detail(request, pk):
    note = Note.objects.get(pk=pk)
    return render(request, 'core/notes_detail.html', {'note': note, "pk":pk})

def note_new(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid(): 
            note = form.save()
            return redirect('notes-detail', pk=note.pk)
    else:
        form = NoteForm()
        
    return render(request, 'core/notes_new.html', {'form': form})

def edit_note(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid(): 
            note = form.save()
            return redirect('notes-detail', pk=note.pk)
    else: 
      form = NoteForm(instance=note)
    return render(request, 'core/notes_new.html', {'form': form})
