from pyscript import document

# predefined sets
grade7 = {"Iwannago Home", "Iaintchoslav Reyes"}
grade8 = {"Ash Trevino", "Luisito Balajadia"}
grade9 = {"Shannon Debussy", "Jojo Siwa"}
grade10 = {"Venice Sibug", "Mikaella Genove"}

# combine all sets ngani
all_members = grade7 | grade8 | grade9 | grade10

# show members on the webpage nganiiiiiiiii
def show_members():
    total = len(all_members)
    document.getElementById("output").innerHTML = f"""
        <p>All Members:{all_members}</p>
        <p>Total Members: {total}</p>
    """

# add new member when button is clicked nganiiiiiii
def add_member(e):
    first = document.getElementById("fname").value
    last = document.getElementById("lname").value
    
    # put new name in a set and add it to all_members #sirbbldat
    new_member = {f"{first} {last}".strip()} - {""}
    all_members.update(new_member)
    
    # clear inputs and update display isaganiiiiiii
    document.getElementById("fname").value = ""
    document.getElementById("lname").value = ""
    show_members()

show_members()