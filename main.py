age=int(input("Your Age: "))
birthplace = input("Were you born in the US (Yes/No):" )
residency=int(input("How many years have you lived in the US? :"))
if age >= 35 and birthplace == "Yes" and residency >= 14:
    print "You are eligible to run for president!"
elif age < 35:
    print "You are not eligible to run for president!"
    print "You are too young !"
elif birthplace == "No":
    print "You are not eligible to run for president!"
    print "You must be be born in the US to run!"
else:
    print "You are not eligible to run for president!"
    print "You must have lived in the US for at least 14 years to run!"