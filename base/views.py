from django.shortcuts import redirect, render, HttpResponse
from base.models import Addnote

# Create your views here.

def home(request):
    if request.method=="POST":
        title=request.POST['title']
        desc =request.POST['description']
        obj= Addnote(noteTitle = title, noteDesc=desc)
        obj.save()
    return(render(request,'home.html'))


def list(request):
    allNotes=Addnote.objects.all()
    print(allNotes)
    list={'list': allNotes}
    return(render(request,'list.html', list))

 
def delete_note(request, id):
    temp=Addnote.objects.get(pk =id)
    temp.delete()
    return redirect('list')

def update_note(request, id):
    temp=Addnote.objects.get(pk =id)
    obj={'obj': temp}
    print(obj.keys())
    return(render(request,'update.html', obj))

def save_changes(request,id):
    new_title=request.POST['title']
    new_desc =request.POST['description']
    temp=Addnote.objects.get(pk =id)
    temp.noteTitle=new_title
    temp.noteDesc= new_desc
    # print(temp.noteTitle)
    # print(temp.noteDesc)
    temp.save()
    s='''
    <h1 style="text-align:center;"> Your changes have been saved</h1>
    <a href="/list" style="text-align:center;font-size: 50px;">View Modified List</a>
    '''
    return HttpResponse(s)



    
     
 