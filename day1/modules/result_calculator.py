mark1 = float(input("Enter first mark: "))
mark2 = float(input("Enter second mark: "))
mark3 = float(input("Enter third mark: "))
def calculate_percentage(mark1, mark2, mark3):
 total = mark1 + mark2 + mark3
 percentage = total / 3
 return percentage
percentage = calculate_percentage(mark1, mark2, mark3)
print("This is the percentage:", percentage)