# Real Storage Capacity Checker
This Python program calculates the actual usable storage capacity of a drive (HDD, SSD, or USB) based on its advertised capacity.  

Storage manufacturers typically advertise capacities in decimal units (GB, TB), where:
- 1 GB (Gigabyte) = 1,000,000,000 bytes
- 1 TB (Terabyte) = 1,000,000,000,000 bytes

However, operating systems measure storage in binary units (GiB, TiB), where:
- 1 GiB (Gibibyte) = 1,073,741,824 bytes
- 1 TiB (Tebibyte) = 1,099,511,627,776 bytes

This discrepancy means that a 1 TB drive will show up as ~0.91 TiB in your OS.
