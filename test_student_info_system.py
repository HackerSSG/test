import unittest
from unittest.mock import patch
from student_info_system import Student, StudentInformationSystem

class TestStudentInformationSystem(unittest.TestCase):
    def setUp(self):
        self.sis = StudentInformationSystem()
        self.student1 = Student(1, "Alice", "A", "10th")
        self.student2 = Student(2, "Bob", "B", "11th")
        self.sis.add_student(self.student1)
        self.sis.add_student(self.student2)

    def test_add_student(self):
        self.assertEqual(len(self.sis.students), 2)
        self.sis.add_student(Student(3, "Charlie", "C", "12th"))
        self.assertEqual(len(self.sis.students), 3)

    def test_search_student(self):
        with patch("builtins.print") as mocked_print:
            self.sis.search_student(1)
            mocked_print.assert_called_with("Roll No: 1, Name: Alice, Grade: A, Class: 10th")

    def test_delete_student(self):
        self.sis.delete_student(1)
        self.assertEqual(len(self.sis.students), 1)
        self.assertEqual(self.sis.students[0].name, "Bob")

    def test_view_students(self):
        with patch("builtins.print") as mocked_print:
            self.sis.view_students()
            mocked_print.assert_any_call("Roll No: 1, Name: Alice, Grade: A, Class: 10th")
            mocked_print.assert_any_call("Roll No: 2, Name: Bob, Grade: B, Class: 11th")

if __name__ == "__main__":
    unittest.main()
