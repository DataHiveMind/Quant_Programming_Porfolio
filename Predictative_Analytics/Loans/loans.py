class Mortgage(object):
    def __init__(self, loan, annRate, months):
        # Create a Mortage, initialised by vlaue returned by function findPayment
        self.loan = loan
        self.rate = annRate/12.0
        self.months = months
        self.paid = [0.0]
        self.owed = [loan]
        self.payment = findPayments(loan,self.rate, months)
        self.legend = None # Description of Mortage
    
    def makePayment(self):
        # Make a Payment
        self.paid.append(self.payment)
        reduction = self.payment - self.owed[-1]*self.rate
        self.owed.append(self.owed[-1] - reduction)
    
    def getTotalPaid(self):
        # Return the total amount paid so far
        return sum(self.paid)
    
    def __str__(self):
        return self.legend

# Classes for Calculating Type 1 and Type 2
class Fixed(Mortgage):   # Inherting mortage class
    def __init__(self,loan,r,months):
        Mortgage.__init__(self, loan, r, months)
        self.legend = "Fixed, " + str(r*100) + "%"
    
class FixedWithPts(Mortgage):
    def __init__(self,loan,r,months,pts):
        Mortgage.__init__(self, loan, r, months)
        self.pts = pts
        self.paid = [loan*(pts/100.0)]
        self.legend = "Fixed, " + str(r*100) + "%, "+ str(pts) + ' points'

def compareMortgages(amt, years, fixedRate, pts, ptsRate):
    totmonths = years*12
    fixed1 = Fixed(amt, fixedRate, totmonths)
    fixed2 = FixedWithPts(amt, ptsRate, totmonths, pts)
    
    morts = [fixed1, fixed2]
    for i in range(totmonths):
        for mort in morts:
            mort.makePayment()
    
    for i in morts:
        print(i)
        print("Total Payment = $" + str(int(i.getTotalPaid())))
        
def findPayments(loan, r: float, m: int):
    pass
    # Returns the monthly payment for a Mortage of size(loan) at Monthly rate(r) for Months(M)
    return loan*((r*(1+r)**m)/((1+r)**m -1))

if __name__ == "__main__":
    compareMortgages(amt = 10000, years = 30, fixedRate = 0.07, pts = 5, ptsRate = 0.07)
    