person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
if 'skills' in person:
    skills = person['skills']
    middle_index = len(skills) // 2
    middle_skill = skills[middle_index]
    print(f"Middle skill: {middle_skill}")
if 'skills' in person:
    has_python = 'Python' in person['skills']
    print(f"Has Python skill: {has_python}")
if 'skills' in person:
    skills = person['skills']
    if set(['JavaScript', 'React']).issubset(skills) and len(skills) == 2:
        print("He is a front end developer")
    elif set(['Node', 'Python', 'MongoDB']).issubset(skills):
        print("He is a backend developer")
    elif set(['React', 'Node', 'MongoDB']).issubset(skills):
        print("He is a fullstack developer")
    else:
        print("Unknown title")
if person['is_marred'] and person['country'] == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in Finland. He is married.")
