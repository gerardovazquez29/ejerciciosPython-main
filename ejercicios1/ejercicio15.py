
humidity_percent = [40,35,20,70]

ideal = [level for level in humidity_percent if level >= 30 and level <= 50]

print(ideal)

"""
[40, 35]
"""