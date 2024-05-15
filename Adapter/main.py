"""
Contoh penggunaan Structural Pattern (Adapter)

Adapter Pattern adalah sebuah pattern yang digunakan untuk mengubah interface 
dari sebuah class ke interface lain yang diharapkan oleh client.
Pattern ini biasanya digunakan ketika kita ingin menggunakan sebuah class yang tidak sesuai dengan kebutuhan kita,
sehingga kita perlu membuat sebuah class baru yang mengubah interface class tersebut ke interface yang kita inginkan.

Contoh kasus:
Misalkan kita memiliki sebuah class Car yang memiliki method drive() dan klakson().
dan juga memiliki class Bus yang memiliki method drive() dan telolet().
Kita ingin membuat instance Car yang memiliki semua method yang dimiliki car dan method telolet().
Kita bisa membuat class TeloletAdapter yang mengubah interface kendaran sebelumnya (dalam hal ini Car) ke interface yang kita inginkan.

"""


class Car:
    # Car adalah salah satu class yang memiliki method drive() dan klakson().
    def __init__(self):
        self.name = "Car"
        print("Car is ready!")

    def drive(self) -> None:
        print(f"Driving a Car...")

    def klakson(self) -> None:
        print("Honk: Tin tin")


class Bus:
    # Bus adalah salah satu class yang memiliki method drive() dan telolet().
    def __init__(self):
        self.name = "Bus"
        print("Bus is ready!")

    def drive(self) -> None:
        print(f"Driving a Bus...")

    def telolet(self) -> None:
        print("Honk: Telolet Telolet")


class TeloletAdapter:
    # TeloletAdapter adalah class yang mengubah interface Kendaraan lain menjadi interface yang memiliki method telolet().
    def __init__(self, vehicle, **adapted_methods) -> None:
        # class ini mewarisi semua property dari class kendaraan sebelumnya
        self.vehicle = vehicle
        self.__dict__.update(adapted_methods)
        print(f"Your {self.name} has been adapted to have Telolet feature!")

    def __getattr__(self, attr):
        # method ini digunakan untuk mewarisi semua method dari class kendaraan sebelumnya
        return getattr(self.vehicle, attr)

    def drive(self) -> None:
        # method ini akan melakukan override terhadap method drive() dari class kendaraan sebelumnya
        print(f"Driving a modified {self.name}...")

    def telolet(self) -> None:
        print("Honk 2nd Variation: Telolet Telolet Telolet")


if __name__ == '__main__':
    bus = Bus()
    car = Car()
    car_modified = TeloletAdapter(car)

    print("\n=Bus=")
    bus.drive()
    bus.telolet()

    print("\n=Car=")
    car.drive()
    car.klakson()
    try:
        # Akan error karena Car tidak memiliki method telolet()
        car.telolet()
    except Exception as e:
        print("Error:", e)

    print("\n=Modified Car (with Telolet Adapter)=")
    car_modified.drive()
    car_modified.klakson()
    try:
        # Tidak akan error karena Car sudah diadaptasi menjadi Car yang memiliki method telolet()
        car_modified.telolet()
    except Exception as e:
        print("Error:", e)
