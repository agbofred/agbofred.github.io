########################################
# Name:
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
        # TODO: Initialize an empty set to store student IDs
        pass
    
    def enroll(self, student_id):
        """Adds a student ID to the system. Returns True if newly enrolled."""
        # TODO: Add student_id to set, return True if added, False if already present
        pass
    
    def is_enrolled(self, student_id):
        """Returns True if the student ID exists in the system."""
        # TODO: Check if student_id exists in the set
        pass
    
    def drop(self, student_id):
        """Removes a student ID. Returns True if removed, False if not found."""
        # TODO: Remove student_id from set, return True if removed, False if not found
        pass
    
    def get_enrollment_count(self):
        """Returns the total number of enrolled students."""
        # TODO: Return the number of students enrolled
        pass
    
    def get_all_students(self):
        """Returns a list of all enrolled student IDs."""
        # TODO: Convert the set to a list and return it
        pass


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
