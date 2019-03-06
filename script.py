class Menu:
  def __init__(self, name, items, start_item, end_item):
    self.name = name
    self.items = items
    self.start_item = start_item
    self.end_item = end_item
    
  def __repr__(self):
    return self.name + ' menu available from ' + str(self.start_item) + ' to ' + str(self.end_item)
  
  def calculate_bill(self, purchased_items):
    total_bill = 0
    for item in purchased_items:
      if item in self.items:
        total_bill += self.items[item]
    return total_bill

class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus
    
  def available_menus(self, time):
    available_menus = []
    for menu in self.menus:
      if time >= menu.start_item and time <= menu.end_item:
        available_menus.append(menu)
    return available_menus
    
    
  def __repr__(self):
    return "Franchise is located at " + self.address
    
#Bruch Menu
brunch_items = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}
brunch_menu = Menu('Brunch', brunch_items, 1100, 1600)

#Early Bird Menu
early_bird_items = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}

early_bird_menu = Menu('Early Bird', early_bird_items, 1500, 1800)

#dinner Menu
dinner_items = {
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}

dinner_menu  = Menu('Dinner', dinner_items, 1700, 2300)
#Kids Menu
kids_items = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}

kids_menu  = Menu('Kids', kids_items, 1100, 2100)

print(brunch_menu)
print(brunch_menu.calculate_bill(['pancakes', 'home fries', 'coffee']))

print(early_bird_menu.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))


menus = [brunch_menu, early_bird_menu, dinner_menu, kids_menu]
flagship_store = Franchise('1232 West End Road', menus)
new_installment = Franchise('12 East Mulberry Street', menus)

print(flagship_store)

print(flagship_store.available_menus(1200))

print(flagship_store.available_menus(1700))
