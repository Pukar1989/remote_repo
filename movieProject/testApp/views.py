from django.shortcuts import render
from testApp.models import Movie
from testApp import forms

# Create your views here.
def index_view(request):
    return render(request,'testApp/index.html')

def add_movie_view(request):
    form=forms.MovieForm()
    if request.method=='POST':
        form=forms.MovieForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
        return index_view(request)
    return render(request,'testApp/addmovie.html',{'form':form})
def list_movie_view(request):
     movie_list=Movie.objects.all()
     return render(request,'testApp/listmovie.html',{'movie_list':movie_list})
