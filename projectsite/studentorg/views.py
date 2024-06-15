from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from studentorg.models import Organization, OrgMember, Student, College, Program
from studentorg.forms import OrganizationForm, OrgMemberForm, StudentForm, CollegeForm, ProgramForm
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from typing import Any
from django.db.models.query import QuerySet
from django.db.models import Q

from django.forms import CharField
from django.db import connection
from django.http import JsonResponse
from django.db.models.functions import ExtractMonth
from django.db.models import Count
from datetime import datetime
from django.db import models

@method_decorator(login_required, name='dispatch')

class HomePageView(ListView):
    model = Organization
    context_object_name = 'home'
    template_name = "home.html"

class ChartView(ListView):
    template_name = 'chart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self, *args, **kwargs):
        pass

def pieChart(request):
    num_college = College.objects.annotate(student_count=models.Count('program__student'))
    labels = [college.college_name for college in num_college]
    counts = [college.student_count for college in num_college]
    
    return JsonResponse({'college_labels': labels, 'college_counts': counts})

def doughnutChart(request):
    students_in_program = Student.objects.values('program__prog_name').annotate(count=Count('id'))
    labels = [item['program__prog_name'] for item in students_in_program]
    counts = [item['count'] for item in students_in_program]

    data = {
        'labels': labels,
        'counts': counts,
    }
    return JsonResponse(data)

def barChart(request):
    org_member = OrgMember.objects.values('organization__name').annotate(count=Count('student'))
    labels = [item['organization__name'] for item in org_member]
    counts = [item['count'] for item in org_member]

    data = {
        'labels': labels,
        'counts': counts,
    }
    return JsonResponse(data)

def lineChart(request):
    org_join_counts = OrgMember.objects.values('date_joined').annotate(count=Count('student')).order_by('date_joined')
    labels = [item['date_joined'].strftime('%Y-%m-%d') for item in org_join_counts]
    counts = [item['count'] for item in org_join_counts]

    data = {
        'labels': labels,
        'counts': counts,
    }
    return JsonResponse(data)

def multibarChart(request):
    org_join_counts = OrgMember.objects.values('date_joined').annotate(count=Count('student')).order_by('date_joined')
    labels = [item['date_joined'].strftime('%Y-%m-%d') for item in org_join_counts]
    counts = [item['count'] for item in org_join_counts]

    data = {
        'labels': labels,
        'counts': counts,
    }
    return JsonResponse(data)

class OrganizationList(ListView):
    model = Organization
    context_object_name = 'organization'
    template_name = 'org_list.html'
    paginate_by = 5

    def get_queryset(self, *args, **kwargs):
         qs = super(OrganizationList, self).get_queryset(*args, **kwargs)
         if self.request.GET.get("q") != None:
             query = self.request.GET.get('q')
             qs = qs.filter(Q(name__icontains=query) |
                            Q(description__icontains=query))
         return qs

class OrganizationCreateView(CreateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'org_add.html'
    success_url = reverse_lazy('organization-list')

class OrganizationUpdateView(UpdateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'org_edit.html'
    success_url = reverse_lazy('organization-list')

class OrganizationDeleteView(DeleteView):
    model = Organization
    template_name = 'org_del.html'
    success_url = reverse_lazy('organization-list')

class OrgMemberList(ListView):
    model = OrgMember
    context_object_name = 'orgmember'
    template_name = 'orgmember_list.html'
    paginate_by = 10

class OrgMemberCreateView(CreateView):
    model = OrgMember
    form_class = OrgMemberForm
    template_name = 'orgmember_add.html'
    success_url = reverse_lazy('orgmember-list')

class OrgMemberUpdateView(UpdateView):
    model = OrgMember
    form_class = OrgMemberForm
    template_name = 'orgmember_edit.html'
    success_url = reverse_lazy('orgmember-list')

class OrgMemberDeleteView(DeleteView):
    model = OrgMember
    template_name = 'orgmember_del.html'
    success_url = reverse_lazy('orgmember-list')

class StudentList(ListView):
    model = Student
    context_object_name = 'student'
    template_name = 'student_list.html'
    paginate_by = 10

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'student_add.html'
    success_url = reverse_lazy('student-list')

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'student_edit.html'
    success_url = reverse_lazy('student-list')

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'student_del.html'
    success_url = reverse_lazy('student-list')

class CollegeList(ListView):
    model = College
    context_object_name = 'college'
    template_name = 'college_list.html'
    paginate_by = 10

class CollegeCreateView(CreateView):
    model = College
    form_class = CollegeForm
    template_name = 'college_add.html'
    success_url = reverse_lazy('college-list')

class CollegeUpdateView(UpdateView):
    model = College
    form_class = CollegeForm
    template_name = 'college_edit.html'
    success_url = reverse_lazy('college-list')

class CollegeDeleteView(DeleteView):
    model = College
    template_name = 'college_del.html'
    success_url = reverse_lazy('college-list')

class ProgramList(ListView):
    model = Program
    context_object_name = 'program'
    template_name = 'program_list.html'
    paginate_by = 10

class ProgramCreateView(CreateView):
    model = Program
    form_class = ProgramForm
    template_name = 'program_add.html'
    success_url = reverse_lazy('program-list')

class ProgramUpdateView(UpdateView):
    model = Program
    form_class = ProgramForm
    template_name = 'program_edit.html'
    success_url = reverse_lazy('program-list')

class ProgramDeleteView(DeleteView):
    model = Program
    template_name = 'program_del.html'
    success_url = reverse_lazy('program-list')