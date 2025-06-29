# Precomputed conversion factors (advertised / real)
TB_TO_TIB = 1000000000000 / 1099511627776  # 1 TB ≈ 0.9095 TiB
GB_TO_GIB = 1000000000 / 1073741824        # 1 GB ≈ 0.9313 GiB

def calculate_real_capacity():
    print("\nStorage Capacity Calculator")
    print("---------------------------")

    while True:
        # Get unit input (case-insensitive)
        unit = input("Enter TB or GB for the advertised unit (or 'q' to quit): ").strip().upper()
        if unit == 'Q':
            break
        if unit not in ('TB', 'GB'):
            print("Error: Please enter 'TB' or 'GB'.")
            continue

         # Get advertised capacity (with error handling)
        try:
            advertised = float(input("Enter the advertised capacity: "))
        except ValueError:
            print("Error: Please enter a valid number.")
            continue

        # Calculate real capacity
        real_capacity = advertised * (TB_TO_TIB if unit == 'TB' else GB_TO_GIB)
        print(f"The actual capacity is {real_capacity:.2f} {unit}\n")

if __name__ == "__main__":
    calculate_real_capacity()
