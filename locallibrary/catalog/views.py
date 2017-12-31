from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
import datetime
from .forms import RenewBookForm


def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()  # The 'all()' is implied by default.

        # Number of visits to this view, as counted in the session variable.
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1

    return render(
        request,
        'index.html',
        context={'num_books': num_books, 'num_instances': num_instances, 'num_instances_available':
            num_instances_available, 'num_authors': num_authors, 'num_visits':num_visits})


class BookListView(generic.ListView):
    model = Book
    """
    Default template name and expected location: /application_name/templates/application_name/the_model_name_list.html
    Within the template you can access the list of books with the template variable named object_list OR book_list
    (i.e. generically "the_model_name_list").

    class BookListView(generic.ListView):
        model = Book
        context_object_name = 'my_book_list'   # your own name for the list as a template variable
        queryset = Book.objects.filter(title__icontains='war')[:5] # Get 5 books containing the title war
        template_name = 'books/my_arbitrary_template_name_list.html'  # Specify your own template name/location

     Override the get_queryset() method to change the list of records returned. This is more flexible than just setting
     the queryset attribute as in the preceding code fragment

    class BookListView(generic.ListView):
    model = Book
        def get_queryset(self):
            return Book.objects.filter(title__icontains='war')[:5] # Get 5 books containing the title war

     Override get_context_data() in order to pass additional context variables to the template. The code below shows how
     to add a variable named "some_data" to the context (it would then be available as a template variable).

    class BookListView(generic.ListView):
    model = Book
        def get_context_data(self, **kwargs):
            # Call the base implementation first to get a context
            context = super(BookListView, self).get_context_data(**kwargs)
            # Get the blog from id and add it to the context
            context['some_data'] = 'This is just some data'
            return context
   """


class BookDetailView(generic.DetailView):
    model = Book

    """
    def book_detail_view(request,pk):
        try:
            book_id=Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise Http404("Book does not exist")
        #book_id=get_object_or_404(Book, pk=pk)
        return render(
            request,
            'catalog/book_detail.html',
            context={'book':book_id,})
    """


@permission_required('catalog.can_mark_returned')
def renew_book_librarian(request, pk):
    """
    View function for renewing a specific BookInstance by librarian
    """
    book_inst=get_object_or_404(BookInstance, pk = pk)

    # If this is a POST request then process the Form data
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request (binding):
        form = RenewBookForm(request.POST)
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            book_inst.due_back = form.cleaned_data['renewal_date']
            book_inst.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = RenewBookForm(initial={'renewal_date': proposed_renewal_date,})

    return render(request, 'catalog/book_renew_librarian.html', {'form': form, 'bookinst':book_inst})


from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class AuthorCreate(CreateView):
    model = Author
    fields = '__all__'
    initial={'date_of_death':'12/10/2016',}

class AuthorUpdate(UpdateView):
    model = Author
    fields = ['first_name','last_name','date_of_birth','date_of_death']

class AuthorDelete(DeleteView):
    model = Author
    """
    Use the reverse_lazy() function to redirect to our author list after an author has been deleted
    reverse_lazy() is a lazily executed version of reverse(), used to provide a URL to a class-based view attribute
    """
    success_url = reverse_lazy('authors')


class AuthorListView(generic.ListView):
    model = Author


class AuthorDetailView(generic.DetailView):
    model = Author