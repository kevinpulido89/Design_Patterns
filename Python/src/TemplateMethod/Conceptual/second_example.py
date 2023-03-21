"""
This module contains the Template class.
https://www.youtube.com/watch?v=BBlaDMqV8ks - Fix The Call Super 
Anti-Pattern With The Template Method Pattern In Python

Template Method is a behavioral design pattern that defines the 
skeleton of an algorithm in the base class but lets subclasses 
override specific steps of the algorithm without changing 
its structure.
"""
from abc import abstractmethod, ABC

class Report(ABC):
    """ Abstract class Report """

    @abstractmethod
    def make_report_body(self):
        """	This method is an abstract method. """
        pass

    def make_report(self):
        """	This method is a concrete method. """
        print("Report header")
        print(f"Company name: {self.company_name}")
        print("*********************************")
        self.make_report_body()
        print()

class SalesReport(Report):
    """
    This class is a child of the Report class.
    """

    def __init__(self, company_name, net_sales):
        self.company_name = company_name
        self.net_sales = net_sales

    def make_report_body(self):
        """
        This method is an implementation of the abstract method make_report_body()
        from the parent class Report
        """
        print(f"Sales: {self.net_sales}")

class FinanceReport(Report):
    """
    This class is a child of the Report class.
    """

    def __init__(self, company_name, finance):
        self.company_name = company_name
        self.finance = finance

    def make_report_body(self):
        print(f"Costs: {self.finance}")

cost = FinanceReport("Google", 1000)
cost.make_report()

sales = SalesReport("Facebook", 2000)
sales.make_report()
