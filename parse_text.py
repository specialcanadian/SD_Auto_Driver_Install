a_string = "A string is more than its parts!"
matches = ["ore", "wholesome", "milk"]

#if any(x in a_string for x in matches):
    

TF = any(x in a_string for x in matches)
print(TF)