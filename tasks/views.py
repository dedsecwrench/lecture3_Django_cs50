from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

# instead of global variable tasks i'm gonna use user sessions
tasks = ["foo","bar","baz"]

# created new form through django
class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    # priority = forms.IntegerField(min_value=0,max_value=10)

def index(request):
    # session is like a big dictionary representing the all data we have in the file inside the session about the user
    # i'm looking inside of the session to see is their already a lsit of tasks in that session
    # if there isn't already a list of tasks in the session
    if "tasks" not in request.session:
        # then i'm gonna create list of tasks in the session
        # if user doesn't have a list of task
        # go ahead and give them the empty list of tasks
        request.session['tasks'] = []
    return render(request, "tasks/index.html", {
        # now i'm gonna render request.session["tasks"]
        # to pass in that list of tasks to this particular template
        "tasks": request.session["tasks"]
        })

def add(request):
    # if user is submitted the form data
    if request.method == "POST":
        # all the form data that user submitted, saved it in form variable
        form = NewTaskForm(request.POST)
        # checking if the form is valid
        # did they actually provided all the necessary data
        if form.is_valid():
            # getting the new task field's data in task vriable
            task = form.cleaned_data["task"]
            # appending that new task in tasks array/list
            # tasks.append(task)
            # appending that new task in the list of user sessions
            request.session["tasks"] += [task]
            # after appending the task we are going back to index page which shows all tasks.
            return HttpResponseRedirect(reverse("tasks:index"))
        # if form isn't valid then we are getting the url of existing form that user has submitted 
        else:
            return render(request, "tasks/add.html",{
                # sending existing form context
                "form": form
            })    

    # if the request method wasn't posted at all
    # if the user just tried to get the page rather than submitting the data
    # then we just gonna render to them an empty form
    return render(request, "tasks/add.html",{
        # NewTaskForm() with brackets creates fresh new blank form
        "form": NewTaskForm()
    })    




    # No such table in django_sessions ERROR =>

    # Django stores data about sessions inside of table by default
    # and you can change to have django store data about sessions
    
    # so we need to create that sessions table 
    # run this command python manage.py migrate
    # it means to migrate data into a database
    # it allow us to create all of the default tables inside of django's database

