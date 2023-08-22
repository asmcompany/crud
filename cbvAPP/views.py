from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Student
from django.db.models import Sum
from django.core.paginator import Paginator

class StudentListViwe(ListView):
    model = Student 
    paginate_by = 5
   

class StudentDetailViwe(DetailView):
    model = Student
    #default template_name is student_detail.html
    #default contex_object_name is student


class StudentCreateViwe(CreateView):
    model = Student
    fields = ("firstName","lastName","enter","testScore","Amount")
    #default template_name is student_form.html
    #default contex_object_name is form


class StudentUpdateViwe(UpdateView):
    model = Student
    fields = ("firstName","lastName","enter","testScore","Amount")


class StudentDeleteViwe(DeleteView):
    model = Student
    success_url = reverse_lazy("student")
    #default template_name is student_confirm_delete.html
    #default contex_object_name is student


