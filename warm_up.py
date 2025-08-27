data = [
    {
        "name": "Chinedu",
        "age": 32,
        "skills": ["Python", "Django", "PostgreSQL"],
        "projects": [
            {"title": "School Management System", "year": 2022},
            {"title": "E-Payment Platform", "year": 2024},
        ]
    },
    {
        "name": "Aisha",
        "age": 28,
        "skills": ["JavaScript", "React", "Node.js"],
        "projects": [
            {"title": "Online Learning Portal", "year": 2023},
            {"title": "Real-time Notification App", "year": 2024},
        ]
    },
    {
        "name": "Tobi",
        "age": 25,
        "skills": ["HTML", "CSS", "TailwindCSS"],
        "projects": [
            {"title": "Portfolio Website", "year": 2022},
            {"title": "Business Landing Page", "year": 2023},
        ]
    },
    {
        "name": "Kunle",
        "age": 30,
        "skills": ["PHP", "Laravel", "MySQL"],
        "projects": [
            {"title": "Property Listing Platform", "year": 2023},
            {"title": "Multi-vendor Marketplace", "year": 2024},
        ]
    },
    {
        "name": "Ngozi",
        "age": 29,
        "skills": ["Java", "Spring Boot", "Docker"],
        "projects": [
            {"title": "Banking API", "year": 2022},
            {"title": "Fleet Management System", "year": 2023},
        ]
    },
    [
        {
            "category": "Books",
            "items": ["Clean Code", "The Pragmatic Programmer"]
        },
        {
            "category": "Courses",
            "items": ["CS50", "Django for Beginners"]
        }
    ]
]



employee = data[0]
print(f' {employee["name"]},\t\t {employee["age"]},\t\t {" ".join(employee["skills"])},\t\t {employee["projects"]}')
employee = data[1]
print(f' {employee["name"]},\t\t {employee["age"]},\t\t {" ".join(employee["skills"])},\t\t {employee["projects"]}')
employee = data[2]
print(f' {employee["name"]},\t\t {employee["age"]},\t\t {" ".join(employee["skills"])},\t\t {employee["projects"]}')
employee = data[3]
print(f' {employee["name"]},\t\t {employee["age"]},\t\t {" ".join(employee["skills"])},\t\t {employee["projects"]}')
employee = data[4]
print(f' {employee["name"]},\t\t {employee["age"]},\t\t {" ".join(employee["skills"])},\t\t {employee["projects"]}')



