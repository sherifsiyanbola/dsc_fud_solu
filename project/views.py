from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from project.models import Project, Comment, Report, Year
from django.shortcuts import render
from project.forms import (
    YearForm,
    PmpProjectEditForm,
    MinistryProjectEditForm,
    CommentForm,
    FilterForm,
    ProjectForm,
    ReportForm,
    CommentEditForm,
    ReportEditForm,
    ProjectFilterForm
)
from .filters import ProjectFilter, ProjectFilterSet
from django_filters.views import FilterView
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
import datetime
from django.core.exceptions import ValidationError


def landpage(request):
    return render(request, 'landpage.html')


class YearCreate(LoginRequiredMixin, CreateView):
    model = Year
    form_class = YearForm
    template_name = 'year/year_form.html'

    def get_success_url(self):
        return reverse('project:year_detail', kwargs={'pk': self.object.pk})


class YearDetail(LoginRequiredMixin, DetailView):
    model = Year
    template_name = 'year/year_detail.html'


class YearDelete(LoginRequiredMixin, DeleteView):
    model = Year
    template_name = 'year/year_confirm_delete.html'
    success_url = reverse_lazy('project:year_list')


class YearUpdate(LoginRequiredMixin, UpdateView):
    model = Year
    form_class = YearForm
    template_name = 'year/year_form.html'

    def get_success_url(self):
        return reverse('project:year_detail', kwargs={'pk': self.object.pk})


class YearList(LoginRequiredMixin, ListView):
    model = Year
    template_name = 'year/year_list.html'


"""
class ProjectCreate(LoginRequiredMixin, CreateView):
    model = Project
    form_class = ProjectForm
   
    def get_success_url(self):
        return reverse('project:project_detail', kwargs={'pk' : self.object.pk})
"""


@login_required
def project_create(request):
    year = Year.objects.last()
    today = datetime.date.today()
    difference = year.date_closed - today

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.budget_year = year
            project.submittedBy = request.user
            # form.post_project()
            form.save()
            return redirect('project:project_detail', pk=project.pk)
    else:
        form = ProjectForm()

    context = {
        'difference': difference,
        'form': form
    }

    return render(request, 'project/project_form.html', context)


class ProjectDetail(LoginRequiredMixin, DetailView):
    model = Project


class ProjectDelete(LoginRequiredMixin, DeleteView):
    model = Project
    success_url = reverse_lazy('project:pmp_projects')

# project edits views


class MinistryProjectUpdate(LoginRequiredMixin, UpdateView):
    model = Project
    form_class = MinistryProjectEditForm

    def get_success_url(self):
        return reverse('project:project_detail', kwargs={'pk': self.object.pk})


class PmpProjectUpdate(LoginRequiredMixin, UpdateView):
    model = Project
    form_class = PmpProjectEditForm

    def get_success_url(self):
        return reverse('project:project_detail', kwargs={'pk': self.object.pk})


# project list views
"""
class PmpProjects(LoginRequiredMixin, ListView):
    model = Project
    template_name = 'project/pmp_projects.html'

"""


@login_required
def project_list(request):
    project_list = Project.objects.filter(status='approved')
    form = FilterForm()
    project_filter = ProjectFilter(request.GET, queryset=project_list)
    return render(request, 'project/project_list.html', {'filter': project_filter, 'form': form})


@login_required
def pmp_project_list(request):
    project_list = Project.objects.all()
    form = ProjectFilterForm()
    project_filter = ProjectFilterSet(request.GET, queryset=project_list)
    return render(request, 'project/pmp_projects.html', {'filter': project_filter, 'form': form})


"""
class MinistryProjects(LoginRequiredMixin, ListView):
    model = Project
    template_name = 'project/ministry_projects.html'

    def get_queryset(self):
        q1 = Project.objects.filter(
            ministry=self.request.user.ministry).filter(status='approved')
        q2 = Project.objects.filter(status='unreviewed').filter(
            ministry=self.request.user.ministry).filter(date__day__gte=datetime.date.today().day - 7)
        return q1.union(q2)
"""


@login_required
def ministry_project_list(request):
    q1 = Project.objects.filter(
        ministry=request.user.ministry).filter(status='approved')
    q2 = Project.objects.filter(status='unreviewed').filter(
        ministry=request.user.ministry).filter(date__day__gte=datetime.date.today().day - 7)
    q3 = q1.union(q2)
    form = ProjectFilterForm()
    project_filter = ProjectFilterSet(request.GET, queryset=q3)
    return render(request, 'project/ministry_projects.html', {'filter': project_filter, 'form': form})


"""
class GovernorList(LoginRequiredMixin, ListView):
    model = Project
    template_name = 'project/governor_projects.html'

    def get_queryset(self):
        q1 = Project.objects.filter(status='approved')
        q2 = Project.objects.filter(status='unreviewed').filter(
            date__day__lte=datetime.date.today().day - 14)
        return q1.union(q2)
"""


@login_required
def governor_project_list(request):
    q1 = Project.objects.filter(status='approved')
    q2 = Project.objects.filter(status='unreviewed').filter(
        date__day__gte=datetime.date.today().day - 14)
    q3 = q1.union(q2)
    form = ProjectFilterForm()
    project_filter = ProjectFilterSet(request.GET, queryset=q3)
    return render(request, 'project/governor_projects.html', {'filter': project_filter, 'form': form})


@login_required
def add_comment(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.project = project
            comment.picture = form.cleaned_data['picture']
            comment.submittedBy = request.user
            form.post_comment()
            comment.save()
            return redirect('project:comment_detail', pk=comment.pk)
            # return redirect('project:project_detail', pk=project.pk)

    else:
        form = CommentForm()
    return render(request, 'comment/comment_form.html', {'form': form})


class CommentDetail(LoginRequiredMixin, DetailView):
    model = Comment
    template_name = 'comment/comment_detail.html'


@login_required
def comment_delete(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('project:project_detail', pk=comment.project.pk)


class CommentUpdate(LoginRequiredMixin, UpdateView):
    model = Comment
    form_class = CommentEditForm
    template_name = 'comment/comment_form.html'

    def get_success_url(self):
        return reverse('project:comment_detail', kwargs={'pk': self.object.pk})


# reports views
class PmpReports(LoginRequiredMixin, ListView):
    model = Report
    template_name = 'report/pmp_reports.html'


class MinistryReports(LoginRequiredMixin, ListView):
    model = Report
    template_name = 'report/ministry_reports.html'

    def get_queryset(self):
        return Report.objects.filter(ministry=self.request.user.ministry).filter(status='approved')


class GovernorReports(LoginRequiredMixin, ListView):
    model = Report
    template_name = 'report/governor_reports.html'

    def get_queryset(self):
        return Report.objects.filter(status='approved')


class ReportCreate(LoginRequiredMixin, CreateView):
    model = Report
    form_class = ReportForm
    template_name = 'report/report_form.html'
    #fields = ['project','text', 'lga', 'ministry', 'picture', 'submitted_by', 'phone']

    def get_success_url(self):
        return reverse('project:report_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.submittedBy = self.request.user
        return super().form_valid(form)


class ReportDetail(LoginRequiredMixin, DetailView):
    model = Report
    template_name = 'report/report_detail.html'


class ReportDelete(LoginRequiredMixin, DeleteView):
    model = Report
    template_name = 'report/report_confirm_delete.html'
    success_url = reverse_lazy('project:pmp_reports')


class ReportUpdate(LoginRequiredMixin, UpdateView):
    model = Report
    form_class = ReportEditForm
    template_name = 'report/report_form.html'

    def get_success_url(self):
        return reverse('project:report_detail', kwargs={'pk': self.object.pk})


@login_required
def dashboard(request):
    context = {}
    context['all_projects'] = Project.objects.all().count()
    context['unreviewed_projects'] = Project.objects.filter(
        status='unreviewed').count()
    context['approved_projects'] = Project.objects.filter(
        status='approved').count()
    context['disapproved_projects'] = Project.objects.filter(
        status='disapproved').count()

    context['all_comments'] = Comment.objects.all().count()
    context['unreviewed_comments'] = Comment.objects.filter(
        status='unreviewed').count()
    context['approved_comments'] = Comment.objects.filter(
        status='approved').count()
    context['disapproved_comments'] = Comment.objects.filter(
        status='disapproved').count()

    context['all_reports'] = Report.objects.all().count()
    context['unreviewed_reports'] = Report.objects.filter(
        status='unreviewed').count()
    context['approved_reports'] = Report.objects.filter(
        status='approved').count()
    context['disapproved_reports'] = Report.objects.filter(
        status='disapproved').count()

    context['min_all_projects'] = Project.objects.filter(
        ministry=request.user.ministry).filter(status='approved').count()
    context['min_all_reports'] = Report.objects.filter(
        ministry=request.user.ministry).filter(status='approved').count()
    context['min_all_comments'] = Comment.objects.filter(
        status='approved').filter(project__ministry=request.user.ministry).count()
    return render(request, 'dashboard/dashboard.html', context)
