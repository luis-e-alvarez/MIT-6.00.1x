class Solution:
    def balanceCalculator(self, balance, annualInterestRate, monthlyPaymentRate):
        """
        balance: float representing unpaid balance 
        annualInterestRate: float representing annual interest rate. Decimal
        monthlyPaymentRate: min monthly payment rate as a decimal
        """
        monthlyInterestRate = round(annualInterestRate/12, 2)
        minMonthlyPayment = monthlyPaymentRate * balance
        for x in range(12):
            balance = balance - minMonthlyPayment
            balance = balance + (monthlyInterestRate * balance)
        print('Remaining balance: ' + round(balance, 2))
    def minMonthlyCalc(self, balance, annualInterestRate):
        """
        balance: float representing unpaid balance
        annualInterestRate: float representing annual interest rate. Decimal
        """
        reducedBalance = balance
        monthlyInterestRate = annualInterestRate/12
        minMonthlyPayment = 10
        while(reducedBalance >= 0):
          for x in range(12):
             reducedBalance = reducedBalance - minMonthlyPayment
             reducedBalance = reducedBalance + (monthlyInterestRate *reducedBalance)
          if(reducedBalance > 0):
              minMonthlyPayment = minMonthlyPayment + 10
              reducedBalance = balance
        print(minMonthlyPayment)
    def bisectionSearch(self, balance, annualInterestRate):
        import math
        epsilon = 0.01
        monthlyInterestRate = annualInterestRate/12.0
        reducedBalance = balance
        lowerBound = balance/12
        upperBound = balance * math.pow((1 + monthlyInterestRate),12)/12.0
        while(abs(reducedBalance) > epsilon):
          minMonthlyPayment = (lowerBound + upperBound) / 2.0
          reducedBalance = balance
          for x in range(12):
             reducedBalance = reducedBalance - minMonthlyPayment
             reducedBalance = reducedBalance + (monthlyInterestRate * reducedBalance)
          if(reducedBalance > 0):
              lowerBound = minMonthlyPayment
          else:
              upperBound = minMonthlyPayment
        print(round(minMonthlyPayment,2))
        


solution = Solution()
solution.bisectionSearch(320000, 0.2)

