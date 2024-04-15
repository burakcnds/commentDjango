from django.shortcuts import render,redirect
from .models import *
from .forms import *
# Create your views here.

def index(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            user_comment = form.save(commit=False)
            user_comment.user = request.user
            user_comment.save()
            return redirect('index')
        else:
            return render(request,'index.html',context)
        
    comment = Comment.objects.all()
    tersComment = reversed(comment)
    # Reversted methodu ilgili arrayi tam tersine çevirir
    
    
    
   
    form = CommentForm()
    
    context = {
        'yorum':tersComment,
        'form':form
    }
    return render(request,'index.html',context)




def sil(request):
    if request.method == 'POST':
        formId = request.POST['sil']
        comment = Comment.objects.filter(id = formId)
        comment.delete()
        return redirect('index')

