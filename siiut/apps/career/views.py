from django.shortcuts import render, redirect, HttpResponse
from .forms import QuarterForm
from .models import Quarter, Level
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
# CRUD Views for Quarter

def quarter_list(request):
  quarters = Quarter.objects.all()
  context = {
    "quarters": quarters
  }
  return render(request, 'career/quarter/index.html', context)

def quarter_create(request):
  if request.method == 'POST':
    form = QuarterForm(request.POST)
    if form.is_valid():
      quarter = Quarter(
        quarter = form.cleaned_data['quarter'],
        quarter_name = form.cleaned_data['quarter_name']
      )
      quarter.save()
      return redirect('career:quarter_list')
  else:
    form = QuarterForm()
    return render(request, 'career/quarter/create.html', {'form': form})

def quarter_details(request, q_id):
  quarter = Quarter.objects.get(pk = q_id)
  return render(request, 'career/quarter/details.html', {'quarter': quarter})

def quarter_update(request, q_id):
    q = Quarter.objects.get(pk = q_id)
    if request.method == 'POST':
        form = QuarterForm(request.POST, instance=q)
        if form.is_valid():
            q.quarter = form.cleaned_data['quarter']
            q.quarter_name = form.cleaned_data['quarter_name']
            q.save()
            return redirect('career:quarter_list')
        else:
            return HttpResponse('Hay error en el formulario')
    else:
        form = QuarterForm(instance = q)
    return render(request, 'career/quarter/update.html', {'form': form})

def quarter_delete(request, q_id):
  if request.method == 'POST':
    q = Quarter.objects.get(pk = q_id)
    q.delete()
    return redirect('career:quarter_list')
  
#------------------------------------------#
# CRUD Views for Level

class LevelList(ListView):
  model = Level
  template_name = 'career/level/index.html'
  context_object_name = 'levels'
  
class LevelDetails(DetailView):
  model = Level
  template_name = 'career/level/details.html'
  context_object_name = 'level'
  
class LevelCreate(CreateView):
  model = Level
  template_name = 'career/level/create.html'
  success_url = reverse_lazy('career:level_list')

class LevelUpdate(UpdateView):
  model = Level
  template_name = 'career/level/update.html'
  success_url = reverse_lazy('career:level_list')
  
class LevelDelete(DeleteView):
  model = Level
  template_name = 'career/level/delete.html'
  success_url = reverse_lazy('career:level_list')
  
