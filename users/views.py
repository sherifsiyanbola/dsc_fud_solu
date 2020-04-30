from django.views.generic import TemplateView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from users.forms import (
    MinistryUserForm,
    GovernorForm,
    PMPForm,
    BudgetForm,
    DueProcessForm,
    EditProfileForm
)
from users.models import Profile
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.views import generic
from .forms import CustomUserCreationForm, CustomUserChangeForm
User = get_user_model()


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


@login_required
def profile(request):
    args = {'user': request.user}
    return render(request, 'registration/profile.html')


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(
            request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('users:profile')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'registration/edit_profile.html', args)


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            update_session_auth_hash(request, form.user)
            form.save()
            return redirect('login')
        else:
            return redirect('change_password')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'registration/change_password.html', args)


@login_required
def user_list(request):
    context = {}
    context['users'] = User.objects.all().order_by('-created')
    context['title'] = 'Users'
    return render(request, 'users/index.html', context)


@login_required
def user_details(request, id=None):
    context = {}
    context['user'] = get_object_or_404(User, id=id)
    return render(request, 'users/details.html', context)


# ministry user add
@login_required
def ministryuser_add(request):
    context = {}
    if request.method == 'POST':
        user_form = MinistryUserForm(request.POST, request.FILES)
        context['user_form'] = user_form
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('users:user_list'))
        else:
            return render(request, 'users/add.html', context)
    else:
        user_form = MinistryUserForm()
        context['user_form'] = user_form
        return render(request, 'users/add.html', context)

# GOVERNOR ADD
@login_required
def governor_add(request):
    context = {}
    if request.method == 'POST':
        user_form = GovernorForm(request.POST, request.FILES)
        context['user_form'] = user_form
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('users:user_list'))
        else:
            return render(request, 'users/add.html', context)
    else:
        user_form = GovernorForm()
        context['user_form'] = user_form
        return render(request, 'users/add.html', context)


# PMP ADD
@login_required
def pmp_add(request):
    context = {}
    if request.method == 'POST':
        user_form = PMPForm(request.POST, request.FILES)
        context['user_form'] = user_form
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('users:user_list'))
        else:
            return render(request, 'users/add.html', context)
    else:
        user_form = PMPForm()
        context['user_form'] = user_form
        return render(request, 'users/add.html', context)


# Budget & eco planning ADD
@login_required
def budget_add(request):
    context = {}
    if request.method == 'POST':
        user_form = BudgetForm(request.POST, request.FILES)
        context['user_form'] = user_form
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('users:user_list'))
        else:
            return render(request, 'users/add.html', context)
    else:
        user_form = BudgetForm()
        context['user_form'] = user_form
        return render(request, 'users/add.html', context)


# due process ADD
@login_required
def due_process_add(request):
    context = {}
    if request.method == 'POST':
        user_form = DueProcessForm(request.POST, request.FILES)
        context['user_form'] = user_form
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('users:user_list'))
        else:
            return render(request, 'users/add.html', context)
    else:
        user_form = DueProcessForm()
        context['user_form'] = user_form
        return render(request, 'users/add.html', context)


@login_required
def user_edit(request, id=None):
    user = get_object_or_404(User, id=id)
    if request.method == 'POST':
        user_form = MinistryUserForm(
            request.POST, request.FILES, instance=user)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('users:user_list'))
        else:
            return render(request, 'users/edit.html', {'user_form': user_form})
    else:
        user_form = MinistryUserForm(instance=user)
        return render(request, 'users/edit.html', {'user_form': user_form})


@login_required
def user_delete(request, id=None):
    user = get_object_or_404(User, id=id)
    if request.method == 'POST':
        user.delete()
        return HttpResponseRedirect(reverse('users:user_list'))
    else:
        context = {}
        context['user'] = user
        return render(request, 'users/delete.html', context)
