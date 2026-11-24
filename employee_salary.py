import sys


def employee_details(name, employee_id, salary):
    return (
        f"Name: {name}\n"
        f"Employee ID: {employee_id}\n"
        f"Salary: {salary}"
    )


if __name__ == "__main__":
    name = sys.argv[1]
    employee_id = sys.argv[2]
    salary = sys.argv[3]
    print("\nEmployee Details")
    print("----------------")
    print(employee_details(name,employee_id,salary))