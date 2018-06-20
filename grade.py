def letter_grade(score):
    if (80 <= score <=90):
        return "B"
    
    if score >= 90:
        return "A"
    else:
        if 90 >= score >= 80:
            return "B"
        else: 
            if 80 >= score >= 70:
                return "C"
            else: 
                if 70 >= score >= 60:
                    return "D"
                else: 
                    return "F"
n = input("Please enter your grade:") 
print(letter_grade(n))