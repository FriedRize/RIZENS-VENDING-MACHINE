class VendingMachine:
    def __init__(self):
        self.items = {
            "A01": {"name": "Water", "price": 1, "stock": 10},
            "B01": {"name": "Chocolates", "price": 5, "stock": 5},
            "C01": {"name": "Soft Drinks", "price": 3, "stock": 8},
            "D01": {"name": "Chips", "price": 3, "stock": 6},
            "E01": {"name": "Energy Drinks", "price": 5, "stock": 4},
            "F01": {"name": "Juice Box", "price": 2, "stock": 7},
        }

    def display_menu(self):
        print("\nWelcome to RIZEN'S VENDING MACHINE! Here are the available items from RIZEN'S VENDING MACHINE:")
        for code, item in self.items.items():
            print(f"{code}: {item['name']} - {item['price']} AED ({item['stock']} in stock)")

    def input_item_code(self):
        while True:
            code = input("\nEnter the item code (e.g., A01): ").upper()
            if code in self.items:
                if self.items[code]['stock'] > 0:
                    return code
                else:
                    print("Sorry, this item is out of stock. Please choose another.")
            else:
                print("Invalid code. Please try again.")

    def process_order(self):
        total_cost = 0
        selected_items = []

        while True:
            code = self.input_item_code()
            item = self.items[code]

            print(f"You selected {item['name']} for {item['price']} AED.")
            confirm = input("Do you want to cancel this item? (yes/no): ").strip().lower()
            if confirm == "yes":
                print("Item canceled. Returning to menu.")
                continue

            total_cost += item['price']
            selected_items.append(code)
            self.items[code]['stock'] -= 1

            another = input("Do you want to add another item? (yes/no): ").strip().lower()
            if another != "yes":
                break

        return total_cost, selected_items

    def handle_payment(self, total_cost):
        while True:
            print(f"\nThe total cost is {total_cost} AED.")
            payment = int(input("Enter your payment amount (in AED): "))

            if payment == total_cost:
                print("Payment received. Dispensing items...")
                return
            elif payment > total_cost:
                change = payment - total_cost
                print(f"Payment received. Your change is {change} AED. Dispensing items...")
                return
            else:
                print(f"Insufficient payment. You need {total_cost - payment} AED more.")
                retry = input("Do you want to cancel the transaction? (yes/no): ").strip().lower()
                if retry == "yes":
                    print("Transaction canceled. Returning credits...")
                    return False

    def start(self):
        while True:
            self.display_menu()
            total_cost, selected_items = self.process_order()

            cancel = input("Do you want to cancel the entire order? (yes/no): ").strip().lower()
            if cancel == "yes":
                print("Order canceled. Returning to start.")
                for code in selected_items:
                    self.items[code]['stock'] += 1  # Restock canceled items
                continue

            if self.handle_payment(total_cost):
                print("\nThank you for your purchase! Please collect your items.")
                for code in selected_items:
                    print(f"Dispensing {self.items[code]['name']}...")
                print("\nTransaction complete. Have a great day!")
                break

vending_machine = VendingMachine()
vending_machine.start()
