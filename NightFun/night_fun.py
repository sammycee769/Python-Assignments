students = [
("Alice", 78),
("Bob", 45),
("Charlie", 90),
("Diana", 62),
("Kent", 30)
]

def unpack_student_data(student_data):
    for name, score in student_data:
        print(f"Name: {name}, Score: {score}")

def unpack_student_data_with_scores_above_60(student_data):
   
    unpacked = [ student_data[0] for student_data in student_data if student_data[1] > 60 ]
    return unpacked

def count_students_above_60(student_data):
    count = 0
    for _, score in student_data:
        if score > 50:
            count += 1
    return count

# unpacked_students = unpack_student_data(students)
unpacked_students_above_60 = unpack_student_data_with_scores_above_60(students)
print(unpacked_students_above_60)
# print(count_students_above_60(students))

products = [
("Laptop", 1200),
("Mouse", 25),
("Keyboard", 45),
("Monitor", 300),
("USB Cable", 10)]

def get_products_above_100(product_data):
    return product_data[1] > 100

def sum_all_product_prices(product_data):
    total = 0
    for _, price in product_data:
        total += price
    return total

def unpack_product_data(product_data):
    for name, price in product_data:
        print(f"Product: {name}-Price: {price}")

# unpack_product_data(products)
# print(sum_all_product_prices(products))
# print(list(filter(get_products_above_100, products)))

points = [ (2, 3),
(-1, 4),
(5, -6),
(0, 7),
(-3, -2)
]

def unpack_point_data(point_data):
    unpacked_data=[ (x_coordinate,y_coordinate) for x_coordinate, y_coordinate in point_data if x_coordinate >= 0 and y_coordinate >= 0 ]   
    return unpacked_data

# print(unpack_point_data(points))     

employees = [
("John", "IT", 50000),
("Jane", "HR", 45000),
("Mike", "IT", 60000),
("Sara", "Finance", 70000)
]

def unpack_employee_data(employee_data):
    for name, department, salary in employee_data:
        print(f"Name: {name}, Department: {department}, Salary: {salary}")

def it_department_employees(employee_data):
    it_employees = [ (name, department, salary) for name, department, salary in employee_data if department == "IT" ]
    return it_employees

def it_department_employees_earning_above_55000(employee_data):
    it_high_earners = [ (name, department, salary) for name, department, salary in employee_data if department == "IT" and salary > 55000 ]
    return it_high_earners

# unpack_employee_data(employees)
# print(it_department_employees(employees))
# print(it_department_employees_earning_above_55000(employees))