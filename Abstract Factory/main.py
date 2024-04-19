
"""
Contoh penggunaan Creational Pattern (Abstract Factory)

Abstract Factory Pattern digunakan untuk membuat kumpulan objek yang saling terkait tanpa harus menentukan
kelas konkret yang akan dihasilkan.

Dalam contoh ini, saya menggunakan Abstract Factory Pattern untuk membuat tim pekerja (IT Team) yang terdiri
dari Developer, Tester, dan Analyst. Setiap anggota tim memiliki nama yang dapat diinisialisasi saat pembuatan
objek.

Dalam Abstract Factory Pattern:
> Abstract Factory (TeamFactory):
  - Merupakan kelas abstrak yang mendefinisikan metode-metode untuk membuat kumpulan objek terkait.
  - Setiap metode abstrak dalam Abstract Factory menghasilkan instance dari objek-objek yang saling terkait
    dan berbeda-beda.
> Concrete Factory (ITTeamFactory):
  - Merupakan implementasi konkret dari Abstract Factory.
  - Setiap Concrete Factory mengimplementasikan metode-metode dari Abstract Factory untuk membuat instance
    konkret dari objek-objek yang terkait.

"""

from abc import ABC, abstractmethod
from typing import List


class Worker(ABC):
    # Interface Worker memiliki tiga method yaitu name(), work() dan get_skills().
    def __init__(self, name: str):
        self._name = name

    def name(self) -> str:
        return self._name

    @abstractmethod
    def work(self) -> str:
        pass

    @abstractmethod
    def get_skills(self) -> List[str]:
        pass


class TeamFactory(ABC):
    # TeamFactory adalah abstract factory untuk menciptakan tim worker terkait.
    @abstractmethod
    def create_developer(self, name: str) -> Worker:
        pass

    @abstractmethod
    def create_tester(self, name: str) -> Worker:
        pass

    @abstractmethod
    def create_analyst(self, name: str) -> Worker:
        pass


class Developer(Worker):
    # Developer adalah salah satu class yang mengimplementasikan interface Worker.
    def __init__(self, name: str):
        super().__init__(name)

    def work(self) -> str:
        return 'Developing'

    def get_skills(self) -> List[str]:
        return ['Python', 'JavaScript', 'PHP']


class Tester(Worker):
    # Tester adalah salah satu class yang mengimplementasikan interface Worker.
    def __init__(self, name: str):
        super().__init__(name)

    def work(self) -> str:
        return 'Testing'

    def get_skills(self) -> List[str]:
        return ['Selenium', 'Junit', 'Jmeter', 'TestNG']


class Analyst(Worker):
    # Analyst adalah salah satu class yang mengimplementasikan interface Worker.
    def __init__(self, name: str):
        super().__init__(name)

    def work(self) -> str:
        return 'Analyzing'

    def get_skills(self) -> List[str]:
        return ['Data Analysis', 'Requirement Analysis', 'UML']


class ITTeamFactory(TeamFactory):
    # ITTeamFactory adalah concrete factory untuk menciptakan tim worker terkait
    # (analyst, developer, atau tester).
    def create_analyst(self, name: str) -> Worker:
        return Analyst(name)

    def create_developer(self, name: str) -> Worker:
        return Developer(name)

    def create_tester(self, name: str) -> Worker:
        return Tester(name)


if __name__ == '__main__':
    # Contoh Penerapan Program dengan Abstract Factory Pattern
    it_team_factory = ITTeamFactory()

    # Membuat tim IT dengan nama anggota
    analyst = it_team_factory.create_analyst('Zain')
    developer = it_team_factory.create_developer('Zainul')
    tester = it_team_factory.create_tester('Muhaimin')

    # Menampilkan informasi tim IT
    print(f"{analyst.name()} starts {analyst.work()} the Application requirements")
    print(f'Skills: {analyst.get_skills()}')

    print(f"\n{developer.name()} starts {developer.work()} the Application")
    print(f'Skills: {developer.get_skills()}')

    print(f"\n{tester.name()} starts {tester.work()} the Application")
    print(f'Skills: {tester.get_skills()}')
