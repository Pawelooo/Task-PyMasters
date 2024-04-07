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

    def generate_report(self):
        return {'name': self.name, 'surname': self.surname}


class DepartmentReportGenerator(ReportGenerator):

    def __init__(self, lst_employer: List):
        self.lst_employer = lst_employer

    def generate_report(self):
        return [{'name': employer.name, 'surname': employer.surname}
                for employer in self.lst_employer]


class Employee:

    def __init__(self, name: str, surname: str,
                 identifier: str, section: str,
                 generator: ReportGenerator):
        self.name = name
        self.surname = surname
        self.identifier = identifier
        self.section = section
        self.generator = generator

    def generate_report(self):
        return self.generator(self.name, self.surname).generate_report()


class Department:

    def __init__(self, name: str, generator: ReportGenerator):
        self.name = name
        self.workers_list = [Employee('Test', 'New', '635253', 'Engine',
                                      EmployeeReportGenerator)]
        self.generate = generator

    def report(self):
        return self.generate(self.workers_list).generate_report()

    def add_new_person(self, employer: Employee):
        self.workers_list.append(employer)