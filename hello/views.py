# hello/views.py
from django.shortcuts import render, redirect
from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data (you can save it to the database or send an email, etc.)
            
            # Redirect to the 'success_page' URL
            return redirect('success')  # Make sure 'success_page' is defined in your urls.py
    else:
        form = ContactForm()

    # Render the 'contact.html' template with the form
    return render(request, 'contact.html', {'form': form})

def success(request):
    return render(request, 'success.html')