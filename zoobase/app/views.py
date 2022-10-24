from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm, AdminPasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.http import request
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, UpdateView
from django_filters.views import FilterView
from django_tables2 import SingleTableView
from django.contrib import admin
from .filters import StigmasFilter
from .forms import AddStigmaForm, LoginUserForm, ProfileUserForm, CustomAdminPasswordChangeForm
from .tables import SearchTable, HomeTable
from .utils import TableViewsMixin
from django.contrib.auth import views as auth_views


class Home(TableViewsMixin, SingleTableView):
    table_class = HomeTable
    template_name = 'app/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Волонтерская база животных Екатеринбурга'
        context['active'] = 'home'

        return context


class Search(TableViewsMixin, FilterView, SingleTableView):
    table_class = SearchTable
    template_name = 'app/search.html'
    filterset_class = StigmasFilter

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Поиск'
        context['active'] = 'search'
        if not context['object_list']:
            context['not_found'] = 'Сорян, ничего нет по этому запросу'
        return context


class AddPage(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    form_class = AddStigmaForm

    template_name = 'app/add_page.html'
    success_url = reverse_lazy('add_page')
    success_message = 'Запись добавлена в таблицу'

    def form_valid(self, form):
        # form.instance.created_by = self.request.user
        form.instance.author = '123123123'
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавить новую запись'
        context['active'] = 'add_page'

        return context


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'app/login.html'
    success_url = reverse_lazy('add_page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Авторизация'
        context['active'] = 'login'
        return context

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'slug': self.request.user})


# class ProfileUser(LoginRequiredMixin, CreateView):
#     form_class = ProfileUserForm
#     template_name = 'app/profile.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Профиль ' + str(self.request.user)
#
#         return context


class ProfileUser(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    """
    Страница профиля пользователя
    """
    model = User
    form_class = ProfileUserForm
    slug_field = 'username'
    slug_url_kwarg = 'slug'
    template_name = 'app/profile.html'
    success_message = 'Данные обновлены'

    # success_url =
    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'slug': self.request.user})



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Профиль ' + str(self.request.user)
        context['admin_url'] = True if str(self.request.user) == 'admin' else ''
        return context


def logout_user(request):
    logout(request)
    return redirect('login')

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     c_def = self.get_user_context(title="Авторизация")
    #     return dict(list(context.items()) + list(c_def.items()))

    # def post(self, request, *args, **kwargs):
    #     super(AddPage, self).post(request)


# def home_def(request):
#     table = StigmasTable(Stigmas.objects.all())
#     # paginator_class = LazyPaginator
#     table.paginate(page=request.GET.get("page", 1), per_page=5)
#     # filter = FilteredPersonListView
#     return render(request, "app/index.html", {"table": table})


# def index(request):
#     stigmas = Stigmas.objects.all()
#     table_class = StigmasTable
#     context = {
#         'stigmas': stigmas,
#     }
#
#     return render(request, 'app/index.html', context=context)


class ProfileUserPass(SuccessMessageMixin, LoginRequiredMixin,  auth_views.PasswordChangeView):
    """
    Страница смены пароля пользователя
    """

    form_class = CustomAdminPasswordChangeForm
    template_name = 'app/profile_pass.html'
    success_message = 'Данные (пароль) обновлены'

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'slug': self.request.user})
