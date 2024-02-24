# Example 2.2
# Service Charge Calculation
room_rent = int(input(" Type Hotel Room Rent: "))
if room_rent >= 5000:
  service_charge = 0.12 * room_rent
  print(f"Service Charge = Rs. {service_charge}")
else:
  service_charge = 0.06 * room_rent
  print(f"Service Charge = Rs. {service_charge:8.2f}")