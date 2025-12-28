from program8 import employee_details

def test_employee_details():
    name = "Alice"
    emp_id = "E001"
    department = "Engineering"
    salary = 75000
    expected_output = (
        "Employee Name: Alice\n"
        "Employee ID: E001\n"
        "Department: Engineering\n"
        "Salary: 75000"
    )
    assert employee_details(name, emp_id, department, salary) == expected_output
