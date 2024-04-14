from main import Department, DepartmentReportGenerator, \
    Employee, EmployeeReportGenerator

def main() -> None:
    d1 = Department('BACKEND')
    d2 = Department('FRONTEND')
    p1 = Employee('Paweł', 'Rutkowski', '515651', 'Tsdfa')
    p2 = Employee('Patryk', 'Rutkowski', '515156', 'Tasfd')
    p1.add_to_department(d1)
    p2.add_to_department(d1)
    print(EmployeeReportGenerator(p1).generate_report())
    print(DepartmentReportGenerator(d1).generate_report())
    print(DepartmentReportGenerator(d2).generate_report())


if __name__ == '__main__':
    main()
