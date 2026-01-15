########################################
# Name: Instructor Solution
# Indicate any collaborators or tools used to assist you including AI:
# Estimated time spent (hrs):
########################################

"""
Problem 2: Student Enrollment System (Object-Oriented & Unordered Collections)

This module implements a student enrollment system using Object-Oriented Programming
with an unordered collection (set) to manage unique student IDs.
"""


class StudentEnrollment:
    """Manages student enrollment using a set for unique student IDs."""
    
    def __init__(self):
        """Initializes an empty enrollment system."""
        self.enrolled_students = set()
    
    def enroll(self, student_id):
        """Adds a student ID to the system. Returns True if newly enrolled."""
        initial_size = len(self.enrolled_students)
        self.enrolled_students.add(student_id)
        return len(self.enrolled_students) > initial_size
    
    def is_enrolled(self, student_id):
        """Returns True if the student ID exists in the system."""
        return student_id in self.enrolled_students
    
    def drop(self, student_id):
        """Removes a student ID. Returns True if removed, False if not found."""
        if student_id in self.enrolled_students:
            self.enrolled_students.remove(student_id)
            return True
        return False
    
    def get_enrollment_count(self):
        """Returns the total number of enrolled students."""
        return len(self.enrolled_students)
    
    def get_all_students(self):
        """Returns a list of all enrolled student IDs."""
        return list(self.enrolled_students)


def main():
    """
    Tests the StudentEnrollment system with sample operations.
    """
    print("Student Enrollment System")
    print("=" * 50)
    
    # Create enrollment system
    lab_section = StudentEnrollment()
    
    # Test enrollment
    print("\nEnrolling students:")
    students = [12345, 23456, 34567, 12345, 45678]
    for student_id in students:
        result = lab_section.enroll(student_id)
        status = "enrolled" if result else "already enrolled"
        print(f"  Student {student_id}: {status}")
    
    # Test enrollment check
    print(f"\nTotal enrolled: {lab_section.get_enrollment_count()}")
    print(f"Is student 12345 enrolled? {lab_section.is_enrolled(12345)}")
    print(f"Is student 99999 enrolled? {lab_section.is_enrolled(99999)}")
    
    # Test dropping
    print("\nDropping student 23456:")
    result = lab_section.drop(23456)
    print(f"  Drop successful: {result}")
    print(f"  New enrollment count: {lab_section.get_enrollment_count()}")
    
    # Display all enrolled students
    print(f"\nAll enrolled students: {sorted(lab_section.get_all_students())}")


if __name__ == "__main__":
    main()
