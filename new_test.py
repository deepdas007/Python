#*************************************************************************************************************************
words = ["adopt", "bake", "beam", "confide", "grill", "plant", "time", "wave", "wish"]
past_tense = []
for i in words:	
    if i[-1] in 'e':
    	i = i + "d"
    	past_tense = past_tense + [i]
    else:
    	i = i + "ed"
    	past_tense = past_tense + [i]

print(past_tense)
#*************************************************************************************************************************


#*************************************************************************************************************************
rainfall_mi = "1.65, 1.46, 2.05, 3.03, 3.35, 3.46, 2.83, 3.23, 3.5, 2.52, 2.8, 1.85"
num_rainy_months = 0
x = rainfall_mi.split(",")
for i in x:
    i = float(i)
    if i > 3:
        num_rainy_months = num_rainy_months + 1
print(num_rainy_months)
#*************************************************************************************************************************


#*************************************************************************************************************************
sentence = "students flock to the arb for a variety of outdoor activities such as jogging and picnicking"

y = sentence.split(" ")
same_letter_count = 0
for i in y:
    if i[0] == i[-1]:
        same_letter_count = same_letter_count + 1
print(same_letter_count)
#*************************************************************************************************************************


#*************************************************************************************************************************
items = ["whirring", "wow!", "calendar", "wry", "glass", "", "llama","tumultuous","owing"]
acc_num = 0
for i in items:
    if "w" in i:
        acc_num = acc_num + 1
print(acc_num)
#*************************************************************************************************************************


#*************************************************************************************************************************
sentence = "python is a high level general purpose programming language that can be applied to many different classes of problems."
z = sentence.split(" ")
num_a_or_e = 0
for i in z:
    if "a" in i or "e" in i:
        num_a_or_e = num_a_or_e + 1
print(num_a_or_e)


#*************************************************************************************************************************


#*************************************************************************************************************************
s = "singing in the rain and playing in the rain are two entirely different situations but both can be fun"
vowels = ['a','e','i','o','u']

# Write your code here.
num_vowels = 0
for i in s:
    if i in vowels:
        num_vowels = num_vowels + 1
print(num_vowels)
#*************************************************************************************************************************