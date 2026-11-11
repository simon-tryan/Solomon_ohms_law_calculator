# Ohm's Law and Power Calculator
# Author: Solomon Philip ibukunoluwa 
# ND1 Mechatronics Engineering, YabaTech

def get_valid_number(prompt):
    """Keep asking until the user enters a valid positive number"""
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a positive number greater than zero.")
            else:
                return value
        except ValueError:
            print("Invalid input! Please enter a number.")

def calculate():
    """Main calculation function"""
    print("\nWhat do you want to calculate?")
    print("1. Voltage (V)")
    print("2. Current (I)")
    print("3. Resistance (R)")
    print("4. Power (P)")
    print("5. Quit")

    choice = input("Enter your choice (1-5): ").strip()

    if choice == "5":
        return None   # Signal to quit

    if choice == "1":  # Voltage = Current × Resistance
        current = get_valid_number("Enter Current (A): ")
        resistance = get_valid_number("Enter Resistance (Ω): ")
        voltage = current * resistance
        result = f"Voltage = {voltage:.2f} V"
        formula = f"V = I × R → {current} × {resistance}"

    elif choice == "2":  # Current = Voltage / Resistance
        voltage = get_valid_number("Enter Voltage (V): ")
        resistance = get_valid_number("Enter Resistance (Ω): ")
        current = voltage / resistance
        result = f"Current = {current:.2f} A"
        formula = f"I = V / R → {voltage} / {resistance}"

    elif choice == "3":  # Resistance = Voltage / Current
        voltage = get_valid_number("Enter Voltage (V): ")
        current = get_valid_number("Enter Current (A): ")
        resistance = voltage / current
        result = f"Resistance = {resistance:.2f} Ω"
        formula = f"R = V / I → {voltage} / {current}"

    elif choice == "4":  # Power = Voltage × Current
        voltage = get_valid_number("Enter Voltage (V): ")
        current = get_valid_number("Enter Current (A): ")
        power = voltage * current
        result = f"Power = {power:.2f} W"
        formula = f"P = V × I → {voltage} × {current}"

    else:
        print("Invalid choice. Please select 1-5.")
        return "invalid"

    print("\n" + "="*50)
    print(result)
    print(f"Formula used: {formula}")
    print("="*50)

    return result

def main():
    """Main program loop"""
    print("="*50)
    print("   OHM'S LAW & POWER CALCULATOR")
    print("="*50)

    history = []   # Own twist: stores all successful calculations

    while True:
        result = calculate()

        if result is None:          # User chose Quit
            break
        elif result != "invalid":
            history.append(result)

    # Show session summary (the twist)
    print("\n" + "="*50)
    print("           SESSION SUMMARY")
    print("="*50)

    if history:
        print(f"You performed {len(history)} calculation(s):\n")
        for i, calc in enumerate(history, 1):
            print(f"{i}. {calc}")
    else:
        print("No calculations were performed.")

    print("\nThank you for using the calculator!")
    print("="*50)

if __name__ == "__main__":
    main()