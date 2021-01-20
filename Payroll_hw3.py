# File: Payroll.py
# Student: Ahmet Nalcaci
# UT EID: an27394
# Course Name: CS303E
# Unique Number: 50695
#
# Date Created: 9/10/2020
# Date Last Modified: 9/17/2020
# Description of Program: Calculate any indivudials payroll by inputing few values 


employees_name = input("Enter employee’s name: ")
hr_worked = float (input("Enter number of hours worked in a week: "))
pay_rate = float (input("Enter hourly pay rate: "))                                              #inputs of the client
ftax_rate = float (input("Enter federal tax withholding rate: "))
stax_rate = float (input("Enter state tax withholding rate: "))


gross_pay = float(hr_worked*pay_rate)                                                         #Calculation for gross pay (hrs * pay rate)
ftax_ = float(ftax_rate) * 100                                                                #Covert the state and federal tax to percentage
stax_ = float(stax_rate) * 100
ftotal = float(gross_pay) * float(ftax_rate)                                                   #Calculation for federal and state tax
stotal = float(gross_pay)*float(stax_rate)
TotalDeduction = float(stotal)+float(ftotal)                                                   #Total deduction by adding federal and state tax
TotalPay = float(gross_pay)-float(TotalDeduction)                                              #Net pay (gross pay - total deduction)



print()
print("Employee Name:", employees_name)
print("Hours Worked:", hr_worked)                                                           
print("Pay Rate:", "$" + format(pay_rate,".2f"))


print("Gross pay:",  "$" + format(gross_pay,".2f"))                                           
             
print("Deductions: ")                                                                                                                                                                        #Federal tax calculation 
print("  Federal Withholding (" + format(ftax_,".1f") + "%): $" + format(ftotal,".2f"))
print("  State Withholding (" + format(stax_,".1f") + "%): $" + format(stotal,".2f"))                          
print("  Total Deduction: $" + format(TotalDeduction,".2f"))                                      
print("Net Pay: $" + format(TotalPay,".2f"))                                                      

