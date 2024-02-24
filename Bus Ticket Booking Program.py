#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[9]:


import random
import pandas as pd
import cv2 as cv
from colorama import Fore,Back,Style
import qrcode
from datetime import datetime

class JaipurTravelService:
    
    def date_validation(self):

        current_date = datetime.now().date()

        while True:
            
            self.date=input("Enter the date(format--> dd-mm-yyyy):")
            
            try:
                # Convert user input to datetime object
                self.date = datetime.strptime(self.date, "%d-%m-%Y").date()

                # Compare dates
                if self.date > current_date:
                    break
                else:
                    print("Error: The entered date is before the current date. Please try again.")
                    
            except ValueError:
                print("Error: Please enter a date in the correct format (DD-MM-YYYY).\n")
            

    
    d=[]
    random_no=[]
    def qr_code(self,url1,img1):
        qr=qrcode.QRCode(version=1,box_size=10,border=10)

        qr.add_data(url1)
        qr.make(fit=True)
        img=qr.make_image(fill_colour="red",back_colour="red")
        img.save(img1)
        image=cv.imread(img1)
        cv.imshow("img",image)
        cv.waitKey(0)
    def __init__(self):
        from colorama import Fore,Back,Style
        print(Fore.RED+Style.BRIGHT+"\t\t\t\t\t\t     Travel Bug")
        print("\t\t\t\t\t\t    {Since 1995}")
        print("\t\t\t\t\t        www.travelmasters.com")
        print("Book Your Buses")
        self.d=[]
        self.name=[]
        self.mn=[]
        self.age=[]
        print(Fore.BLUE+Style.BRIGHT)
        
        self.date_validation()
        while True:
            origin_list = ["Jaipur","Alwar","Jodhpur","Bharatpur","Ajmer","Kota","Delhi"]
            print("\nOrigin Cities:\n",origin_list)
            origin= input("Enter the orgin city name:")
            
            if origin in ["Jaipur","jaipur","JAIPUR"]:
                pickuppoint_list=["Sindhi Camp","200ft, Ajmer Road"]
                self.Jaipur()
                break

            elif origin in ["ALWAR","Alwar","alwar"]:
                self.Alwar()
                break
                
            elif origin in ["JODHPUR","Jodhpur","jodhpur"]:
                self.Jodhpur()
                break

            elif origin in ["BHARATPUR","Bharatpur","bharatpur"]:
                self. Bharatpur()
                break

            elif origin in ["AJMER","Ajmer","ajmer"]:
                self.Ajmer()
                break

            elif origin in ["KOTA","Kota","kota"]:
                self.Kota()
                break

            elif origin in ["DELHI","Delhi","delhi"]:
                self.Delhi()
                break
            else:
                print("Invalid Input! Please Re-enter....\n")

    def Jaipur(self):
        
        while True:
            dest_list=["Alwar","Jodhpur","Bharatpur","Ajmer","Kota","Delhi"]
            self.pickuppoint_list=["Sindhi Camp","200ft, Ajmer Road"]
            print("\nDestination Cities:\n",dest_list)

            destination=input("Enter the destination city name:")
        
            if destination in ["Jodhpur","jodhpur","JODHPUR"]:
                company_name=["Jain Travels","Gajraj Travels","M R Travels","Jakhar Travels","Sainath Travel Agency","Jain Travels"]
                bus_type=["AC Seater","AC Sleeper","AC Sleeper","Non-AC Seater","Non-AC Sleeper","AC Sleeper"]
                price=[550,900,900,500,600,800]
                timing=["10:30 AM - 05:05 PM","10.30 PM - 05:35 AM","10:30 PM - 05:30 AM","09:00 AM - 04:45 PM","10:30 PM - 06:00 AM","11:00 PM - 05:45 AM"]
                duration=["06h 35m","07h 05m","07h 00m","07h 45m","07h 30m","06h 45m"]
                self.bus={"Company Name":company_name,"Bus Type":bus_type,"Price":price,"Duration":duration,"Timing":timing}
                df=pd.DataFrame(self.bus)
                df.index=df.index+1
                print("\n\n\t\t\t\t---Buses Information Chart---\n")
                print("Jaipur -- to -- Jodhpur\n")
                print(df.to_string(index=True))
        #       break
                self.drop_point="Basni Mandi Mode Pali Road"
                break

            elif destination in ["Alwar","alwar","ALWAR"]:
                company_name=["M R Travels","B R Travels","M R Travels","Yadav Bus Service","Deepak Tour & Travels"]
                bus_type=["AC Seater","AC Sleeper","AC Seater","Non-AC Seater","Non-AC Sleeper"]
                price=[950,1600,500,289,600]
                timing=["02:00 AM - 04:00 AM","05.10 AM - 07:00 AM","10:30 AM - 12:30 PM","09:00 AM - 12:20 PM","01:00 PM - 04:11 PM"]
                duration=["02h 00m","01h 50m","02h 00m","03h 20m","03h 11m"]
                self.bus={"Company Name":company_name,"Bus Type":bus_type,"Price":price,"Duration":duration,"Timing":timing}
                df=pd.DataFrame(self.bus)
                df.index=df.index+1
                print("\n\n\t\t\t\t---Buses Information Chart---\n")
                print("Jaipur -- to -- Alwar\n")
                print(df.to_string(index=True))
                self.drop_point="Delhi Mumbai Express Highway, Alwar"
                break
                
            elif destination in ["BHARATPUR","Bharatpur","bharatpur"]:
                company_name=["NueGo","Sethi Yatra Company","Vijay Travels","Goyal Travels","Jain Travels regd"]
                bus_type=["AC Seater","AC Sleeper","AC Seater","AC Seater","Non-AC Seater"]
                price=[266,600,400,599,1000]
                timing=["06:00 AM - 10:15 AM","02.30 PM - 06:25 PM","03:30 AM - 06:50 AM","05:30 PM - 09:35 PM","11:50 PM - 03:35 AM"]
                duration=["04h 15m","03h 55m","03h 20m","04h 05m","03h 45m"]
                self.bus={"Company Name":company_name,"Bus Type":bus_type,"Price":price,"Duration":duration,"Timing":timing}
                df=pd.DataFrame(self.bus)
                df.index=df.index+1
                print("\n\n\t\t\t\t---Buses Information Chart---\n")
                print("Jaipur -- to -- Bharatpur\n")
                print(df.to_string(index=True))
                self.drop_point="Baypass bharatpur"
                break
                
            elif destination in ["AJMER","Ajmer","ajmer"]:
                company_name=["Anshi Raj Shree Travels","Jai Nathdwara Travels","Jai Nathdwara Travels","Jain Parshwanath Travels Jaipur","Jain Travels regd"]
                bus_type=["AC Sleeper","AC Sleeper","Non-AC Seater","AC Sleeper","AC Seater"]
                price=[299,600,800,289,600,599]
                timing=["04:00 AM - 07:15 AM","10.15 PM - 12:45 AM","03:15 PM - 12:30 PM","09:00 AM - 12:20 PM","01:00 PM - 04:11 PM"]
                duration=["02h 00m","01h 50m","02h 00m","03h 20m","03h 11m"]
                self.bus={"Company Name":company_name,"Bus Type":bus_type,"Price":price,"Duration":duration,"Timing":timing}
                df=pd.DataFrame(self.bus)
                df.index=df.index+1
                print("\n\n\t\t\t\t---Buses Information Chart---\n")
                print("Jaipur -- to -- Ajmer\n")
                print(df.to_string(index=True))
                self.drop_point="Parbatpura Bypass, Ajmer"
                break
                
            elif destination in ["KOTA","Kota","kota"]:
                company_name=["Babu Travels","Navrang Travels","Jai Shrinath Ji Ki","Babu Travels","Mahalaxmi Travels"]
                bus_type=["Non-AC Seater","AC Sleeper","Non-AC Sleeper","AC Seater","AC Sleeper"]
                price=[250,500,400,1150,750]
                timing=["10:15 AM - 04:19 PM","11.00 PM - 05:00 AM","10:30 PM - 05:00 AM","04:30 AM - 09:15 PM","05:30 AM - 10:45 PM"]
                duration=["06h 04m","06h 00m","06h 30m","04h 45m","05h 15m"]
                self.bus={"Company Name":company_name,"Bus Type":bus_type,"Price":price,"Duration":duration,"Timing":timing}
                df=pd.DataFrame(self.bus)
                df.index=df.index+1
                print("\n\n\t\t\t\t---Buses Information Chart---\n")
                print("Jaipur -- to -- Kota\n")
                print(df.to_string(index=True))
                self.drop_point="Swami Vivekanda Chauraha"
                break

            elif destination in ["DELHI","Delhi","delhi"]:
                company_name=["Zingbus Plus","NueGo","Goldline Super Deluxe","Shakti Travels","Gajraj Travels"]
                bus_type=["AC Sleeper","AC Seater","AC Sleeper","Non-AC Seater","AC Sleeper"]
                price=[393,371,550,250,500]
                timing=["10:15 PM - 05:00 AM","09.30 AM - 03:00 PM","11:50 PM - 05:45 AM","11:55 PM - 06:15 AM","02:15 AM - 06:30 AM"]
                duration=["06h 45m","05h 30m","05h 55m","06h 20m","04h 15m"]
                self.bus={"Company Name":company_name,"Bus Type":bus_type,"Price":price,"Duration":duration,"Timing":timing}
                df=pd.DataFrame(self.bus)
                df.index=df.index+1
                print("\n\n\t\t\t\t---Buses Information Chart---\n")
                print("Jaipur -- to -- Delhi\n")
                print(df.to_string(index=True))
                self.drop_point="Dhaula kuan Bus Stand"
                break

            else:
                print("Invalid Destination Name! Please re-enter.....\n")
        
        self.pass_details()
        self.payment_page()
        self.ticket()
                
    def Alwar(self):
        while True:
            dest_list=["Jaipur","Jodhpur","Bharatpur","Ajmer","Kota","Delhi"]
            pickuppoint_list=["Delhi Mumbai express way, BUS STAND","Roadways Bus stand Alwar, Lal diggi road"]
            print("\nDestination Cities:\n",dest_list)

            destination=input("Enter the destination city name:")
        
            if destination in ["Jaipur","jaipur","JAIPUR"]:
                company_name=["M R Travels","Shree Karni Travels","Jakhar Travels","Yadav Bus Service","Deepak Tour & Travels"]
                bus_type=["AC Sleeper","Non-AC Sleeper","AC Seater","Non-AC Seater","Non-AC Sleeper"]
                price=[1600,450,1000,289,700]
                timing=["10:30 AM - 05:05 PM","10.30 PM - 05:35 AM","10:30 PM - 05:30 AM","09:00 AM - 04:45 PM","10:30 PM - 06:00 AM","11:00 PM - 05:45 AM"]
                duration=["06h 35m","07h 05m","07h 00m","07h 45m","07h 30m","06h 45m"]
                self.bus={"Company Name":company_name,"Bus Type":bus_type,"Price":price,"Duration":duration,"Timing":timing}
                df=pd.DataFrame(self.bus)
                df.index=df.index+1
                print("\n\n\t\t\t\t---Buses Information Chart---\n")
                print("Alwar -- to -- Jaipur\n")
                print(df.to_string(index=True))
        #       break
                self.drop_point="Sindhi Camp Bus Stand"
                break

            elif destination in ["Jodhpur","jodhpur","JODHPUR"]:
                company_name=["M R Travels","Jakhar Travels","Jakhar Travels"]
                bus_type=["AC Sleeper","AC Seater","AC Sleeper"]
                price=[1000,700.888]
                timing=["11:30 PM - 09:00 AM","11.30 PM - 08:30 AM","11.30 PM - 08:30 AM"]
                duration=["09h 30m","09h 00m","09h 00m"]
                self.bus={"Company Name":company_name,"Bus Type":bus_type,"Price":price,"Duration":duration,"Timing":timing}
                df=pd.DataFrame(self.bus)
                df.index=df.index+1
                print("\n\n\t\t\t\t---Buses Information Chart---\n")
                print("Alwar -- to -- Jodhpur\n")
                print(df.to_string(index=True))
        #       break
                self.drop_point="Basni Mandi Mode Pali Road"
                break                
            elif destination in ["BHARATPUR","Bharatpur","bharatpur"]:
                company_name=["Vijay Travels","Vijay Travels"]
                bus_type=["AC Seater","AC Sleeper"]
                price=[400,550]
                timing=["03:00 AM - 06:00 AM","03:00 AM - 06:00 AM"]
                duration=["03h 00m","03h 00m"]
                self.bus={"Company Name":company_name,"Bus Type":bus_type,"Price":price,"Duration":duration,"Timing":timing}
                df=pd.DataFrame(self.bus)
                df.index=df.index+1
                print("\n\n\t\t\t\t---Buses Information Chart---\n")
                print("Alwar -- to -- Bharatpur\n")
                print(df.to_string(index=True))
                self.drop_point="Baypass bharatpur"
                break
                
            elif destination in ["AJMER","Ajmer","ajmer"]:
                company_name=["M R Travels","Jakhar Travels","M R Travels","Jakhar Travels"]
                bus_type=["AC Sleeper","AC Sleeper","AC Sleeper","AC Seater"]
                price=[1000,1200,1600,1000]
                timing=["11:30 PM - 04:30 AM","11.30 PM - 05:00 AM","08:15 PM - 01:00 AM","11.30 PM - 05:00 AM"]
                duration=["05h 00m","05h 30m","02h 00m","04h 45m","05h 30m"]
                self.bus={"Company Name":company_name,"Bus Type":bus_type,"Price":price,"Duration":duration,"Timing":timing}
                df=pd.DataFrame(self.bus)
                df.index=df.index+1
                print("\n\n\t\t\t\t---Buses Information Chart---\n")
                print("Alwar -- to -- Ajmer\n")
                print(df.to_string(index=True))
                self.drop_point="Parbatpura Bypass, Ajmer"
                break
                
            elif destination in ["KOTA","Kota","kota"]:
                company_name=["Ashok Travels","Gajraj Travels","Gajraj Travels","BR Travels","Ashok Travels"]
                bus_type=["Non-AC Seater","AC Sleeper","AC Sleeper","AC Sleeper","Non-AC Sleeper"]
                price=[1010,1600,1700,2999,1210]
                timing=["10.30 PM - 05:00 AM","11.00 PM - 04:20 AM","09:00 PM - 02:50 AM","10:25 PM - 05:15 AM","10.30 PM - 05:00 AM"]
                duration=["06h 30m","05h 20m","05h 50m","06h 50m","06h 30m"]
                self.bus={"Company Name":company_name,"Bus Type":bus_type,"Price":price,"Duration":duration,"Timing":timing}
                df=pd.DataFrame(self.bus)
                df.index=df.index+1
                print("\n\n\t\t\t\t---Buses Information Chart---\n")
                print("Alwar -- to -- Kota\n")
                print(df.to_string(index=True))
                self.drop_point="Swami Vivekanda Chauraha"
                break

            elif destination in ["DELHI","Delhi","delhi"]:
                company_name=["Deepak Travels","P.G Travels","Parmar Travels","M R Travels","B R Travels"]
                bus_type=["Non-AC Sleeper","Non-AC Seater","Non-AC Seater","AC Sleeper","AC Sleeper"]
                price=[679,503,399,950,999]
                timing=["11:30 PM - 01:50 AM","11.35 PM - 05:00 AM","11:15 PM - 04:00 AM","04:00 AM - 07:00 AM","07:00 AM - 09:45 AM"]
                duration=["02h 15m","05h 25m","04h 45m","03h 00m","02h 45m"]
                self.bus={"Company Name":company_name,"Bus Type":bus_type,"Price":price,"Duration":duration,"Timing":timing}
                df=pd.DataFrame(self.bus)
                df.index=df.index+1
                print("\n\n\t\t\t\t---Buses Information Chart---\n")
                print("Alwar -- to -- Delhi\n")
                print(df.to_string(index=True))
                self.drop_point="Dhaula kuan Bus Stand"
                break

            else:
                print("Invalid Destination Name! Please re-enter.....\n")
        
        self.pass_details()
        self.payment_page()
        self.ticket()
    
    def Jodhpur(self):
        
        while True:
            dest_list=["Jaipur","Alwar","Bharatpur","Ajmer","Kota","Delhi"]
            self.pickuppoint_list=["Jhalamand Circle","12th road"]
            print("\nDestination Cities:\n",dest_list)

            destination=input("Enter the destination city name:")
        
            if destination in ["Jaipur","jaipur","JAIPUR"]:
                company_name=["RR Travels RADHA RAMAN","M R Travels","Gajraj Travels","Jain Travels regd","Shree Ganesh Travels"]
                bus_type=["AC Seater","AC Seater","AC Sleeper","Non-AC Sleeper","AC Seater"]
                price=[500,500,650,550,400]
                timing=["07:00 PM - 02:30 AM","10.45 PM - 06:00 AM","10:00 PM - 05:10 AM","10:00 PM - 06:12 AM","01:30 AM - 06:45 AM"]
                duration=["07h 30m","07h 15m","07h 10m","08h 12m","05h 15m"]
                self.bus={"Company Name":company_name,"Bus Type":bus_type,"Price":price,"Duration":duration,"Timing":timing}
                df=pd.DataFrame(self.bus)
                df.index=df.index+1
                print("\n\n\t\t\t\t---Buses Information Chart---\n")
                print("Jodhpur -- to -- Jaipur\n")
                print(df.to_string(index=True))
        #       break
                self.drop_point="Sindhi Camp Bus Stand"
                break

            elif destination in ["Alwar","alwar","ALWAR"]:
                company_name=["Jakhar Travels","Jakhar Travels","M R Travels"]
                bus_type=["AC Seater","AC Sleeper","AC Sleeper"]
                price=[850,950,950]
                timing=["08.15 PM - 05:00 AM","08.15 PM - 05:00 AM","07:30 PM - 04:00 AM"]
                duration=["08h 45m","08h 45m","08h 30m"]
                self.bus={"Company Name":company_name,"Bus Type":bus_type,"Price":price,"Duration":duration,"Timing":timing}
                df=pd.DataFrame(self.bus)
                df.index=df.index+1
                print("\n\n\t\t\t\t---Buses Information Chart---\n")
                print("Jodhpur -- to -- Alwar\n")
                print(df.to_string(index=True))
                self.drop_point="Delhi Mumbai Express Highway, Alwar"
                break
                
            elif destination in ["BHARATPUR","Bharatpur","bharatpur"]:
                company_name=["Jain Travels regd","Jakhar Travels","M R Travels","Om Travels","Pooja Parswanath Travels"]
                bus_type=["Non-AC Seater","Non-AC Sleeper","AC Seater","AC Sleeper","AC Sleeper"]
                price=[650,850,650,1100,900]
                timing=["05:00 PM - 05:15 AM","10:00 PM - 08:55 AM","10:05 PM - 08:45 AM","03:00 PM - 02:59 AM","09:45 PM - 07:55 AM"]
                duration=["12h 15m","10h 55m","10h 40m","11h 59m","10h 10m"]
                self.bus={"Company Name":company_name,"Bus Type":bus_type,"Price":price,"Duration":duration,"Timing":timing}
                df=pd.DataFrame(self.bus)
                df.index=df.index+1
                print("\n\n\t\t\t\t---Buses Information Chart---\n")
                print("Jodhpur -- to -- Bharatpur\n")
                print(df.to_string(index=True))
                self.drop_point="Baypass bharatpur"
                break
                
            elif destination in ["AJMER","Ajmer","ajmer"]:
                company_name=["Gajraj Travels","Jain Travels regd","Shree Ganesh Travels","Jakhar Travels","Bhagwati Tours & Travels"]
                bus_type=["AC Sleeper","AC Sleeper","AC Seater","AC Seater","AC Sleeper"]
                price=[650,650,700,400,618]
                timing=["10:00 PM - 03:10 AM","10.30 PM - 02:20 AM","11:00 PM - 03:30 AM","09:00 PM - 05:27 AM","11:30 PM - 04:00 AM"]
                duration=["05h 10m","03h 50m","04h 16m","04h 30m","04h 30m"]
                self.bus={"Company Name":company_name,"Bus Type":bus_type,"Price":price,"Duration":duration,"Timing":timing}
                df=pd.DataFrame(self.bus)
                df.index=df.index+1
                print("\n\n\t\t\t\t---Buses Information Chart---\n")
                print("Jodhpur -- to -- Ajmer\n")
                print(df.to_string(index=True))
                self.drop_point="Parbatpura Bypass, Ajmer"
                break
                
            elif destination in ["KOTA","Kota","kota"]:
                company_name=["Gajraj Travels","Jain Travels regd","M R Travels","Babu Travels","Jakhar Travels"]
                bus_type=["AC Sleeper","AC Seater","AC Sleeper","Non-AC Seater","Non-AC Sleeper"]
                price=[700,550,700,450,600]
                timing=["10:00 PM - 06:00 AM","10:00 PM - 06:15 AM","10:00 PM - 06:05 AM","09:15 PM - 06:05 AM","10:00 PM - 06:15 AM"]
                duration=["08h 00m","08h 40m","08h 05m","08h 50m","08h 15m"]
                self.bus={"Company Name":company_name,"Bus Type":bus_type,"Price":price,"Duration":duration,"Timing":timing}
                df=pd.DataFrame(self.bus)
                df.index=df.index+1
                print("\n\n\t\t\t\t---Buses Information Chart---\n")
                print("Jodhpur -- to -- Kota\n")
                print(df.to_string(index=True))
                self.drop_point="Swami Vivekanda Chauraha"
                break

            elif destination in ["DELHI","Delhi","delhi"]:
                company_name=["Jakhar Travels","Bluecity Bus","M R Travels","Gajraj Travels","Jain Travels regd"]
                bus_type=["AC Seater","AC Sleeper","AC Sleeper","AC Sleeper","Non-AC Sleeper"]
                price=[850,950,950,950,850]
                timing=["08:15 PM - 06:40 AM","07:00 PM - 07:50 AM","07:30 PM - 07:00 AM","07:30 PM - 06:30 AM","07:00 PM - 08:14 AM"]
                duration=["10h 25m","12h 50m","11h 30m","11h 00m","13h 14m"]
                self.bus={"Company Name":company_name,"Bus Type":bus_type,"Price":price,"Duration":duration,"Timing":timing}
                df=pd.DataFrame(self.bus)
                df.index=df.index+1
                print("\n\n\t\t\t\t---Buses Information Chart---\n")
                print("Jodhpur -- to -- Delhi\n")
                print(df.to_string(index=True))
                self.drop_point="Dhaula kuan Bus Stand"
                break

            else:
                print("Invalid Destination Name! Please re-enter.....\n")
        
        self.pass_details()
        self.payment_page()
        self.ticket()
        
    def Bharatpur(self):
        
        while True:
            dest_list=["Jaipur","Alwar","Jodhpur","Ajmer","Kota","Delhi"]
            self.pickuppoint_list=["Bharatpur Saras Chauraha","Dehra modh jaipur byepass"]
            print("\nDestination Cities:\n",dest_list)

            destination=input("Enter the destination city name:")

            if destination in ["Jaipur","jaipur","JAIPUR"]:
                company_name=["NueGo","B G Travels","RR Travels","Anshi Raj Shree Travels","Vijay Travels","Jain Travels regd"]
                bus_type=["AC Seater","AC Sleeper","AC Seater","AC Sleeper","AC Sleeper","Non-AC Sleeper"]
                price=[371,550,1200,1299,950,900]
                timing=["03:15 PM - 06:25 PM","04.00 PM - 08:10 PM","05:30 PM - 10:20 PM","05:30 AM - 09:30 AM","12:50 AM - 03:50 AM","06:40 PM - 11:15 PM"]
                duration=["03h 10m","04h 10m","04h 50m","04h 00m","03h 00m","04h 35m"]
                self.bus={"Company Name":company_name,"Bus Type":bus_type,"Price":price,"Duration":duration,"Timing":timing}
                df=pd.DataFrame(self.bus)
                df.index=df.index+1
                print("\n\n\t\t\t\t---Buses Information Chart---\n")
                print("Bharatpur -- to -- Jaipur\n")
                print(df.to_string(index=True))
        #       break
                self.drop_point="Sindhi Camp Bus Stand"
                break

            elif destination in ["Alwar","alwar","ALWAR"]:
                company_name=["Vijay Travels","Vijay Travels"]
                bus_type=["AC Seater","AC Sleeper"]
                price=[400,700]
                timing=["07:30 PM - 10:30 PM","07:30 PM - 10:30 PM"]
                duration=["03h 00m","03h 00m"]
                self.bus={"Company Name":company_name,"Bus Type":bus_type,"Price":price,"Duration":duration,"Timing":timing}
                df=pd.DataFrame(self.bus)
                df.index=df.index+1
                print("\n\n\t\t\t\t---Buses Information Chart---\n")
                print("Bharatpur -- to -- Alwar\n")
                print(df.to_string(index=True))
                self.drop_point="Delhi Mumbai Express Highway, Alwar"
                break
                
            elif destination in ["Jodhpur","jodhpur","JODHPUR"]:
                company_name=["M R Travels","B R Travels","M R Travels","Yadav Bus Service","Deepak Tour & Travels"]
                bus_type=["AC Seater","AC Sleeper","AC Seater","Non-AC Seater","Non-AC Sleeper"]
                price=[950,1600,500,289,600,599]
                timing=["02:00 AM - 04:00 AM","05.10 AM - 07:00 AM","10:30 AM - 12:30 PM","09:00 AM - 12:20 PM","01:00 PM - 04:11 PM"]
                duration=["02h 00m","01h 50m","02h 00m","03h 20m","03h 11m"]
                self.bus={"Company Name":company_name,"Bus Type":bus_type,"Price":price,"Duration":duration,"Timing":timing}
                df=pd.DataFrame(self.bus)
                df.index=df.index+1
                print("\n\n\t\t\t\t---Buses Information Chart---\n")
                print("Bharatpur -- to -- Jodhpur\n")
                print(df.to_string(index=True))
                self.drop_point="Basni Mandi Mode Pali Road"
                break
                
            elif destination in ["AJMER","Ajmer","ajmer"]:
                company_name=["M R Travels","Jain Travels regd","Jakhar Travels","R.R Travels","B G Travels"]
                bus_type=["AC Seater","Non-AC Sleeper","AC Sleeper","AC Seater","AC Sleeper"]
                price=[770,900,857,599,1199]
                timing=["12:20 AM - 11:15 AM","09.10 PM - 08:00 AM","06:30 PM - 04:40 AM","06:00 PM - 05:40 AM","05:30 PM - 05:25 AM"]
                duration=["10h 55m","10h 50m","10h 10m","11h 40m","11h 55m"]
                self.bus={"Company Name":company_name,"Bus Type":bus_type,"Price":price,"Duration":duration,"Timing":timing}
                df=pd.DataFrame(self.bus)
                df.index=df.index+1
                print("\n\n\t\t\t\t---Buses Information Chart---\n")
                print("Bharatpur -- to -- Kota\n")
                print(df.to_string(index=True))
                self.drop_point="Parbatpura Bypass, Ajmer"
                break
                
            elif destination in ["KOTA","Kota","kota"]:
                company_name=["Yadav Vishvakarma Travels","Yadav Vishvakarma Travels"]
                bus_type=["Non-AC Seater","Non-AC Sleeper"]
                price=[800,1100]
                timing=["02:56 AM - 11:41 AM","02:56 AM - 11:41 AM"]
                duration=["08h 45m","08h 45m"]
                self.bus={"Company Name":company_name,"Bus Type":bus_type,"Price":price,"Duration":duration,"Timing":timing}
                df=pd.DataFrame(self.bus)
                df.index=df.index+1
                print("\n\n\t\t\t\t---Buses Information Chart---\n")
                print("Bharatpur -- to -- Kota\n")
                print(df.to_string(index=True))
                self.drop_point="Swami Vivekanda Chauraha"
                break

            elif destination in ["DELHI","Delhi","delhi"]:
                company_name=["Yadav Vishvakarma Travels","Yadav Vishvakarma Travels"]
                bus_type=["Non-AC Seater","Non-AC Sleeper"]
                price=[400,600]
                timing=["03:00 AM - 07:00 AM","03:00 AM - 07:00 AM"]
                duration=["04h 00m","04h 00m"]
                self.bus={"Company Name":company_name,"Bus Type":bus_type,"Price":price,"Duration":duration,"Timing":timing}
                df=pd.DataFrame(self.bus)
                df.index=df.index+1
                print("\n\n\t\t\t\t---Buses Information Chart---\n")
                print("Bharatpur -- to -- Delhi\n")
                print(df.to_string(index=True))
                self.drop_point="Dhaula kuan Bus Stand"
                break

            else:
                print("Invalid Destination Name! Please re-enter.....\n")
        
        self.pass_details()
        self.payment_page()
        self.ticket()
        
    def Ajmer(self):
        while True:
            dest_list=["Jaipur","Alwar","Jodhpur","Bharatpur","Kota","Delhi"]
            self.pickuppoint_list=["Prabhatapura bypass Ajmer"]
            print("\nDestination Cities:\n",dest_list)

            destination=input("Enter the destination city name:")
        
            if destination in ["Jaipur","jaipur","JAIPUR"]:
                company_name=["Jain Travels regd","Pooja Yaduvanshi Travels","RR Travels","Anshi Raj Shree Travels","Jain Travels regd"]
                bus_type=["AC Seater","AC Sleeper","AC Seater","AC Sleeper","Non-AC Sleeper"]
                price=[250,600,500,999,350]
                timing=["06:00 PM - 08:45 PM","04.30 AM - 06:15 AM","12:15 AM - 02:30 AM","06:00 PM - 09:15 PM","04:00 PM - 06:45 PM"]
                duration=["02h 45m","01h 45m","02h 15m","03h 15m","02h 45m"]
                self.bus={"Company Name":company_name,"Bus Type":bus_type,"Price":price,"Duration":duration,"Timing":timing}
                df=pd.DataFrame(self.bus)
                df.index=df.index+1
                print("\n\n\t\t\t\t---Buses Information Chart---\n")
                print("Ajmer -- to -- Jaipur\n")
                print(df.to_string(index=True))
        #       break
                self.drop_point="Sindhi Camp Bus Stand"
                break

            elif destination in ["Alwar","alwar","ALWAR"]:
                company_name=["Jakhar Travels","Jakhar Travels","M R Travels"]
                bus_type=["AC Seater","AC Sleeper","AC Sleeper"]
                price=[700,888,1500]
                timing=["12:45 AM - 05:00 AM","12:45 AM - 05:00 AM","01:00 AM - 05:30 AM"]
                duration=["04h 15m","04h 15m","04h 30m"]
                self.bus={"Company Name":company_name,"Bus Type":bus_type,"Price":price,"Duration":duration,"Timing":timing}
                df=pd.DataFrame(self.bus)
                df.index=df.index+1
                print("\n\n\t\t\t\t---Buses Information Chart---\n")
                print("Ajmer -- to -- Alwar\n")
                print(df.to_string(index=True))
                self.drop_point="Delhi Mumbai Express Highway, Alwar"
                break
                
            elif destination in ["BHARATPUR","Bharatpur","bharatpur"]:
                company_name=["Jay Bajrang Travels Agency","Jain Travels regd","Jakhar Travels","Choudhary Travels & Cargo","Kamal Travels"]
                bus_type=["AC Seater","Non-AC Sleeper","Non-AC Seater","AC Sleeper","Non-AC Sleeper"]
                price=[600,800,500,1200,800]
                timing=["01:20 AM - 07:30 AM","08.30 PM - 02:45 AM","02:30 AM - 08:55 AM","07:30 PM - 12:00 AM","08:30 PM - 03:30 AM"]
                duration=["06h 10m","06h 15m","06h 25m","04h 30m","07h 00m"]
                self.bus={"Company Name":company_name,"Bus Type":bus_type,"Price":price,"Duration":duration,"Timing":timing}
                df=pd.DataFrame(self.bus)
                df.index=df.index+1
                print("\n\n\t\t\t\t---Buses Information Chart---\n")
                print("Ajmer -- to -- Bharatpur\n")
                print(df.to_string(index=True))
                self.drop_point="Baypass bharatpur"
                break
                
            elif destination in ["Jodhpur","jodhpur","JODHPUR"]:
                company_name=["Gajaraj Travels","Bhagwati Tours & Travels","Jain Travels regd","Jakhar Travels & Cargo","Chanakya Travels Agency"]
                bus_type=["AC Sleeper","AC Seater","AC Seater","Non-AC Seater","AC Sleeper"]
                price=[900,380,450,350,400]
                timing=["05:27 AM - 09:23 AM","09.00 PM - 12:30 AM","01:00 AM - 05:00 AM","10:30 PM - 02:30 AM","05:30 AM - 09:40 AM"]
                duration=["03h 56m","03h 30m","04h 00m","04h 00m","04h 10m"]
                self.bus={"Company Name":company_name,"Bus Type":bus_type,"Price":price,"Duration":duration,"Timing":timing}
                df=pd.DataFrame(self.bus)
                df.index=df.index+1
                print("\n\n\t\t\t\t---Buses Information Chart---\n")
                print("Ajmer -- to -- Jodhpur\n")
                print(df.to_string(index=True))
                self.drop_point="Basni Mandi Mode Pali Road"
                break
                
            elif destination in ["KOTA","Kota","kota"]:
                company_name=["Rathore Travels Madho","Jakhar Travels","M R Travels","Milan Travels","Laxmi Travellers"]
                bus_type=["Non-AC Seater","Non-AC Sleeper","Non-AC Seater","AC Seater","AC Sleeper"]
                price=[300,450,550,380,650]
                timing=["11:55 PM - 05:00 AM","11.00 PM - 05:15 AM","11:40 PM - 03:40 AM","11:50 PM - 05:40 AM","02:30 AM - 06:35 AM"]
                duration=["05h 05m","06h 15m","04h 00m","05h 50m","04h 05m"]
                self.bus={"Company Name":company_name,"Bus Type":bus_type,"Price":price,"Duration":duration,"Timing":timing}
                df=pd.DataFrame(self.bus)
                df.index=df.index+1
                print("\n\n\t\t\t\t---Buses Information Chart---\n")
                print("Ajmer -- to --Kota\n")
                print(df.to_string(index=True))
                self.drop_point="Swami Vivekanda Chauraha"
                break

            elif destination in ["DELHI","Delhi","delhi"]:
                company_name=["RR Travels Radha Raman","Bluecity Bus","Ashok Travels","Shree Rishabh Travels","M R Travels"]
                bus_type=["AC Seater","AC Sleeper","Non-AC Seater","Non-AC Sleeper","AC Sleeper"]
                price=[1300,950,389,752,950]
                timing=["11:35 PM - 06:50 AM","11.55 PM - 07:50 AM","08:15 PM - 06:30 AM","11:25 PM - 06:30 AM","11:50 PM - 07:00 AM"]
                duration=["07h 15m","07h 55m","10h 15m","07h 05m","07h 10m"]
                self.bus={"Company Name":company_name,"Bus Type":bus_type,"Price":price,"Duration":duration,"Timing":timing}
                df=pd.DataFrame(self.bus)
                df.index=df.index+1
                print("\n\n\t\t\t\t---Buses Information Chart---\n")
                print("Ajmer -- to -- Delhi\n")
                print(df.to_string(index=True))
                self.drop_point="Dhaula kuan Bus Stand"
                break

            else:
                print("Invalid Destination Name! Please re-enter.....\n")
        
        self.pass_details()
        self.payment_page()
        self.ticket()
        
    def Kota(self):
        
        while True:
            dest_list=["Jaipur","Alwar","Jodhpur","Bharatpur","Ajmer","Delhi"]
            self.pickuppoint_list=["AlhaUdal Park Keshavpura Kota","Chawani Choraha Kota"]
            print("\nDestination Cities:\n",dest_list)

            destination=input("Enter the destination city name:")
        
            if destination in ["Jaipur","jaipur","JAIPUR"]:
                company_name=["Mahalaxmi Travels","Babu Travels","Navrang Travels","Babu Travels","Jakhar Travels","Vijay Travels"]
                bus_type=["AC Seater","AC Sleeper","AC Sleeper","Non-AC Seater","Non-AC Sleeper","AC Sleeper"]
                price=[333,650,500,300,500,1299]
                timing=["05:00 PM - 10:15 PM","04.00 PM - 08:40 PM","11:00 PM - 04:30 AM","11:00 PM - 05:00 AM","11:30 PM - 05:00 AM","06:00 PM - 10:40 PM"]
                duration=["05h 15m","04h 40m","05h 30m","06h 00m","05h 30m","04h 40m"]
                self.bus={"Company Name":company_name,"Bus Type":bus_type,"Price":price,"Duration":duration,"Timing":timing}
                df=pd.DataFrame(self.bus)
                df.index=df.index+1
                print("\n\n\t\t\t\t---Buses Information Chart---\n")
                print("Kota -- to -- Jaipur\n")
                print(df.to_string(index=True))
        #       break
                self.drop_point="Sindhi Camp Bus Stand"
                break

            elif destination in ["Alwar","alwar","ALWAR"]:
                company_name=["Babu Travels","Babu Travels","B R Travels","Gajraj Travels","Gajraj Travels"]
                bus_type=["AC Sleeper","AC Sleeper","AC Sleeper","AC Sleeper","AC Sleeper"]
                price=[999,1500,1100,1400,1400]
                timing=["11:40 PM - 06:30 AM","11.55 PM - 07:35 AM","01:15 AM - 07:00 AM","01:10 AM - 06:00 AM","11:30 PM - 04:30 AM"]
                duration=["06h 50m","07h 40m","05h 45m","04h 50m","05h 00m"]
                self.bus={"Company Name":company_name,"Bus Type":bus_type,"Price":price,"Duration":duration,"Timing":timing}
                df=pd.DataFrame(self.bus)
                df.index=df.index+1
                print("\n\n\t\t\t\t---Buses Information Chart---\n")
                print("Kota -- to -- Alwar\n")
                print(df.to_string(index=True))
                self.drop_point="Delhi Mumbai Express Highway, Alwar"
                break
                
            elif destination in ["BHARATPUR","Bharatpur","bharatpur"]:
                company_name=["Yadav Vishvakarma Travels","Yadav Vishvakarma Travels","Ganesh Travels","Ganesh Travels"]
                bus_type=["AC Seater","AC Sleeper","AC Seater","AC Sleeper"]
                price=[400,600,500,700]
                timing=["06:30 PM - 03:00 AM","06:30 PM - 03:00 AM","06:30 PM - 02:30 AM","06:30 PM - 02:30 AM"]
                duration=["08h 30m","08h 30m","08h 00m","08h 00m"]
                self.bus={"Company Name":company_name,"Bus Type":bus_type,"Price":price,"Duration":duration,"Timing":timing}
                df=pd.DataFrame(self.bus)
                df.index=df.index+1
                print("\n\n\t\t\t\t---Buses Information Chart---\n")
                print("Kota -- to -- Bharatpur\n")
                print(df.to_string(index=True))
                self.drop_point="Baypass bharatpur"
                break
                
            elif destination in ["AJMER","Ajmer","ajmer"]:
                company_name=["Rathore Travels Madho","Ganesh Travels","M R Travels","Jakhar Travels","Nama Travels"]
                bus_type=["Non-AC Sleeper","Non-AC Seater","AC Sleeper","Non-AC Sleeper","Non-AC Seater"]
                price=[650,300,825,550,300]
                timing=["11:30 PM - 06:45 AM","04.30 AM - 10:15 AM","06:00 AM - 10:30 AM","09:45 PM - 10:15 AM","08:05 PM - 01:00 AM"]
                duration=["05h 15m","05h 45m","04h 30m","05h 10m","04h 55m"]
                self.bus={"Company Name":company_name,"Bus Type":bus_type,"Price":price,"Duration":duration,"Timing":timing}
                df=pd.DataFrame(self.bus)
                df.index=df.index+1
                print("\n\n\t\t\t\t---Buses Information Chart---\n")
                print("Kota -- to -- Ajmer\n")
                print(df.to_string(index=True))
                self.drop_point="Parbatpura Bypass, Ajmer"
                break
                
            elif destination in ["Jodhpur","jodhpur","JODHPUR"]:
                company_name=["Gajraj Travels","Jain Travels regd","M R Travels","Babu Travels","Jakhar Travels"]
                bus_type=["AC Sleeper","Non-AC Sleeper","AC Sleeper","Non-AC Seater","AC Seater"]
                price=[700,600,665,450,686]
                timing=["10:15 PM - 06:30 AM","09.30 PM - 06:20 AM","10:00 PM - 06:15 AM","09:45 PM - 07:20 AM","06:45 PM - 03:00 AM"]
                duration=["08h 15m","08h 50m","08h 15m","09h 35m","08h 15m"]
                self.bus={"Company Name":company_name,"Bus Type":bus_type,"Price":price,"Duration":duration,"Timing":timing}
                df=pd.DataFrame(self.bus)
                df.index=df.index+1
                print("\n\n\t\t\t\t---Buses Information Chart---\n")
                print("Kota -- to -- Jodhpur\n")
                print(df.to_string(index=True))
                self.drop_point="Basni Mandi Mode Pali Road"
                break

            elif destination in ["DELHI","Delhi","delhi"]:
                company_name=["Gajraj Travels","Babu Travels","Samreen Travels","Navrang Travels","B R Travels"]
                bus_type=["AC Sleeper","AC Sleeper","AC Sleeper","AC Seater","AC Sleeper"]
                price=[1400,900,850,600,1100]
                timing=["11:30 PM - 08:15 AM","09:30 PM - 05:55 AM","09:30 PM - 06:00 AM","08:30 PM - 06:00 AM","01:15 AM - 09:45 AM"]
                duration=["08h 45m","08h 25m","08h 30m","09h 30m","08h 30m"]
                self.bus={"Company Name":company_name,"Bus Type":bus_type,"Price":price,"Duration":duration,"Timing":timing}
                df=pd.DataFrame(self.bus)
                df.index=df.index+1
                print("\n\n\t\t\t\t---Buses Information Chart---\n")
                print("Kota -- to -- Delhi\n")
                print(df.to_string(index=True))
                self.drop_point="Dhaula kuan Bus Stand"
                break

            else:
                print("Invalid Destination Name! Please re-enter.....\n")
        
        self.pass_details()
        self.payment_page()
        self.ticket()
    
    def Delhi(self):
        
        while True:
            dest_list=["Jaipur","Alwar","Jodhpur","Bharatpur","Ajmer","Kota"]
            self.pickuppoint_list=["Karol Bagh Bus Stop","Dhaula Kuan Bus Stop"]
            print("\nDestination Cities:\n",dest_list)

            destination=input("Enter the destination city name:")

            if destination in ["Jaipur","jaipur","JAIPUR"]:
                company_name=["RR Travels RADHA RAMAN","NueGo","Vikas Travels","Gajraj Travels","Rahi Travells"]
                bus_type=["AC Sleeper","AC Seater","AC Sleeper","AC Sleeper","AC Seater"]
                price=[2200,511,474,1500,900]
                timing=["04:55 PM - 11:25 PM","07.30 AM - 12:05 PM","11:59 PM - 05:40 AM","09:00 PM - 02:15 AM","11:30 PM - 05:00 AM"]
                duration=["06h 30m","04h 35m","05h 41m","05h 15m","05h 30m"]
                self.bus={"Company Name":company_name,"Bus Type":bus_type,"Price":price,"Duration":duration,"Timing":timing}
                df=pd.DataFrame(self.bus)
                df.index=df.index+1
                print("\n\n\t\t\t\t---Buses Information Chart---\n")
                print("Delhi -- to -- Jaipur\n")
                print(df.to_string(index=True))
        #       break
                self.drop_point="Sindhi Camp Bus Stand"
                break

            elif destination in ["Alwar","alwar","ALWAR"]:
                company_name=["Deepak Travels","P.G Travels","Parmar Travels","M R Travels","B R Travels"]
                bus_type=["Non-AC Seater","Non-AC Sleeper","Non-AC Seater","AC Sleeper","AC Sleeper"]
                price=[379,1044,399,1000,999]
                timing=["06:00 PM - 08:00 PM","07.30 PM - 12:05 AM","09:30 PM - 01:45 AM","09:00 PM - 11:30 PM","07:15 PM - 10:25 PM"]
                duration=["02h 00m","04h 35m","04h 15m","02h 30m","03h 10m"]
                self.bus={"Company Name":company_name,"Bus Type":bus_type,"Price":price,"Duration":duration,"Timing":timing}
                df=pd.DataFrame(self.bus)
                df.index=df.index+1
                print("\n\n\t\t\t\t---Buses Information Chart---\n")
                print("Delhi -- to -- Alwar\n")
                print(df.to_string(index=True))
                self.drop_point="Delhi Mumbai Express Highway, Alwar"
                break
                
            elif destination in ["BHARATPUR","Bharatpur","bharatpur"]:
                company_name=["Yadav Vishvakarma Travels","Yadav Vishvakarma Travels"]
                bus_type=["Non-AC Seater","Non-AC Sleeper"]
                price=[479,579]
                timing=["10:30 PM - 02:56 AM","10:30 PM - 02:56 AM"]
                duration=["04h 26m","04h 26m"]
                self.bus={"Company Name":company_name,"Bus Type":bus_type,"Price":price,"Duration":duration,"Timing":timing}
                df=pd.DataFrame(self.bus)
                df.index=df.index+1
                print("\n\n\t\t\t\t---Buses Information Chart---\n")
                print("Delhi -- to -- Bharatpur\n")
                print(df.to_string(index=True))
                self.drop_point="Baypass bharatpur"
                break
                
            elif destination in ["AJMER","Ajmer","ajmer"]:
                company_name=["Jakhar Travels","RR Travels RADHA RAMAN","Bluecity Bus","Gajraj Travels","Jain Travels regd"]
                bus_type=["AC Seater","AC Sleeper","AC Sleeper","AC Sleeper","Non-AC Sleeper"]
                price=[1000,2200,950,900,900]
                timing=["08:30 PM - 05:00 AM","04.55 PM - 01:19 AM","09:30 PM - 04:45 PM","09:00 PM - 05:27 AM","08:00 PM - 03:51 AM"]
                duration=["08h 30m","08h 24m","07h 15m","08h 27m","07h 51m"]
                self.bus={"Company Name":company_name,"Bus Type":bus_type,"Price":price,"Duration":duration,"Timing":timing}
                df=pd.DataFrame(self.bus)
                df.index=df.index+1
                print("\n\n\t\t\t\t---Buses Information Chart---\n")
                print("Delhi -- to -- Ajmer\n")
                print(df.to_string(index=True))
                self.drop_point="Parbatpura Bypass, Ajmer"
                break
                
            elif destination in ["KOTA","Kota","kota"]:
                company_name=["Gajraj Travels","Babu Travels","Samreen Travels","Navrang Travels","Jakhar Travels"]
                bus_type=["AC Sleeper","AC Sleeper","AC Sleeper","AC Seater","AC Sleeper"]
                price=[1800,850,1000,600,848]
                timing=["06:00 PM - 02:50 AM","09.10 PM - 06:10 AM","11:00 PM - 09:00 AM","08:00 PM - 05:30 AM","09:15 PM - 05:50 AM"]
                duration=["08h 50m","08h 40m","10h 00m","09h 30m","08h 45m"]
                self.bus={"Company Name":company_name,"Bus Type":bus_type,"Price":price,"Duration":duration,"Timing":timing}
                df=pd.DataFrame(self.bus)
                df.index=df.index+1
                print("\n\n\t\t\t\t---Buses Information Chart---\n")
                print("Delhi -- to -- Kota\n")
                print(df.to_string(index=True))
                self.drop_point="Swami Vivekanda Chauraha"
                break

            elif destination in ["Jodhpur","jodhpur","JODHPUR"]:
                company_name=["Jakhar Travels","Bluecity Bus","M R Travels","Vishwakarma Nirman Travels","Jain Travels regd"]
                bus_type=["AC Seater","AC Sleeper","AC Sleeper","Non-AC Sleeper","AC Sleeper"]
                price=[1000,999,1000,900,1200]
                timing=["08:30 PM - 08:30 AM","09:30 PM - 08:30 AM","09:00 PM - 09:00 AM","07:15 PM - 06:45 AM","09:15 PM - 09:03 AM"]
                duration=["12h 00m","11h 00m","12h 00m","11h 30m","11h 48m"]
                self.bus={"Company Name":company_name,"Bus Type":bus_type,"Price":price,"Duration":duration,"Timing":timing}
                df=pd.DataFrame(self.bus)
                df.index=df.index+1
                print("\n\n\t\t\t\t---Buses Information Chart---\n")
                print("Delhi -- to -- Jodhpur\n")
                print(df.to_string(index=True))
                self.drop_point="Basni Mandi Mode Pali Road"
                break

            else:
                print("Invalid Destination Name! Please re-enter.....\n")
        
        self.pass_details()
        self.payment_page()
        self.ticket()
        
        
        
    def pass_details(self):
        while True:
            self.p=int(input("\n\nEnter the no. of selected company :"))
            self.pass_no=int(input("Enter the no. of passengers:"))
            print("Pick-up Point List:\n",self.pickuppoint_list)
            self.pickup_point=input("Enter the name of pickup point:")
            self.random_number = random.randint(1, 10000)
            for k in range(self.pass_no):
                self.rand_no=self.random_number
                name=input("\nEnter the passenger "+str(k+1)+" name:")
                self.name.append(name)
                mobileno=int(input("Enter the passenger "+str(k+1)+" mobile no.:"))
                self.mn.append(mobileno)
                age=int(input("Enter the passenger "+str(k+1)+" age:"))
                self.age.append(age)
                self.random_no.append(self.rand_no)
                self.random_number+=1
            break
            
    def payment_page(self):
        print(Fore.RED+Style.BRIGHT)
        print("Taking you to the payment page:")
        print(Fore.BLUE+Style.BRIGHT)
        self.amount=self.bus["Price"][self.p-1]
        total=self.amount*self.pass_no
        self.d.append(total)

        t=sum(self.d)
        m=(sum(self.d)*0.05)
        self.amount=t+m
        print("Total Amount:",t,"Rs.")
        print("service tax= 5%")
        print("Total Amount Including Service Tax:",self.amount,"Rs.")

        print("\n")

        while True:
            payment_option=input("Select Payment Option - Paytm, Phone Pe, Google Pay:")
            if payment_option in ["PAYTM","Paytm","paytm"]:
                url="https://paytm.com/"
                img="Paytm.png"
                self.qr_code(url,img)
                break

            elif payment_option in ["PHONE PE","Phone Pe","phone pe"]:
                url="https://www.phonepe.com/"
                img="Phone Pe.png"
                self.qr_code(url,img)
                break

            elif payment_option in ["Google Pay","GOOGLE PAY","google pay"]:
                url="https://pay.google.com/about/"
                img="Google Pay.png"
                self.qr_code(url,img)
                break

            else:
                print("Invalid Payment Option! Please Re-enter carefully\n")
    
    def ticket(self):
        
        for k in range(self.pass_no):
            print("\n\n----------------------------------------------------Bus Ticket---------------------------------------------------------\n")
            print("Ticket ID:",self.random_no[k],"\t\t\tCompany Name:",self.bus["Company Name"][self.p-1],"\t\t\tTiming:",self.bus["Timing"][self.p-1])
            print("Passenger Name:",self.name[k],"            Bus Type:",self.bus["Bus Type"][self.p-1],"\t\t\t\tDuration:",self.bus["Duration"][self.p-1])
            print("Age:",self.age[k],"\t\t\t\tTotal Amount:",self.amount/self.pass_no,"\t\t\t\t Date:",self.date)
            print("\nPickup-point:",self.pickup_point,"\t\t\t\t\t\tDrop Point:",self.drop_point)
            print("\n\t\t\t\t\t         Happy Journey🙏🙏")
            print("---------------------------------------------------------------------------------------------------------------------------\n\n")


# In[10]:


obj=JaipurTravelService()


# In[ ]:




