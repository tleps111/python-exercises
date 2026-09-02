talent = int(input("Enter talents: "))
pound = int(input("Enter pounds: "))
lot = float(input("Enter lots: "))

talent_grams = talent * 20 * 32 * 13.3
pound_grams = pound * 32 * 13.3
lot_grams = lot * 13.3
total_grams = talent_grams + pound_grams + lot_grams

kilograms = int(total_grams // 1000)
grams = total_grams % 1000

print(f"The weight in modern units {kilograms} kilograms and {grams:.2f} grams")
 








