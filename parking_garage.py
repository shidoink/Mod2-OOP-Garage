class parkingGarage():

    def __init__ (self, ticketsInMachine, ticketsSold, unpaidUsers, parkingSlotsAvailable, moneyCollected, paidUsers):
        self.ticketsInmachine= ticketsInMachine
        self.ticketsSold= ticketsSold
        self.unpaidUsers= unpaidUsers
        self.parkingSlotsAvailable=parkingSlotsAvailable
        self.moneyCollected = moneyCollected
        self.paidUsers = paidUsers

    def carDetectedIncoming(self):
        '''prompts user for information, provides ticket, enters user into system'''
        ticket_requested= input("Press any key to take ticket")
        if ticket_requested !='':
            self.ticketsInmachine -= 1
            self.ticketsSold += 1
            self.parkingSlotsAvailable-= 1
            license_plate= input("Please enter license plate number")
            parking_time= input("Please select parking duration: \n A) 0 -1 ($4) hr B) 1-2 ($5) hrs C) 2-3 ($6) hrs D) 3+ hrs ($7)")
            print( "Thank you, Please take the parking ticket.")
            
            self.unpaidUsers[license_plate]= parking_time
        
        else:
            "well, go away then"

    def carDetectedLeaving(self):
        user_input_license_plate= input("reading license plate number from ticket so no need to worry about input errors :) ")
        time_parked= self.unpaidUsers.get(user_input_license_plate)
        if time_parked== "A":
            print("Expected payment $4")
            self.moneyCollected += 4
        elif time_parked== "B":
            print("Expected payment $5")
            self.moneyCollected += 5
        elif time_parked== "C":
            print("Expected payment $6")
            self.moneyCollected += 6
        else:
            print("Expected payment $7")
            self.moneyCollected +=7
        card_info=input('reading card info (just type something in pls) ')
        if card_info!='':
            print('Thank you for your payment, have a nice day ')
            self.parkingSlotsAvailable+=1
            self.paidUsers.update({user_input_license_plate: time_parked})
            self.unpaidUsers.pop(user_input_license_plate)
        else:
            print("Card failed to read, try blowing it off. ")
        
    def adminSeeTotals(self):
        print("$" + self.moneyCollected)
    
    def adminSeeUnpaidParkers(self):
        print(self.unpaidUsers)
    
    def adminSeePaidParkers(self):
        print(self.paidUsers)
    
    def adminSeeTicketsInMachine(self):
        print(self.ticketsInmachine)
    
    def adminSeeSlots(self):
        print(self.parkingSlotsAvailable)

    def adminAddTickets(self):
        tickets_added= int(input("How many tickets are you adding? "))
        self.ticketsInmachine+=tickets_added





my_garage= parkingGarage(999,0,{},99,0,{})

system_running= True
while system_running:
    machine_input=input("Waiting input: Car (I)ncoming, Car (L)eaving, (A)dmin access, (S)hutdown system. ")
    
    if machine_input== "I":
        my_garage.carDetectedIncoming()

    elif machine_input== "L":
        my_garage.carDetectedLeaving()

    elif machine_input== "A":
        admin_access= True
        while admin_access:
            admin_selection=input("Hello admin! Please make selection: \n 'SeeTotals','SeeUnpaidParkers','SeePaidParkers','SeeTicketsinMachine','SeeSlots', 'AddTickets','exit'. ")
            if admin_selection== 'SeeTotals':
                my_garage.adminSeeTotals()
            elif admin_selection== 'SeeUnpaidParkers':
                my_garage.adminSeeUnpaidParkers()
            elif admin_selection== 'SeePaidParkers':
                my_garage.adminSeePaidParkers()
            elif admin_selection== 'SeeTicketsinMachine':
                my_garage.adminSeeTicketsInMachine()
            elif admin_selection== 'SeeSlots':
                my_garage.adminSeeSlots()
            elif admin_selection== 'AddTickets':
                my_garage.adminAddTickets()
            elif admin_selection== 'exit':
                admin_access= False
            else:
                'invalid input'

    elif machine_input=='S':
        system_running= False
    else:
        print("Invalid")
        
    




