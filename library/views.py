from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Author
from .forms import BookForm

def home(request):
    books = Book.objects.all()
    return render(request, 'library/home.html', {'books': books})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'library/book_detail.html', {'book': book})

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookForm()
    return render(request, 'library/add_book.html', {'form': form})
