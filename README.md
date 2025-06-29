# Real Storage Capacity Checker
This Python program calculates the actual usable storage capacity of a drive (HDD, SSD, or USB) based on its advertised capacity.  

Storage manufacturers typically advertise capacities in decimal units (GB, TB), where:
- 1 GB (Gigabyte) = 1,000,000,000 bytes
- 1 TB (Terabyte) = 1,000,000,000,000 bytes

However, operating systems measure storage in binary units (GiB, TiB), where:
- 1 GiB (Gibibyte) = 1,073,741,824 bytes
- 1 TiB (Tebibyte) = 1,099,511,627,776 bytes

This discrepancy means that a 1 TB drive will show up as ~0.91 TiB in your OS.

### What the Program Does:
1. Asks the user for the advertised storage unit (TB or GB).
2. Takes the advertised capacity (e.g., "1" for a 1TB drive).
3. Calculates and displays the real usable capacity in the same unit, accounting for the difference between decimal and binary measurement.

### Example Output:
- Input: TB, 1 → Output: "The actual capacity is 0.91 TB"
- Input: GB, 500 → Output: "The actual capacity is 465.66 GB"

This helps users understand why their drive appears smaller than advertised in their operating system.
