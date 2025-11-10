from arrays import Array
from abstractqueue import AbstractQueue
from arrayqueue import ArrayQueue
from bag import Bag

class Drink:
    def __init__(self, name, price):
        self.name = name
        self.size = 'Medium'
        self.price = price
    
    ## Implementing menu
    def __str__(self):
        return f"{self.name} ({self.price})"
        

class OrderItem:
    def __init__(self, drink, customization):
        self.drink = drink
        self.customization = customization
    
    #accessors     
    def get_drink(self):
        return self.drink
    
    def get_customization(self):
        return self.customization
    
    def get_price(self):
        return self.drink.price

    def __str__(self):
        if self.customization:
            return f"{self.drink.name} ({self.drink.size}) - ${self.drink.price:.2f} | Custom: {self.customization}"
        else:
            return f"{self.drink.name} ({self.drink.size}) - ${self.drink.price:.2f}"
        
class CustomerOrder:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.items = []  # List of OrderItem
        
    #accessors methods
    def get_customer(self):
        return self.customer_name
    
    def get_item(self):
        return self.items
    
    def __str__(self):
        result = f"Order for {self.customer_name}: \n"
        for i, item in enumerate(self.items, 1):
            result += f" {i}. {item} \n"
        return result.strip()
    
    def get_total_price(self):
        return sum(item.get_price() for item in self.items)
    
    
    #mutators
    def add_item(self, order_item):
        self.items.append(order_item)
    

class BistroSystem:
    def __init__(self):
        self.m_menu = self.main_menus()  # Array of Main Menu
        self.d_menu = self.drink_menus()  # Array of Drink
        self.open_orders = ArrayQueue()  # Queue of CustomerOrder
        self.completed_orders = Bag()    # Bag/List of CustomerOrder
        # ... program logic methods
    
     #implementing Drink menu:
    def drink_menus(self):
        drink_menu = Array(5)
        drink_menu[0] = Drink("Bearcat Mocha", 39.9)
        drink_menu[1] = Drink("Campus Latte", 3.00)
        drink_menu[2] = Drink("Study Session Espresso", 2.75)
        drink_menu[3] = Drink("Library Chai", 3.25)
        drink_menu[4] = Drink("Finals Frappe", 4.00)
        return drink_menu
    
    # Implementing Main Menu
    def main_menus(self):
        mm_menu = Array(6)
        mm_menu[0] = "Display Menu"
        mm_menu[1] = "Take New Order"
        mm_menu[2] = "View Open Orders"
        mm_menu[3] = "Mark Next Order as Complete"
        mm_menu[4] = "View End-of-Day Report"
        mm_menu[5] = "Exit"
        return mm_menu
        
    #Display Main menu
    def display_main_menu(self):
        print("\n 📋 MAIN MENU \n")
        for i, lyst in enumerate(self.m_menu):
            print(f"{i+1}. {lyst}")
       
       
    #Display Drink menu
    def display_drink_menu(self, index):
        finished = True
        while finished:
            print("\n Select a drink :\n")
            for i, drink in enumerate(self.d_menu):
                print(f"{i+1}. {drink}")
            option = input(f"Drink #{index+1}: Enter drink number (1-5): ")
            if option == "":
                print("Invalid value. Please enter a number.")
                continue
            try:
                option = int(option)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                continue
            if option < 1 or option > len(self.d_menu):
                print("Choice out of range.")
                continue
            #self.take_new_order()
            finished = False
        return option
    
    # Take Order
    def take_new_order(self):
        name = input("Enter customer name: ")
        order = CustomerOrder(name)
        num_drink = int(input("How many drink would you want to order? "))
        for i in range(num_drink):
            drink_num= int(self.display_drink_menu(i))
            customization= input(f"Any customization for drink {self.d_menu[drink_num-1].name}? ")
            order_item = OrderItem(self.d_menu[drink_num], customization)
            order.add_item(order_item)
        print(f"\n📝 Order Summary for {name}:")
        for item in order.items:
            print(f"- {item.drink.name} (Medium) - {item.customization}")
        confirm = input("Confirm order? (yes/no): ").lower()
        if confirm == "yes":
            self.open_orders.add(order)
            print("✅ Order placed successfully!")
        else:
            print("Order cancelled.")
        
    # Veiw Open Order 
    def view_open_orders(self):
        print("\n🕒 Open Orders:")
        for idx, order in enumerate(self.open_orders, 1):
            drinks = ", ".join([f"{item.drink.name} ({item.customization})" for item in order.items])
            print(f"{idx}. {order.customer_name}: {drinks}")
                
    # Make order complete    
    def mark_order_complete(self):
        if self.open_orders.isEmpty():
            print("No open orders.")
            return
        order = self.open_orders.pop()
        self.completed_orders.add(order)
        print(f"✅ Order for {order.customer_name} marked as complete.")
    
    # End of Order Report
    def end_of_day_report(self):
        drink_counts = {}
        drink_sales = {}
        total_revenue = 0.0
        for order in self.completed_orders:
            for item in order.items:
                name = item.drink.name
                price = item.drink.price
                drink_counts[name] = drink_counts.get(name, 0) + 1
                drink_sales[name] = drink_sales.get(name, 0.0) + price
                total_revenue += price
        print("\nEnd-of-Day Report:")
        for name in drink_counts:
            print(f"{name}: Sold {drink_counts[name]}, Sales ${drink_sales[name]:.2f}")
        print(f"Total Revenue: ${total_revenue:.2f}")
    
    # RunProgram    
    def runProgram(self):
        print("\n ☕️ Welcome to Bistro Drink: Select an option to continue:\n")
        self.display_main_menu()
        while True:
            choice = input("Enter your choice: ")
            if choice == '1':
                self.display_main_menu()
            elif choice == '2':
                self.take_new_order()
            elif choice == '3':
                self.view_open_orders()
            elif choice == '4':
                self.mark_order_complete()
            elif choice == '5':
                self.end_of_day_report()
            elif choice == '6':
                print("\n Goodbye!\n")
                break
            else:
                print("\nInvalid choice.\n")
        
k = BistroSystem()
k.runProgram()