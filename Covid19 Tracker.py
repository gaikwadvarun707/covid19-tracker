#Code To Track Covid19 Using Python

for i in range(0,100):
    print(" ")

    #importing covid module
    from covid import Covid
    print("Covid Tracker")
    cv=Covid()

    #Global Results with the help of predefined functions
    #assigned variables to the predefined function

    act=cv.get_total_active_cases()
    rec=cv.get_total_recovered()
    death=cv.get_total_deaths()
    con=cv.get_total_confirmed_cases()

    print("1.Global Count") #get all the global covid updates
    print("2.Active Cases")
    print("3.Confirmed Cases")
    print("4.Recovered Cases")
    print("5.Deceased")
    print("6.Get Covid Updtes By Country Name")

    choice=input("Enter a number of your choice :")

    #if-elif-else statements used

    if choice == '1':
        print("Active Cases ",act, "\nConfirmed Cases ",con,"\nRecovered Cases ",rec,"\nDeceased :",death)

    elif choice =='2':
        print("Active Cases :",act)

    elif choice=='3':
        print("Confirmed Cases :",con)

    elif choice=='4':
        print("Recovered Cases :",rec)

    elif choice=='5':
        print("Deceased :",death)

    elif choice=='6':
        str =i =input("Enter Country Name :")#get the status of Covid19 in a perticular country
        cname =cv.get_status_by_country_name(i)
        print(cname)

    else:
        print("Invalid Option")
