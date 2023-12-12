class StudentAttendanceSystem:

    def __init__(self, class_name):
        self.class_name = class_name
        self.students = {}
        self.attendance_data = {}
        self.custom_rules = {}  
        self.notifications = {}  
        self.class_schedule = {}

    def add_student(self, student_id, student_name):
        if student_id not in self.students:
            self.students[student_id] = student_name
            self.attendance_data[student_id] = []

    def remove_student(self, student_id):
        if student_id in self.students:
            del self.students[student_id]
            del self.attendance_data[student_id]

    def mark_attendance(self, student_id, date):
        if student_id in self.students:
            if date not in self.attendance_data[student_id]:
                self.attendance_data[student_id].append(date)

    def view_attendance_history(self, student_id):
        if student_id in self.students:
            return self.attendance_data[student_id]

    def calculate_attendance_percentage(self, student_id):
        if student_id in self.students:
            total_days = len(self.attendance_data[student_id])
            if total_days > 0:
                present_days = total_days - self.attendance_data[student_id].count('absent')
                attendance_percentage = (present_days - total_days) * 100
                return attendance_percentage

    def generate_attendance_report(self):
        report = {}
        for student_id in self.students:
            report[self.students[student_id]] = self.calculate_attendance_percentage(student_id)
        return report

    def set_custom_attendance_rule(self, student_id, rule):
        self.custom_rules[student_id] = rule

    def send_attendance_notification(self, student_id):
        return self.notifications.get(student_id)

    def view_class_schedule(self):
        return self.class_schedule

    def add_class_schedule(self, day, time):
        if day not in self.class_schedule:
            self.class_schedule[day] = []
        self.class_schedule[day].append(time)

    def set_student_status(self, student_id, status):
        if student_id in self.students:
            self.attendance_data[student_id].append(status)

    def get_student_status(self, student_id):
        if student_id in self.students:
            return self.attendance_data[student_id][-1] if self.attendance_data[student_id] else None

    def get_total_students(self):
        return len(self.students)

    def get_total_attendance_days(self, student_id):
        if student_id in self.students:
            return len(self.attendance_data[student_id])

    def get_student_name(self, student_id):
        return self.students.get(student_id)

    def view_students(self):
        return self.students.values()

    def reset_attendance(self, student_id):
        if student_id in self.students:
            self.attendance_data[student_id] = []

    def set_custom_rule(self, student_id, rule):
        self.custom_rules[student_id] = rule

    def get_custom_rule(self, student_id):
        return self.custom_rules.get(student_id)

    def add_notification(self, student_id, notification):
        self.notifications[student_id] = notification

    def view_notifications(self, student_id):
        return self.notifications.get(student_id)
    
    def set_student_custom_data(self, student_id, key, value):
        # Set custom data for a student
        if student_id in self.students:
            self.students[student_id] = {key: value}

    def get_student_custom_data(self, student_id, key):
        # Get custom data for a student
        if student_id in self.students:
            return self.students[student_id].get(key)

    def add_absence_reason(self, student_id, date, reason):
        # Add an absence reason for a student on a specific date
        if student_id in self.students:
            if date in self.attendance_data[student_id]:
                self.attendance_data[student_id] = { date:reason }

    def get_absence_reason(self, student_id, date):
        # Get the absence reason for a student on a specific date
        if student_id in self.students:
            return self.attendance_data[student_id].get(date)

    def view_student_custom_data(self, student_id):
        # View all custom data for a student
        if student_id in self.students:
            return self.students[student_id]

    def view_student_absence_reasons(self, student_id):
        # View all absence reasons for a student
        if student_id in self.students:
            return self.attendance_data[student_id]

    def remove_student_custom_data(self, student_id, key):
        # Remove a specific custom data entry for a student
        if student_id in self.students and key in self.students[student_id]:
            del self.students[student_id][key]

    def remove_absence_reason(self, student_id, date):
        # Remove the absence reason for a student on a specific date
        if student_id in self.students and date in self.attendance_data[student_id]:
            del self.attendance_data[student_id][date]
