from django.shortcuts import render, redirect
import markdown2
import random
from . import util
from django.urls import reverse
from django.http import HttpResponseRedirect

md = markdown2.Markdown()

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def viewpage(request, entries):
    entrylist = util.list_entries()
    if entries in entrylist:
        return render(request, "encyclopedia/entries.html" , {
            "title" : entries,
            "entry" : md.convert(util.get_entry(entries))
            })
    else:
        return render(request, "encyclopedia/error.html", {
            "entry" : entries
        })
        
def search(request):
    entries = util.list_entries()
    string = []
    if request.method == "POST":
        query = request.POST['q']
        for entry in entries:
            if query.upper() == entry.upper():
                return render(request, "encyclopedia/entries.html",{
                    "title": query,
                    "entry": md.convert(util.get_entry(query))
                })

        for entry in entries:
            if query.upper() in entry.upper():
                return render(request, "encyclopedia/entries.html",{
                    "entry": md.convert(util.get_entry(entry))
                })
                
        for entry in entries:
            if query.upper() not in entry.upper():
                return render(request, "encyclopedia/error.html", {
                    "entry" : query
                })

def createPage(request):
        
    if request.method == "GET":
        return render(request, "encyclopedia/create.html") 

    if request.method == "POST":
        entries = util.list_entries()
        entry = request.POST.get("content")
        title = request.POST.get("title")
        if title in entries:
             return render(request, "encyclopedia/error.html", {
                    "entry" : title
                })
        else:
            util.save_entry(title, entry)
            return render(request, "encyclopedia/entries.html" , {
                "title" : title,
                "entry" : entry
                })

def editPage(request, title):
  
    if request.method == "GET":
        entry = util.get_entry(title)
        return render(request, "encyclopedia/edit.html",{
            "title": title,
            "entry": entry
        }) 
    if request.method == "POST":
        entry = request.POST.get("content")
        util.save_entry(title, entry)
        return HttpResponseRedirect(reverse('viewpage', args=[title]))

def rand(request):
    entries = util.list_entries()
    entry = random.choice(entries)

    return render(request, "encyclopedia/entries.html" , {
        "title" : entry,
        "entry" : md.convert(util.get_entry(entry))
        })    

