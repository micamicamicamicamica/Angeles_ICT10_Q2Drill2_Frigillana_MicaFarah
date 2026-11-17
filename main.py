from pyscript import document


grade_7 = {"Fabio Wood", "Aizal Harrell", "Angelo Blackburn"}
grade_8 = {"Amelia Gray", "Eva Bird", "Issac Slater"}
grade_9 = {"Lance Moran", "Laila Woods", "Reuben Carson"}
grade_10 = {"Lia Marks", "Clark Waters", "Keenan Neal"}

current = grade_7.union(grade_8, grade_9, grade_10)

def get_full_name():
    first_name = document.getElementById("firstname").value.strip()
    last_name = document.getElementById("surname").value.strip()
    return f"{first_name} {last_name}"

def show_result(event):
    result = document.getElementById("message")
    new_name = get_full_name()
    current.add(new_name)
    total = len(current)
    result.innerText = f"Member Names: {current} Total Number of Members: {total}"