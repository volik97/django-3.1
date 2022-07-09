from django.shortcuts import render
import datetime
from books.models import Book


def books_view(request):
    template = 'books/books_list.html'
    pub_d = request.GET.get('pub_date')

    try:
        pub_d = datetime.datetime.strptime(pub_d, '%Y-%m-%d')
        context = {
            'books': Book.objects.filter(pub_date__exact=pub_d).order_by('pub_date')
        }
    except TypeError:
        context = {
            'books': Book.objects.order_by('pub_date').all()
        }
    return render(request, template, context)


