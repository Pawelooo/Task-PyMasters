from abc import ABC, abstractmethod
from typing import List


class ReportGenerator(ABC):

    @abstractmethod
    def generate_report(self):
        pass


class EmployeeReportGenerator(ReportGenerator):

    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    def generate_report(self) -> List[dict]:
        return [{'name': self.name, 'surname': self.surname}]


class DepartmentReportGenerator(ReportGenerator):

    def __init__(self, lst_employer: List):
        self.lst_employer = lst_employer

    def generate_report(self) -> List[dict]:
        return [{'name': employer.name, 'surname': employer.surname}
                for employer in self.lst_employer]


class Employee:

    def __init__(self, name: str, surname: str,
                 identifier: str, section: str,
                 generator):
        self.name = name
        self.surname = surname
        self.identifier = identifier
        self.section = section
        self.generator = generator(self.name, self.surname)

    def generate_report(self):
        return self.generator.report_generator()


class Department:

    def __init__(self, name: str, generator_type: type):
        self.name = name
        self.employees_list = [Employee('Test', 'New', '635253', 'Engine',
                                      EmployeeReportGenerator)]
        self.report_generator = generator_type(self.employees_list)

    def report(self):
        return self.report_generator().generate_report()

    def add_employee(self, employer: Employee):
        self.employees_list.append(employer)
