"""
Contoh penggunaan Creational Pattern (Factory)

Factory Pattern digunakan untuk membuat sebuah class yang bertanggung jawab untuk membuat instance dari class lain.
Ini biasa digunakan untuk membuat instance dari class yang memiliki banyak subclass.
Untuk case kali ini saya menggunakan factory pattern untuk membuat instance dari class Developer, Tester,
dan Analyst sebagai Worker.
"""

from abc import ABC, abstractmethod
from typing import List


class Worker(ABC):
    # Interface Worker memiliki tiga method abstract yaitu name(), work() dan get_skills().
    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def work(self) -> str:
        pass

    @abstractmethod
    def get_skills(self) -> List[str]:
        pass


class Developer(Worker):
    # Developer adalah salah satu class yang mengimplementasikan interface Worker.
    def name(self) -> str:
        return 'Developer'

    def work(self) -> str:
        return 'Developing'

    def get_skills(self) -> List[str]:
        return ['Python', 'JavaScript', 'PHP']


class Tester(Worker):
    # Tester adalah salah satu class yang mengimplementasikan interface Worker.
    def name(self) -> str:
        return 'Tester'

    def work(self) -> str:
        return 'Testing'

    def get_skills(self) -> List[str]:
        return ['Selenium', 'Junit', 'Jmeter', 'TestNG']


class Analyst(Worker):
    # Analyst adalah salah satu class yang mengimplementasikan interface Worker.
    def name(self) -> str:
        return 'Analyst'

    def work(self) -> str:
        return 'Analyzing'

    def get_skills(self) -> List[str]:
        return ['Data Analysis', 'Requirement Analysis', 'UML']


class WorkerFactory:
    # WorkerFactory adalah factory class yang bertanggung jawab untuk membuat instance dari class Developer, Tester,
    # dan Analyst.
    def create_worker(self, worker_type: str) -> Worker:
        if worker_type == 'developer':
            return Developer()
        elif worker_type == 'tester':
            return Tester()
        elif worker_type == 'analyst':
            return Analyst()
        raise ValueError(f'Invalid Worker Type: {worker_type}')


if __name__ == '__main__':
    # Contoh Penerapan Program
    wf = WorkerFactory()

    workers = [
        wf.create_worker('analyst'),
        wf.create_worker('developer'),
        wf.create_worker('tester')
    ]

    for worker in workers:
        print(f"{worker.name()} start {worker.work()} the Program")
        print(f'Skills: {worker.get_skills()}', end='\n\n')
