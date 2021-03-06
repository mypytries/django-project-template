# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

# Views for Students

def students_list(request):
    students = (
	    {'id': 1,
	    'first_name': u'Валентин',
	    'last_name': u'Петренко',
	    'ticket': 5141,
	    'image': 'img/1.jpg'},
	    {'id': 2,
	    'first_name': u'Павло',
	    'last_name': u'Рудий',
	    'ticket': 5181,
	    'image': 'img/2.jpg'},
	    {'id': 1,
	    'first_name': u'Віталій',
	    'last_name': u'Семеной',
	    'ticket': u'5141M',
	    'image': 'img/3.jpg'},
	)
    return render(request, 'students/students_list.html', {'students': students})

def students_add(request):
    return render(request, '<h1>Student Add Form</h1>')

def students_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' % sid)

def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)

# Views for Groups

def groups_list(request):
    return HttpResponse('<h1>Groups List</h1>')

def groups_add(request):
    return render(request, '<h1>Group Add Form</h1>')

def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Group %s</h1>' % gid)

def groups_delete(request, gid):
    return HttpResponse('<h1>Delete Group %s</h1>' % gid)

