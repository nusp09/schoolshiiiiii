def tax(salary):
    if salary <= 12570:
        salary = salary * 1
    elif salary <= 50270:
        taxable = salary - 12570
        tax = taxable * 0.2
        salary = salary - tax
    elif salary <= 125140:
         taxable = salary - 50270
         tax = taxable * 0.4
         salary = salary - tax
         taxable = salary - (50270+12570)
         tax = taxable * 0.2
         salary = salary - tax
    elif salary > 125140:
        taxable = salary - 125140
        tax = taxable * 0.45
        salary = salary - tax
        taxable = salary - (50270+12570)
        tax = taxable * 0.4
        salary = salary - tax
        taxable = salary - (50270+12570+125140)
        tax = taxable * 0.2
        salary = salary - tax
    deductions = float(input("Enter any deductions: "))
    salary = salary + deductions
    return salary
salary = float(input("Enter your salary: "))

print(f"Your take home pay is £{tax(salary)}")
