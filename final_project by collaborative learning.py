                          #PROJECT-FILE


#final project by COLLABORATIVE LEARNING
#PROJECT NAME:checking my favourite house before buying it and prining the details after the complete selection of house requirements .

#VARIOUS REQUIRED LISTS AND DICTIONARIES

Area_list=["madhura nagar","sudharao colony","nehru colony","syndicate colony","whirpool colony"]
Budget_list=[2500000,5200000,8500000,1000000]
Sq_ft_list=['200x400','600x800','1000x1200','1400x1600','1500x500','1900x1000' , '2000x1500','3000x2000']
Direction_list=["EAST","WEST","NORTH","SOUTH"]
dictionary_rooms={'1':'2-bed_rooms,2-bath_rooms,1-kitchen_room,1-store_room,1-normal_room','2':'3-bed_rooms,2-bath_room,1-store_room,1-kitchen_room','3':'1-bed_room,1-bath_room,1-store_room,2-kitchen_room'}

#AREA FUNCTION TO SHOW WHICH AREA WAS SELECTED

def area(colony):
    print("hi welcome to: ",colony)
    print("-----------------------------------------")
    print("This is the area section in your selected colony")

    if(colony==Area_list[0]or colony==Area_list[1] or colony==Area_list[2] or colony==Area_list[3] or colony==Area_list[4]):

       Sq_ft()

#SELECT_NO_OF_ROOMS TYPE FUNCTION WHICH SHOWS ACCORDING TO SQ_FT

def select_no_of_rooms(Sq_ft):
    print("/n")
    print("----------------------------------------------")
    print("SELECT_NO_OF_ROOMS")
    print("----------------------------------------------")
    print("No.of room designs available for your Sq_ft: ",Sq_ft)
    print('''1.2-bed_rooms,2-bath_rooms,1-kitchen_room,1-store_room,1-normal_room,
2.3-bed_rooms,2-bath_room,1-store_room,1-kitchen_room
3.11-bed_room,1-bath_room,1-store_room,2-kitchen_room''')
    print("select any one option from 1,2,3")
    print("----------------------------------------------")
    
    select_no_of_rooms.dic=input("Enter option: ")

    if (select_no_of_rooms.dic in dictionary_rooms):
         return  select_no_of_rooms.dic
    else:
         print("THE SELECTED ROOMS ARE NOT THERE EVEN IF YOU ENTERED WRONG NUMBER THE SUMMARY WILL BE GIVEN BUT IT'S NOT ACCEPTED")

#THIS IS DIRECTION FUNCTION INVOKED BY SQ_FT
#DIRECTION FUNCTION TO SHOW YOUR RESPECTIVE CHOOSEN DIRECTION AND THE SENDING  THIS TO SELECTION_OF_NO_OF_ROOMS:

def Direction(sq_ft):
    print("\n----------------------------------------------")
    print("SELECT HOUSE FACING")
    print("-------------------------------------------------")
    print("choose your facing from directions list: ")
    print(Direction_list)
    print("--------------------------------------------------")
    Direction.Directn=input("Enter your fav facing: ")

    if (Direction.Directn in Direction_list):
        select_no_of_rooms(Sq_ft)
    else:
        print("THE SELECTED DIRECTION IS NOT IN THE LIST")

    
#SQ_FT FUNCTION INVOKED AFTER SELECTING COLONY AREA

def Sq_ft():
    
    print("\n--------------------------------------------------")
    print("SELECT SQUARE FEET")
    print("----------------------------------------------------")
    print(Sq_ft_list)
    print("----------------------------------------------------")
    Sq_ft.Sq_ft=input("Enter square feet: ")
    if (Sq_ft.Sq_ft in Sq_ft_list):
          Direction(Sq_ft)
    else:
          print("CHOOSE SQUARE FEET IS NOT IN OUR LIST")


#START OF HOUSING PLAN PROJECT

c="Welcome to new housing colony.\n we're so glad to meet you."
print(c)
print("""
--------------------------------------------------------------------
____________________________________________________________________

Below are the areas that we'reoffering to you select you residency.

-> madhura nagar
-> sudharao colony
-> syndicate colony
-> whirpool colony

Enter any of your interested colony name to move forward else press 1 (or) 0 to exit from process. """)
print("\n")
print("--------------------------------------------------------------")
print("SELECT AREA")
print("---------------------------------------------------------------")

colony=input("Enter area: ")

#CHECKING OF THE COLONY NAME IN LIST AND THE PROCEDING WITH PROCEDURE  FURTHER:

print("\n")
print("---------------------------------------------------------------")
if (colony in Area_list):
     print("SELECT BUDGET")
     print("-----------------------------------------------------------")
     print("Here are budgets list for buying a house and the same budget follows for all colony areas :")
     print(Budget_list)
     print("-----------------------------------------------------------")
     Budget=int(input("Enter your budget: "))
     if (Budget in Budget_list):
         area(colony)
     else:
         print("THE ENTERED BUDGET DOESN'T MATCH OOPS!!")



  #SUMMARY OF THE SELECTED HOUSING PLAN 
     print("\n\n-------------------------------------------")
     print("THE SUMMARY OF YOUR HOUSE PLAN:")
     print("-----------------------------------------------")
     print("YOUR COLONY:",colony)
     print("YOUR BUDGET:",Budget)
     print("YOUR SQUARE FEET:",Sq_ft.Sq_ft)
     print("YOUR FAV FACING:",Direction.Directn)

     if (select_no_of_rooms.dic in dictionary_rooms):
           print("YOUR SELECTED ROOM TYPE :",select_no_of_rooms.dic)
     else:       
           print("YOUR SUMMARY NOT ACCEPTED BECAUSE THE NO.OF ROOMS TYPE YOU CHOSENIS INVALID")
     print("--------------------------------------------------------")
     print("-----------THANK YOU FOR BOOKING YOUR SLOT IN OUR HOUSING COLONY------")
elif(colony=='1' or colony=='0'):  
     print("sorry if any mistakes from our side and your cancellation of process is successfull")
else:
     print("THE WRITTEN COLONY IS NOT THERE IN OUR LIST")
    
        

    

    
