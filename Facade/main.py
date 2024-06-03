"""
Contoh penggunaan Structural Pattern (Facade)

Facade Pattern digunakan untuk menyediakan antarmuka tunggal yang menyederhanakan 
interaksi dengan serangkaian antarmuka dalam subsistem. 
Ini berguna untuk menyembunyikan kompleksitas subsistem dan memberikan titik akses
yang lebih mudah bagi pengguna.

Untuk contoh kasus kali ini, saya menggunakan Facade Pattern untuk mengelola operasi 
basis data dalam konteks e-commerce. Saya memiliki beberapa layanan (Service) 
yang masing-masing bertanggung jawab untuk mengelola data terkait
pesanan, pembayaran, dan inventaris yang mana semuanya diintegrasikan oleh
ECommerceFacade.
"""

import json
from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional

class IOrderService(ABC):
    # Interface IOrderService memiliki dua method abstract yaitu create_order()
    # dan cancel_order().
    @abstractmethod
    def create_order(self, customer_id: int, product_ids: List[int], total_amount: float) -> Dict[str, Any]:
        pass

    @abstractmethod
    def cancel_order(self, order_id: int) -> Optional[Dict[str, Any]]:
        pass

class IPaymentService(ABC):
    # Interface IPaymentService memiliki satu method abstract yaitu process_payment().
    @abstractmethod
    def process_payment(self, order_id: int, amount: float) -> Dict[str, Any]:
        pass

class IInventoryService(ABC):
    # Interface IInventoryService memiliki dua method abstract yaitu update_inventory()
    # dan calculate_total_amount().
    @abstractmethod
    def update_inventory(self, product_ids: List[int]) -> None:
        pass

    @abstractmethod
    def calculate_total_amount(self, product_ids: List[int]) -> float:
        pass

class OrderService(IOrderService):
    # OrderService adalah salah satu class yang mengimplementasikan suatu operasi beli.
    def __init__(self, orders_file: str = 'orders.json'):
        self.orders_file = orders_file

    def _read_orders(self) -> List[Dict[str, Any]]:
        with open(self.orders_file, 'r') as file:
            return json.load(file)

    def _write_orders(self, orders: List[Dict[str, Any]]) -> None:
        with open(self.orders_file, 'w') as file:
            json.dump(orders, file, indent=4)

    def create_order(self, customer_id: int, product_ids: List[int], total_amount: float) -> Dict[str, Any]:
        orders = self._read_orders()
        new_order = {
            "order_id": len(orders) + 1,
            "customer_id": customer_id,
            "product_ids": product_ids,
            "total_amount": total_amount,
            "status": "created"
        }
        orders.append(new_order)
        self._write_orders(orders)
        return new_order

    def cancel_order(self, order_id: int) -> Optional[Dict[str, Any]]:
        orders = self._read_orders()
        for order in orders:
            if order['order_id'] == order_id:
                order['status'] = 'canceled'
                self._write_orders(orders)
                return order
        return None

class PaymentService(IPaymentService):
    # PaymentService adalah salah satu class yang mengimplementasikan suatu operasi pembayaran.
    def __init__(self, payments_file: str = 'payments.json'):
        self.payments_file = payments_file

    def _read_payments(self) -> List[Dict[str, Any]]:
        with open(self.payments_file, 'r') as file:
            return json.load(file)

    def _write_payments(self, payments: List[Dict[str, Any]]) -> None:
        with open(self.payments_file, 'w') as file:
            json.dump(payments, file, indent=4)

    def process_payment(self, order_id: int, amount: float) -> Dict[str, Any]:
        payments = self._read_payments()
        new_payment = {
            "payment_id": len(payments) + 1,
            "order_id": order_id,
            "amount": amount,
            "status": "processed"
        }
        payments.append(new_payment)
        self._write_payments(payments)
        return new_payment

class InventoryService(IInventoryService):
    # InventoryService adalah salah satu class yang mengimplementasikan suatu operasi inventaris.
    def __init__(self, inventory_file: str = 'inventory.json'):
        self.inventory_file = inventory_file

    def _read_inventory(self) -> List[Dict[str, Any]]:
        with open(self.inventory_file, 'r') as file:
            return json.load(file)

    def _write_inventory(self, inventory: List[Dict[str, Any]]) -> None:
        with open(self.inventory_file, 'w') as file:
            json.dump(inventory, file, indent=4)

    def update_inventory(self, product_ids: List[int]) -> None:
        inventory = self._read_inventory()
        for product_id in product_ids:
            for item in inventory:
                if item['product_id'] == product_id:
                    item['quantity'] -= 1
        self._write_inventory(inventory)

    def calculate_total_amount(self, product_ids: List[int]) -> float:
        inventory = self._read_inventory()
        total_amount = 0.0
        for product_id in product_ids:
            for item in inventory:
                if item['product_id'] == product_id:
                    total_amount += item['price']
        return total_amount

class ECommerceFacade:
    # ECommerceFacade adalah class yang bertanggung jawab untuk mengintegrasikan setiap service yang ada.
    def __init__(self, 
                 order_service: Optional[IOrderService] = None,
                 payment_service: Optional[IPaymentService] = None,
                 inventory_service: Optional[IInventoryService] = None):
        self.order_service = order_service or OrderService()
        self.payment_service = payment_service or PaymentService()
        self.inventory_service = inventory_service or InventoryService()

    def place_order(self, customer_id: int, product_ids: List[int]) -> Dict[str, Any]:
        # Operasi untuk melakukan order.
        total_amount = self.inventory_service.calculate_total_amount(product_ids)
        order = self.order_service.create_order(customer_id, product_ids, total_amount)
        payment = self.payment_service.process_payment(order['order_id'], total_amount)
        self.inventory_service.update_inventory(product_ids)
        return {
            "order": order,
            "payment": payment
        }

    def cancel_order(self, order_id: int) -> Optional[Dict[str, Any]]:
        # Operasi untuk membatalkan order.
        order = self.order_service.cancel_order(order_id)
        return order

if __name__ == '__main__':
    # Contoh Penerapan Program
    ecommerce = ECommerceFacade()

    customer_id = 101
    product_ids = [1, 2]

    # Melakukan order
    order_result = ecommerce.place_order(customer_id, product_ids)
    print("\nOrder Result:", order_result)

    # Membatalkan order
    cancel_result = ecommerce.cancel_order(order_result['order']['order_id'])
    print("\nCancel Result:", cancel_result)
