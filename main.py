from pyscript import document, display

campusINDEX = "fairview"
gsectionINDEX = "10-Emerald"
hobbies = "guitar"
band = "Irrevocable"

display(f"Campus: {campusINDEX}", target="campusINDEX")
display(f"Section: {gsectionINDEX}", target="gsectionINDEX")
display(f"Hobbies: {hobbies}", target="hobbies")
display(f"Favorite Band: {band}", target="band")


# SEATWORK 1 CODE START
# list of members that got in (case sensitive upon testing)
club_membersSW1 = ["John Numbers", "Ben Franklin", "John Mark San Pedro Santos"]

def check_candidate(e):
    document.getElementById("output1SW1").innerHTML = ""
    
    # combine first and last name
    first_nameSW1 = document.getElementById("input1SW1").value.strip()
    last_nameSW1 = document.getElementById("input2SW1").value.strip()
    full_nameSW1 = f"{first_nameSW1} {last_nameSW1}"
    
    # check if name is in the list of members that got in
    is_memberSW1 = full_nameSW1 in club_membersSW1
    
    # choose message based on result from checking the list of members that got in
    messagesSW1 = [
        f"Sorry {full_nameSW1}, your name is not on the list.",
        f"Congratulations {full_nameSW1}! You are now part of the ICT club."
    ]
    
    result_messageSW1 = messagesSW1[is_memberSW1]
    
    # Display message
    display(result_messageSW1, target="output1SW1")

# SEATWORK 1 CODE END





# SKILLS TEST CODE START
#   Dictionary with elements and their info
elementsST1= {"F" : ("FLOURINE", 9, 18.9984),
                        # 0          1      2
           "H" : ("HYDROGEN", 1, 1.0079),
           "N" : ("NITROGEN", 7, 14.0067),
           "Xe" : ("XENON", 54, 131.293),
           "He" : ("HELIUM", 2, 4.0026),
           "Ne" : ("NEON", 10, 20.1797),
           "Ar" : ("ARGON", 18, 39.948),
           "Kr" : ("KRYPTON", 36, 83.8),
           "Rn" : ("RADON", 86, 222),
           "C" : ("CARBON", 6, 12.0107),
           "O" : ("OXYGEN", 8, 15.9994),
           "P" : ("PHOSPHORUS", 15, 30.9738),
           "S" : ("SULFUR", 16, 32.065),
           "Cl" : ("CHLORINE", 17, 35.453),
           "Se" : ("SELENIUM", 34, 78.96),
           "Br" : ("BROMINE", 35, 79.904),
           "I" : ("IODINE", 53, 126.9045),
           }
#   KEY : VALUE
    #ELEMENT    :   Element name, Atomic number, Atomic Mass

def search_element(e):
    #   Get input from HTML text input
    elementA = document.getElementById("elementA").value
    #   Retrieve info of elements from dict
    resultST1 = elementsST1.get(elementA, ("Sorry! This element is probably a metal or you didn't input the atomic symbol correctly. Please note that the input is case sensitive.", "-", "-") ) #Fallbacks included
    #   Display result in HTML

    document.getElementById("symbol").innerText = elementA #  displays element symbol
    document.getElementById("name").innerText = resultST1[0] #displays element name
    document.getElementById("number").innerText = resultST1[1] # displays element atomic number
    document.getElementById("mass").innerText = resultST1[2] # displays element atomic mass 

# SKILLS TEST CODE END



# DRILL2 CODE START
Gradeten = {"Person The Person"}
Gradenine = {"John Numbers"}
Gradeeight = {"Andres Bonifacio"}
Gradeseven = {"Et al De La Pena"}
all_membersD2 = Gradeten | Gradenine | Gradeeight | Gradeseven

members_listD2 = "<br>".join(sorted(all_membersD2))
display(members_listD2, target="listfull")
display(f"TOTAL MEMBERS: {len(all_membersD2)}", target="totalD2")


def add_member(e):
    first_nameD2 = document.getElementById("input1D2").value.strip() # gets first name input
    last_nameD2 = document.getElementById("input2D2").value.strip() # gets last name input
    document.getElementById("output1D2").innerHTML = ""

    full_nameD2 = f"{first_nameD2} {last_nameD2}" # combines first and last name inputs into one name
    all_membersD2.add(full_nameD2) # uses combined name and inputs it into list
    document.getElementById("input1D2").value = ""
    document.getElementById("input2D2").value = ""
    document.getElementById("listfull").innerHTML = "<br>".join(sorted(all_membersD2)) # A bit buggy at the start, but after adding a new member, it fixes itself.
    document.getElementById("totalD2").innerHTML = f"TOTAL MEMBERS: {len(all_membersD2)}"