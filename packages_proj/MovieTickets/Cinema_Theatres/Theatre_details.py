def shows(theatre_name):
    movies_list=[]
    show_timings=[]
    if theatre_name=="asian_mall":
        movies_list=['Vikram','777 Charlie','Ante Sundaraniki','Major','F3']
        show_timings_dict={'Vikram':['1:30pm','4:30pm','10:55pm'],
                           '777 Charlie':['10:30am','4:45pm','10:45pm'],
                           'Ante Sundaraniki':['12:50pm','4:10pm','7:30pm','10:50pm'],
                           'Major':['7:55pm'],
                           'F3':['1:40pm','7:50pm']
                           }
        return show_timings_dict


    elif theatre_name=="PVR_cinemas":
        movies_list=['Vikram','Ante Sundaraniki', 'Major']
        show_timings_dict = {'Vikram': ['1:30pm','10:55pm'],
                             'Ante Sundaraniki': ['4:10pm', '7:30pm', '10:50pm'],
                             'Major': ['7:15pm'],
                             }
        return show_timings_dict
    elif theatre_name=="Ashoka":
        movies_list=['Major']
        show_timings=["10:45am","2:15pm","5:50pm","9:30pm"]
        return show_timings

def theatre_selected(theatre_name):
    if theatre_name=="asian_mall":
        print("Address:Bus Stand Road, Beside Asian Sridevi Mall, Hanamkonda, Telangana 506001")
        print(shows(theatre_name))
    elif theatre_name=="PVR_cinemas":
        print("Address:8-8-7&8-8, 8, Station Rd, Warangal, Telangana 506002")
        print(shows(theatre_name))
    elif theatre_name=="Ashoka":
        print("Address:242, 6-1-242, Main Rd, Reddy Colony, Hanamkonda, Telangana 506002")
        print(shows(theatre_name))