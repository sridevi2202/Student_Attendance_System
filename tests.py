import unittest
from code import StudentAttendanceSystem
class TestStudentAttendanceSystem(unittest.TestCase):

    def setUp(self):
        self.system = StudentAttendanceSystem("Math101")

    def test_add_student(self):
        self.system.add_student(1, "Alice")
        self.assertEqual(len(self.system.students), 1)
        self.assertEqual(self.system.students[1], "Alice")

    def test_remove_student(self):
        self.system.add_student(1, "Alice")
        self.system.remove_student(1)
        self.assertEqual(len(self.system.students), 0)

    def test_mark_attendance(self):
        self.system.add_student(1, "Alice")
        self.system.mark_attendance(1, "2023-12-08")
        self.assertEqual(len(self.system.attendance_data[1]), 1)

    def test_view_attendance_history(self):
        self.system.add_student(1, "Alice")
        self.system.mark_attendance(1, "2023-12-08")
        self.assertEqual(self.system.view_attendance_history(1), ["2023-12-08"])

    def test_calculate_attendance_percentage(self):
        self.system.add_student(1, "Alice")
        self.system.mark_attendance(1, "2023-12-08")
        self.system.mark_attendance(1, "2023-12-09")
        self.assertEqual(self.system.calculate_attendance_percentage(1), 100.0)

    def test_generate_attendance_report(self):
        self.system.add_student(1, "Alice")
        self.system.add_student(2, "Bob")
        self.system.mark_attendance(1, "2023-12-08")
        self.system.mark_attendance(2, "2023-12-08")
        report = self.system.generate_attendance_report()
        self.assertEqual(report["Alice"], 100.0)
        self.assertEqual(report["Bob"], 100.0)

    def test_set_custom_attendance_rule(self):
        self.system.add_student(1, "Alice")
        self.system.set_custom_attendance_rule(1, "Custom Rule")
        self.assertEqual(self.system.custom_rules[1], "Custom Rule")

    def test_send_attendance_notification(self):
        self.system.add_student(1, "Alice")
        self.system.add_notification(1, "Notification")
        self.assertEqual(self.system.send_attendance_notification(1), "Notification")

    def test_view_class_schedule(self):
        self.system.add_class_schedule("Monday", "11:00")
        self.assertEqual(self.system.view_class_schedule(), {"Monday": ["11:00"]})

    def test_add_class_schedule(self):
        self.system.add_class_schedule("Monday", "11:00")
        self.assertEqual(self.system.view_class_schedule(), {"Monday": ["11:00"]})

    def test_set_student_status(self):
        self.system.add_student(1, "Alice")
        self.system.set_student_status(1, "present")
        self.assertEqual(self.system.get_student_status(1), "present")

    def test_get_student_status(self):
        self.system.add_student(1, "Alice")
        self.system.set_student_status(1, "absent")
        self.assertEqual(self.system.get_student_status(1), "absent")

    def test_get_total_students(self):
        self.system.add_student(1, "Alice")
        self.system.add_student(2, "Bob")
        self.assertEqual(self.system.get_total_students(), 2)

    def test_get_total_attendance_days(self):
        self.system.add_student(1, "Alice")
        self.system.mark_attendance(1, "2023-12-08")
        self.system.mark_attendance(1, "2023-12-09")
        self.assertEqual(self.system.get_total_attendance_days(1), 2)

    def test_get_student_name(self):
        self.system.add_student(1, "Alice")
        self.assertEqual(self.system.get_student_name(1), "Alice")

    def test_view_students(self):
        self.system.add_student(1, "Alice")
        self.system.add_student(2, "Bob")
        students = list(self.system.view_students())
        self.assertIn("Alice", students)
        self.assertIn("Bob", students)

    def test_reset_attendance(self):
        self.system.add_student(1, "Alice")
        self.system.mark_attendance(1, "2023-12-08")
        self.system.reset_attendance(1)
        self.assertEqual(len(self.system.view_attendance_history(1)), 0)

    def test_set_custom_rule(self):
        self.system.add_student(1, "Alice")
        self.system.set_custom_rule(1, "Custom Rule")
        self.assertEqual(self.system.get_custom_rule(1), "Custom Rule")

    def test_add_notification(self):
        self.system.add_student(1, "Alice")
        self.system.add_notification(1, "Notification")
        self.assertEqual(self.system.view_notifications(1), "Notification")

    def test_view_notifications(self):
        self.system.add_student(1, "Alice")
        self.system.add_notification(1, "Notification")
        self.assertEqual(self.system.view_notifications(1), "Notification")

    def test_set_student_custom_data(self):
        self.system.add_student(1, "Alice")
        self.system.set_student_custom_data(1, "age", 20)
        self.assertEqual(self.system.get_student_custom_data(1, "age"), 20)

    def test_get_student_custom_data(self):
        self.system.add_student(1, "Alice")
        self.system.set_student_custom_data(1, "age", 20)
        self.assertEqual(self.system.get_student_custom_data(1, "age"), 20)

    def test_add_absence_reason(self):
        self.system.add_student(1, "Alice")
        self.system.mark_attendance(1, "2023-12-08")
        self.system.add_absence_reason(1, "2023-12-08", "Sick")
        self.assertEqual(self.system.get_absence_reason(1, "2023-12-08"), "Sick")

    def test_get_absence_reason(self):
        self.system.add_student(1, "Alice")
        self.system.mark_attendance(1, "2023-12-08")
        self.system.add_absence_reason(1, "2023-12-08", "Sick")
        self.assertEqual(self.system.get_absence_reason(1, "2023-12-08"), "Sick")

    def test_view_student_custom_data(self):
        self.system.add_student(1, "Alice")
        self.system.set_student_custom_data(1, "age", 20)
        custom_data = self.system.view_student_custom_data(1)
        self.assertEqual(custom_data, {"age": 20})

    def test_view_student_absence_reasons(self):
        self.system.add_student(1, "Alice")
        self.system.mark_attendance(1, "2023-12-08")
        self.system.add_absence_reason(1, "2023-12-08", "Sick")
        absence_reasons = self.system.view_student_absence_reasons(1)
        self.assertEqual(absence_reasons, {"2023-12-08": "Sick"})

    def test_remove_student_custom_data(self):
        self.system.add_student(1, "Alice")
        self.system.set_student_custom_data(1, "age", 20)
        self.system.remove_student_custom_data(1, "age")
        self.assertIsNone(self.system.get_student_custom_data(1, "age"))

    def test_remove_absence_reason(self):
        self.system.add_student(1, "Alice")
        self.system.mark_attendance(1, "2023-12-08")
        self.system.add_absence_reason(1, "2023-12-08", "Sick")
        self.system.remove_absence_reason(1, "2023-12-08")
        self.assertIsNone(self.system.get_absence_reason(1, "2023-12-08"))

if __name__ == '__main__':
    unittest.main()
