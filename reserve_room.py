from scipy import signal
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle
from datetime import timedelta
import datetime
from datetime import datetime

class reservation():
    def __init__(self,single_room,double_room): ## this creates 2 arguments for the 2 different types of bookings
    ## init the variables
    
        self.all_days_list=[] ## list of all dates in the year 2019
        self.sr_tic=[] ## list of all dates 
        self.db_tic=[] ##list of all dates  it is same as sr_list
        self.sr_list={} # list is converted in dictionary to store the current booking value
        self.db_list={} # contains the list of all dates in 2019 and default rooms available
        self.x=0 ## this is used for plotting of two rooms
        self.y=0.15 ## this is also for creating plots to show reserved rooms as per date requested
        self.j=0# also a chart variable
        self.single_room=single_room ## init the user input variables
        self.double_room=double_room ## init the user defined vars
        ## we'll create a list to store all the dates and booking vals in a dictionary for the year 2019
        ## the code below creates two dictionaries which will be updated by user and has dates listed as string
        self.start_date = '01/01/2019' ## start date is 1-jan till 31 dec 2019
        self.start_date= datetime.strptime(self.start_date,'%m/%d/%Y') # convert string to datetime
        for i in range(365):# run till end of year
            self.ss=self.start_date+timedelta(i) # iterate by day
            self.ss2 = self.ss.strftime('%m/%d/%Y') # convert datetime to string (for asthetics)
            self.all_days_list.append(self.ss2)# add it to the list
            self.sr_tic.append(self.single_room) ## create two list with same dates to store separate reservation vars
            self.db_tic.append(self.double_room)
        self.sr_list=dict(zip(self.all_days_list,self.sr_tic)) ## combine two list to convert it to a dictionary
        self.db_list= dict(zip(self.all_days_list,self.db_tic))
        ## sr_list= single room list
        ## db_list =double room list
        
    
    ## function to book tickets
    def book_ti(self,from_d,to_d,num_tick,class_b):
        my_b_date= []## returns the list of booking dates
        nt=[] ## returns the number of tickets booked ( or rooms)
        from_d= datetime.strptime(from_d,'%m/%d/%Y') ## from booking date
        to_d = datetime.strptime(to_d,'%m/%d/%Y')  ## to booking date
        delta_d = to_d - from_d ## iterate by days
        for i in range(delta_d.days+1):
            jj=from_d+timedelta(i) 
            jj2=jj.strftime('%m/%d/%Y') ## convert it to string
            my_b_date.append(jj2)## create a list my_b_date to store booking dates vals
            nt.append(num_tick) ## number_of_tickets or number_of_rooms to be booked
        book_det =dict(zip(my_b_date,nt)) ## create a dictionary to store the vals of reservation dates with the number of tickets
        if class_b=='ec': # if classs is 'ec' or economy or single room
            dd= {key:self.db_list[key]-book_det.get(key,0) for key in self.db_list.keys()} # create a list to store the vals(final value is whatever number of tickets left after subtracting the total number of tickets)
            if len([(k,v) for k,v in dd.items() if v<0]) >=1: ## the logic makes sure that if user inputs number of tickets larger than the available ones then the code will break by printing error and number of rooms or tickets available 
                print('error no more seats left')##____ would be the rooms available before the booking (there would be no booking recorded )
                self.db_list= self.db_list ## if the user inputs the number of tickets to be in range within the available number of tickets then the reservation will take place
            else:
                print('booking_confirmed')
                self.db_list= dd    
        if class_b =='fc': ## similar logic as above just the booking _class will be different
            aa=  {key:self.sr_list[key]- book_det.get(key,0) for key in self.sr_list.keys()}
            if len([(k,v) for k,v in aa.items() if v<0])>=1:
                print('error no more seats left')
                self.sr_list= self.sr_list
            else:
                print('booking_confirmed')
                self.sr_list = aa
   
    def plot(self,date_look): ### this code plots the available seats and the booked seats
        currentAxis= plt.gca() ## add plot
        self.j=0 ## iterating value which prints individual seats
        self.y=0 ## y_axis - set it to zero initially
        self.x=0 ## x_axis - set it to zero intially
        for i in range(self.single_room): ## add the number of rooms in the graph and paint them red
            currentAxis.add_patch(Rectangle((self.x+self.j,self.y),0.08,0.2,facecolor='red')) ## this adds rectangular patches to the graph
            self.j+=0.1 ## iterates overt the number of rooms
        
        self.j=0 ## set it back to zeroo so that our code can paint the available seats blue
        for i in range(self.sr_list[date_look]):  
            currentAxis.add_patch(Rectangle((self.x+self.j,self.y),0.08,0.2,facecolor ='blue'))
            self.j+=0.1
        self.y = 0.5
        self.j = 0
        for i in range(self.double_room): ## the second row of data represents economy class or double bed room
            currentAxis.add_patch(Rectangle((self.x+self.j,self.y),0.08,0.2,facecolor='red')) 
            self.j+=0.1
        self.j= 0
        for i in range(self.db_list[date_look]):
            currentAxis.add_patch(Rectangle((self.x+self.j,self.y),0.08,0.2,facecolor= 'blue')) 
            self.j+=0.1
        return currentAxis
                
    def dbr(self,lookup_var):## this function returns the list of dates with booked tickets if argument is 'booked' else it returns everything
        if lookup_var=='booked': 
            rr=[(k,v) for k,v in self.db_list.items() if v<10]
        else:
            rr=[(k,v) for k,v in self.db_list.items() if v==10]
        return rr
    
    def sbr(self,lookup_var):
        if lookup_var=='booked':
            rr=[(k,v) for k,v in self.sr_list.items() if v<10]
        else:
            rr=[(k,v) for k,v in self.sr_list.items() if v==10]
        return rr
    

#### running the code
rr2=reservation(10,10)
rr2.book_ti('12/10/2019','12/31/2019',7,'ec')
rr2.book_ti('12/10/2019','12/31/2019',1,'ec')
rr2.book_ti('12/10/2019','12/31/2019',3,'ec')
rr2.dbr('booked')
rr2.plot('12/10/2019')

rr2.book_ti('12/10/2019','12/31/2019',3,'fc')
rr2.plot('12/10/2019')
rr2.sbr('booked')
rr2.plot('12/10/2019')



    







