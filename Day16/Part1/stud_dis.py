#Question: Ek dictionary banao jisme 5 students ke naam aur marks ho — highest marks wala student nikalo

student_marks={
    "Prashant" : 77,
    "Zoiab" :78,
    "Abhishek" :87,
    "Aashish" :91,
    "Rahul" :85
}
highest=0
for name,marks in student_marks.items():
    if marks>highest:
        highest=marks
        Topper=name
    else:
        pass
print(f"Topper is {Topper} with marks {highest}")