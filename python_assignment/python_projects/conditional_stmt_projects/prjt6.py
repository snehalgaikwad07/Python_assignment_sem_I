#******************** Hotel Room Booking System ************************
name=input("Enter Guest Name:")
room_type=input("Enter room type(standard/Deluxe/suite):")
no_of_night=int(input("Enter Number of nights:"))
standard_room=2000
deluxe_room=3500
suite_room=6000
discount=0
if no_of_night>0:
    if no_of_night>=5 and no_of_night<10:
      discount=0.10
    elif no_of_night>=10:
      discount=0.20

if room_type.lower()=="standard":
   total_amount=standard_room*no_of_night
   discount_amount=total_amount*discount
   st_final=total_amount-discount_amount
elif room_type.lower()=="deluxe":
   total_amount=deluxe_room*no_of_night
   discount_amount=total_amount*discount
   dx_final=total_amount-discount_amount
elif room_type.lower()=="suite":
   total_amount=suite_room*no_of_night
   discount_amount=total_amount*discount
   suite_final=total_amount-discount_amount

print("***Room Details***")
print("Guest Name:",name)
print("Room Type:",room_type)
print("Number of nights:",no_of_night)
if room_type=="standard":
   print("Room charge:",standard_room)
elif room_type=="deluxe":
   print("Room charge:",deluxe_room)
elif room_type=="suite":
   print("Room charge:",suite_room)

print("Discount:",discount)

if room_type=="standard":
   print("Final booking amount:",st_final)
elif room_type=="deluxe":
   print("Final booking amount:",dx_final)
elif room_type=="suite":
   print("Final booking amount:",suite_final)
