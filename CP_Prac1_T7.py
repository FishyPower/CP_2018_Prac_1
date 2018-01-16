#Computing Practical 1 - Task 7

name = input("Enter name: ")
hours = float(input("Enter number of hours worked weekly: "))
hourly_pay = float(input("Enter hourly pay rate: "))
cpf_rate = float(input("Enter CPF contribution rate(%): "))

gross_pay = hours * hourly_pay * cpf_rate
cpf = gross_pay / 100

net_pay = gross_pay - cpf

print("Payroll statement for {0}".format(name))
print("Number of hours worked in week: {0}".format(hours))
print("Hourly pay rate: $ {0}".format(hourly_pay))
print("Gross pay = $ {0}".format(gross_pay))

print()

print("Net pay = $ {0}".format(net_pay))