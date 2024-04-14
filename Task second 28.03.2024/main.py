from abc import ABC, abstractmethod
from typing import List, Dict, Any


class ReportGenerator(ABC):

    @abstractmethod
    def generate_report(self):
        pass


class EmployeeReportGenerator(ReportGenerator):

    def __init__(self, employee):
        self.employee = employee

    def generate_report(self) -> dict[str, Any]:
        return {'name': self.employee.name, 'surname': self.employee.surname }



class DepartmentReportGenerator(ReportGenerator):

    def __init__(self, department):
        self.department = department

    def generate_report(self) -> List[dict]:
        return [
            {
                'name': employer.name,
                'surname': employer.surname
            }
            for employer in self.department.employees_list
        ]


class Employee:

    def __init__(self, name: str, surname: str,
                 identifier: str, section: str):
        self.name = name
        self.surname = surname
        self.identifier = identifier
        self.section = section
        self.department = None

    def add_to_department(self, department):
        self.department = department
        department.employees_list.append(self)


class Department:

    def __init__(self, name: str):
        self.name = name
        self.employees_list = []

    def add_employee(self, employer: Employee):
        self.employees_list.append(employer)

