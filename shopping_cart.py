class ShoppingCart:
    # write your code here
    def __init__(self, emp_discount=None):
        self.total = 0
        self.employee_discount = emp_discount
        self.items = []
        
    def add_item(self, name, price, quantity=1):
        if quantity > 1:
            for i in range(0,quantity):
                self.items.append({'name': name, 'price': price})
        else:
            self.items.append({'name': name, 'price': price})
        self.total += price*quantity
        return self.total
    
    def mean_item_price(self):
        avg_price = self.total/len(self.items)
        return avg_price

    def median_item_price(self):
        prices_list = []
        for item in self.items:
            prices_list.append(item['price'])
        sorted_list = sorted(prices_list)
        if len(sorted_list) % 2 != 0:
            med_price = sorted_list[len(sorted_list)//2]
        else:
            med_price = (sorted_list[len(sorted_list)/2] + sorted_list[len(sorted_list)/2 - 1])/2
        return med_price
    
    def apply_discount(self):
        if self.employee_discount:
            return self.total*(1 - (self.employee_discount*0.01))
        else: 
            return 'Sorry, there is no discount to apply to your cart :('
    
    def void_last_item(self):
        if self.items:
            removed_item = self.items.pop()
            self.total -= removed_item['price']
        else:
            return "There are no items in your cart!"
            