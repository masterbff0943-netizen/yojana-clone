# 1. The Data: Your mini database (List of Dictionaries)
schemes_db = [
    {"id": 1, "title": "PM Kisan Samman Nidhi", "occupation": "farmer", "description": "Provides ₹6,000 per year to farmer families."},
    {"id": 2, "title": "Post Matric Scholarship", "occupation": "student", "description": "Financial assistance for students pursuing higher education."},
    {"id": 3, "title": "Mudra Yojana", "occupation": "business", "description": "Loans up to ₹10 Lakhs for small enterprises."},
    {"id": 4, "title": "National Agricultural Market", "occupation": "farmer", "description": "Pan-India electronic trading portal."}
]

# 2. The Matchmaker: Python filtering function
def run_filter(user_occupation):
    print(f"\n--- Searching schemes for: {user_occupation.upper()} ---\n")
    
    # List comprehension to filter the database
    eligible_schemes = [
        scheme for scheme in schemes_db 
        if scheme["occupation"] == user_occupation or user_occupation == "all"
    ]
    
    # Display the results
    if not eligible_schemes:
        print("No schemes found for this occupation.")
    else:
        for scheme in eligible_schemes:
            print(f"Title: {scheme['title']}")
            print(f"Details: {scheme['description']}\n")

# 3. The Interface: Getting user input from the terminal
print("Welcome to My Scheme Finder!")
print("Options: farmer, student, business, all")
user_input = input("What is your occupation? ").strip().lower()

run_filter(user_input)