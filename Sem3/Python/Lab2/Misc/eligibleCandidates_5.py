def FindEligibleCandidates(name,math, phy, chem):
    total_in_all_3_sub = math+phy+chem
    total_in_math_and_phy = math+phy

    if(total_in_all_3_sub >= 200 or total_in_math_and_phy >= 150):
        if(math >= 60 and phy>= 50 and chem >= 40):
            print(f"Yes, {name} is Eligible!\n") 
        else:
            print(f"Oh! {name} is not Eligible! To be eligible number should be : Math >= 60 | Physics >= 50 | Chemistry >= 40\n")
    else:
        print(f"No, {name} is not Eligible!\nTotal number in all 3 subjects should be >= 200 or Total number is Math and Physics should be >= 150.\n")



name = input("Please enter the name of the candidate : ")
math = float(input("Score in Math ? : "))
physics = float(input("Score in Physics ? : "))
chemistry = float(input("Score in Chemistry ? : "))

FindEligibleCandidates(name, math, physics, chemistry)