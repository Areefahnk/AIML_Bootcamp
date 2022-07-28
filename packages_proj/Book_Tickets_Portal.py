import MovieTickets
from MovieTickets.Cinema_Theatres import Theatre_details as td
print("Select the Movie Theatre:")
print('''1. asian_mall,
2. PVR_cinemas,
3. Ashoka''')
theatre_name=int(input("Enter the selection (1/2/3)"))
if theatre_name==1:
    td.theatre_selected('asian_mall')
elif theatre_name==2:
    td.theatre_selected('PVR_cinemas')
elif theatre_name==3:
    td.theatre_selected('Ashoka')

