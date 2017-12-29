from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre
from django.views import generic


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