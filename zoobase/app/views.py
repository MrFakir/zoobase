from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django_filters.views import FilterView
from django_tables2 import SingleTableView

from .filters import StigmasFilter
from .forms import AddStigmaForm, LoginUserForm
from .tables import SearchTable, HomeTable
from .utils import TableViewsMixin


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


class AddPage(SuccessMessageMixin, CreateView):
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
