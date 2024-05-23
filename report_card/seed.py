from faker import Faker  # used to fill fake data into the table   >pip install faker
fake = Faker()

import random
from .models import *
from django.db.models import Sum
from datetime import date

def create_subject_marks(n):
    try:
        student_objs = Student.objects.all()
        for student in student_objs:
            subjects = Subject.objects.all()
            for subject in subjects:
                SubjectMarks.objects.create(
                    subject = subject,
                    student = student,
                    marks = random.randint(0,100)
                )
    except Exception as e:
        print(e)



def seed_db(n=10)->None:
    try:

        for i in range(0, n):
            department_objs = Department.objects.all()
            if not department_objs:
                raise Exception("No departments found in the database.")
            
            random_index = random.randint(0, len(department_objs)-1)
            department = department_objs[random_index]

            student_id = f'S0{random.randint(100, 999)}'
            student_name = fake.name()
            student_email = fake.email()
            student_age = random.randint(20, 30)
            student_address = fake.address()

            student_id_obj = StudentID.objects.create(student_id = student_id)

            stduent_obj = Student.objects.create(
                department = department,
                student_id = student_id_obj,
                student_name = student_name,
                student_email = student_email,
                student_age = student_age,
                student_address = student_address    
        )
        print(f'Student created successfully.')

    except Exception as e:
        print(e)

# def generate_report_card():
#     current_rank = -1
#     ranks = Student.objects.annotate(marks = Sum('studentmarks__marks')).order_by('-marks', '-student_age')
    
#     i = 1
#     for rank in ranks:
#         ReportCard.objects.create(
#             student = rank,
#             student_rank = i
#         )   
#         i = i+1

def generate_report_card():
    today = date.today()
    
    # Check if report cards for today have already been generated
    if ReportCard.objects.filter(date_of_report_card_generation=today).exists():
        print("Report cards for today have already been generated.")
        return

    # Annotate students with their total marks and order them
    ranks = Student.objects.annotate(marks=Sum('studentmarks__marks')).order_by('-marks', '-student_age')
    
    current_rank = 1
    for rank in ranks:
        ReportCard.objects.create(
            student=rank,
            student_rank=current_rank,
            date_of_report_card_generation=today
        )
        current_rank += 1

    print("Report cards generated successfully.")