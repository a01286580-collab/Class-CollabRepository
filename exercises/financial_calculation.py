
#First Present Value calculation
PV_1 = 1000
IR_1 = 0.05
Per_1 = 10

FV_1 = (
    PV_1
    * (1 + IR_1) ** Per_1
)
#Second Present Value Calculation
PV_2 = 1300
IR_2 = 0.11
Per_2 = 10

FV_2 = (
    PV_2
    * (1 + IR_2) ** Per_2
)

print("Scenario 1:", round(FV_1, 2))
print("Scenario 2:", round(FV_2, 2))

# Formula: FV = PV * (1 + r)
# Computes the Future Value (FV) using compound interest, where PV is the initial investment,
# r is the periodic interest rate, and n is the total number of compounding periods.

# Comparison:
# Scenario 2 yields 3,691.25 compared to 1,628.89 in Scenario 1.
# The combination of a higher initial principal (1,300 vs 1,000) and more than double
# the interest rate (11% vs 5%) produces a 126.6% higher return over 10 periods.