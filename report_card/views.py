from django.shortcuts import render

from report_card.seed import generate_report_card
from .models import *
from django.core.paginator import Paginator

from django.db.models import Q, Sum #used to search any key or variable throughout the table not only for a particular variable... work as a OR option
# Create your views here.

def get_students(request):
    queryset = Student.objects.all()


    if request.GET.get('search'):
        search = request.GET.get('search')
        queryset = queryset.filter(
            Q(student_name__icontains = search) |
            Q(department__department__icontains = search) |
            Q(student_id__student_id__icontains = search) |
            Q(student_email__icontains = search)

        )

    paginator = Paginator(queryset, 25)  # Show 25 students per page.
    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)
    print(page_obj)
    return render(request, "students.html", {"queryset": page_obj})

def see_marks(request, student_id): #student_id is passed as a parameter
    queryset = SubjectMarks.objects.filter(student__student_id__student_id = student_id )
    total_marks = queryset.aggregate(total_marks = Sum('marks'))
   

    return render(request, "see_marks.html", {"queryset": queryset, "total_marks" : total_marks})





