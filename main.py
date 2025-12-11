from pyscript import document

# Seatwork 2
def calc_gwa(e):
    first = document.getElementById('first_name').value
    last = document.getElementById('last_name').value

    def to_float(idname):
        try:
            return float(document.getElementById(idname).value)
        except:
            return 0.0

    science = to_float("g_science")
    math = to_float("g_math")
    english = to_float("g_english")
    filipino = to_float("g_filipino")
    ict = to_float("g_ict")
    pe = to_float("g_pe")

    total = science + math + english + filipino + ict + pe
    average = total / 6
    remark = "Passed" if average >= 75 else "Failed"

    document.getElementById("name_out").innerText = f"{first} {last}"
    document.getElementById("summary_out").innerText = (
        f"Science: {science}Math: {math}English: {english}"
        f"Filipino: {filipino}ICT: {ict}PE: {pe}"
    )
    document.getElementById("gwa_out").innerText = f"GWA: {average:.2f} ({remark})"


# Skills Test
dance_info = {
    'Name': 'Dance Club',
    'Description': 'Dancing, choreography, and performances.',
    'Meeting_Time': 'Wednesdays 3:30–5:00 PM',
    'Location': 'Room 405',
    'Advisor': 'Mr. Marutani',
    'Category': 'Dancing, freestyle, hip-hop'
}

glee_info = {
    'Name': 'Glee Club',
    'Description': 'Singing and performing for events.',
    'Meeting_Time': 'Mondays 4:00–5:00 PM',
    'Location': 'Room 210',
    'Advisor': 'Ms. David',
    'Category': 'Singing'
}

science_info = {
    'Name': 'Science Club',
    'Description': 'Hands-on experiments and science fairs.',
    'Meeting_Time': 'Fridays 2:30–4:00 PM',
    'Location': 'Lab 2',
    'Advisor': 'Sr. Castanio/Calpo',
    'Category': 'Academics'
}

art_info = {
    'Name': 'Art Club',
    'Description': 'Drawing, painting, and creativity workshops.',
    'Meeting_Time': 'Thursdays 3:00–4:30 PM',
    'Location': 'Art Room',
    'Advisor': 'Mr. Visaya',
    'Category': 'Arts & Creativity'
}

math_info = {
    'Name': 'Math Club',
    'Description': 'Exploring advanced math topics and competitions.',
    'Meeting_Time': 'Tuesdays 3:30–6:00 PM',
    'Location': 'Room 308',
    'Advisor': 'Mr. Ferma',
    'Category': 'Academics'
}

volleyball_info = {
    'Name': 'Varsity Volleyball Team',
    'Description': 'Competitive volleyball team representing the school.',
    'Meeting_Time': 'Mondays, Wednesdays, Fridays 4:00–6:00 PM',
    'Location': 'Quadrangel',
    'Advisor': 'Mr. Gervacio',
    'Category': 'Sports'
}

CLUBS = {
    'dance': dance_info,
    'glee': glee_info,
    'science': science_info,
    'art': art_info,
    'math': math_info,
    'volleyball': volleyball_info
}

# not sure about the club info, I might be wrong 
def show_club(e):
    sel = document.getElementById("club_select")
    key = sel.value
    club = CLUBS.get(key)
    out = document.getElementById("club_info")

# learned how to do this in a yotube video made by Krish Naik
    html = f"""
        <h5>{club['Name']}</h5>
        <p><strong>Description:</strong> {club['Description']}</p>
        <p><strong>Meeting Time:</strong> {club['Meeting_Time']}</p>
        <p><strong>Location:</strong> {club['Location']}</p>
        <p><strong>Advisor:</strong> {club['Advisor']}</p>
        <p><strong>Category:</strong> {club['Category']}</p>
    """

    out.innerHTML = html

