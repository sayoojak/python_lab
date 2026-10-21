students = {
    "Anu": (85, 90),
    "Binu": (85, 80),
    "Ciya": (95, 85),
    "David": (70, 95)
}
 
sorted_students = sorted(
    students.items(),
    key=lambda item: (-item[1][0], item[1][1])
)
 
for name, marks in sorted_students:
    print(name, marks)
