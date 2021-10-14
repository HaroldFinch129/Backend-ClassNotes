from django.shortcuts import render
from .forms import StudentForm

def index(request):
    return render(request, 'student/index.html')

# from django.contrib import messages
def student_page(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Student added successful")
            return redirect('/student/')
    context = {
        'form': form
    }
    return render(request, 'student/student.html', context)


