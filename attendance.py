"""
Attendance Register

Task:
- Track attendance of students.
- Use a dictionary { "student_id": {"name": str, "present_days": list, "absent_days": list} }
- Functions to mark attendance, check history, and get reports.
- Use your head/logic to mark multiple students at once.
- Use **kwargs for flexible reporting (e.g., only_present=True).

// NOT FOR THIS ASSIGNMENT
Future OOP Extension:
- Student class with mark_present() and mark_absent().
- AttendanceRegister class that manages records.
"""



from datetime import date
attendance = {}

def mark_attendance(sid, name, status):
    today = str(date.today())
    if sid not in attendance:
        attendance[sid] = {"name": name, "present": [], "absent": []}
    if status == "p": attendance[sid]["present"].append(today)
    else: attendance[sid]["absent"].append(today)

def show_report():
    for sid, rec in attendance.items():
        print(f"{sid}-{rec['name']}: {len(rec['present'])}P, {len(rec['absent'])}A")

while True:
    sid = input("ID (q=quit): ")
    if sid == "q": break
    name = input("Name: ")
    status = input("Present/Absent (p/a): ")
    mark_attendance(sid, name, status)

show_report()

