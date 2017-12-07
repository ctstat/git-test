# Chain Class Example
class Retail_1:
    """ Retail Class for Revenue Calculation """
    def __init__(self, brand):
         """ Information of each retail e.g., income and cost """
         self.brand = brand
         self.income = []
         self.cost = []
         print("This is the revenue report of", self.brand)

    def AddIncome(self, income):
        """ Record all incomes """
        self.income.append(income)
    
    def AddCost(self, cost):
        """ Record all costs """
        self.cost.append(cost)
    
    def Revenue(self):
        """ Calculate the average revenue"""
        meanincome = sum(self.income) / len(self.income)
        meancost = sum(self.cost) / len(self.cost)
        aveRevenue = meanincome - meancost
        return ("{0} average revenue is ${1} billions".format(self.brand, aveRevenue))


# Walmart
c1 = Retail_1("Walmart")

# income of each walmart store
walmart_income = [100, 120, 90, 115, 85]
walmart_cost = [55, 45, 30, 60, 57]

for i,j in zip(walmart_income, walmart_cost):
    c1.AddIncome(i)
    c1.AddCost(j)

print(c1.Revenue())




