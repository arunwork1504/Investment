import matplotlib.pyplot as plt

# Fund categories and their approximate risk levels (1 = lowest, 5 = highest)
fund_categories = [
    ("Overnight Fund", 1),
    ("Liquid Fund", 1),
    ("Ultra Short Duration Fund", 1.5),
    ("Low Duration Fund", 1.5),
    ("Money Market Fund", 1.5),
    ("Short Duration Fund", 2),
    ("Medium Duration Fund", 2.5),
    ("Medium to Long Duration Fund", 3),
    ("Long Duration Fund", 3.5),
    ("Gilt Fund", 3),
    ("Corporate Bond Fund", 2.5),
    ("Banking & PSU Fund", 2.5),
    ("Credit Risk Fund", 4),
    ("Dynamic Bond Fund", 3),
    ("Conservative Hybrid Fund", 2),
    ("Balanced Hybrid Fund", 3),
    ("Aggressive Hybrid Fund", 4),
    ("Balanced Advantage Fund", 3),
    ("Multi Asset Allocation Fund", 3),
    ("Arbitrage Fund", 2),
    ("Equity Savings Fund", 3),
    ("Large Cap Fund", 3.5),
    ("Large & Mid Cap Fund", 4),
    ("Mid Cap Fund", 4.5),
    ("Small Cap Fund", 5),
    ("Multi Cap Fund", 4.5),
    ("Flexi Cap Fund", 4),
    ("Focused Fund", 4.5),
    ("Sectoral/Thematic Fund", 5),
    ("ELSS", 4),
    ("Index Fund", 3.5),
    ("ETF", 3.5),
    ("Retirement Fund", 3.5),
    ("Children's Fund", 3.5),
    ("Fund of Funds", 3)
]

# Separate names and risk levels
names = [x[0] for x in fund_categories]
risk_levels = [x[1] for x in fund_categories]

# Create figure
plt.figure(figsize=(10, 12))
plt.scatter(risk_levels, names, c=risk_levels, cmap='coolwarm', s=100, edgecolors='black')

# Labels & Title
plt.xlabel("Risk Level (1 = Lowest, 5 = Highest)", fontsize=12)
plt.ylabel("Fund Category", fontsize=12)
plt.title("Mutual Fund Categories in India - Risk Map", fontsize=14, fontweight='bold')
plt.colorbar(label="Risk Level")

# Invert y-axis to have safest at top
plt.gca().invert_yaxis()

# Show plot
plt.tight_layout()
plt.show()
