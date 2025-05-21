# Step 1: Define the base exception class
class Error(Exception):
    """Base class for custom exceptions"""
    pass

# Step 2: Define a specific exception class for invalid date of birth
class DobException(Error):
    """Raised when age is not within the allowed range"""

    def __init__(self, age, message="Age must be between 20 and 30 to apply for this exam."):
        self.age = age
        self.message = f"{message} You entered age: {age}."
        super().__init__(self.message)

# Step 3: Main logic to take user input and validate
def check_exam_eligibility():
    try:
        # Input birth year from user
        year_of_birth = int(input("Enter your year of birth: "))
        current_year = 2024
        age = current_year - year_of_birth

        # Validate age
        if 20 <= age <= 30:
            print(f"Your age is {age}. You are eligible to apply for the exam.")
        else:
            # Raise custom exception if not eligible
            raise DobException(age)

    except DobException as e:
        # Handle the custom exception
        print("Custom Exception Caught:")
        print(e)

    except ValueError:
        # Handle invalid input (e.g., non-integer input)
        print("Invalid input. Please enter a valid year.")

# Step 4: Run the function
if __name__ == "__main__":
    check_exam_eligibility()
