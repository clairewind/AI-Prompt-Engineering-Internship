import random
x = random.randint(0,4)
print("\n" "Your stir fry ingredients: " "\n")
#Proteins
proteinAnswer = ""

proteinLst = ["Beef", "Chicken", "Pork", "Tofu", "Tempeh"]

if x == 0:
    proteinAnswer = proteinLst[0]
if x == 1:
    proteinAnswer = proteinLst[1]
if x == 2:
    proteinAnswer = proteinLst[2]
if x == 3:
    proteinAnswer = proteinLst[3]
if x == 4:
    proteinAnswer = proteinLst[4]
    
print("Protein: " + str(proteinAnswer))
#Vegetable 1
y = random.randint(0,13)
veg1Answer = ""
veg1Lst = ["Green Beans", "Broccolini", "Broccoli", "Carrots", "Cauliflower", "Eggplant", "Oyster Mushrooms", "Wood Ear Mushrooms", "Lion's Mane Mushrooms", "Snow Peas", "Romanesco", "Gai Lan", "Parsnips", "Cabbage"]
if y == 0:
    veg1Answer = veg1Lst[0]
if y == 1:
    veg1Answer = veg1Lst[1]
if y == 2:
    veg1Answer = veg1Lst[2]
if y == 3:
    veg1Answer = veg1Lst[3]
if y == 4:
    veg1Answer = veg1Lst[4]
if y == 5:
    veg1Answer = veg1Lst[5]
if y == 6:
    veg1Answer = veg1Lst[6]
if y == 7:
    veg1Answer = veg1Lst[7]
if y == 8:
    veg1Answer = veg1Lst[8]
if y == 9:
    veg1Answer = veg1Lst[9]
if y == 10:
    veg1Answer = veg1Lst[10]
if y == 11:
    veg1Answer = veg1Lst[11]
if y == 12:
    veg1Answer = veg1Lst[12]
if y == 13:
    veg1Answer = veg1Lst[13]

print("Vegetable 1: " + str(veg1Answer))


#Vegetable 2

z = random.randint(0,13)

veg2Answer = ""


if z == 0:
    veg2Answer = veg1Lst[0]
if z == 1:
    veg2Answer = veg1Lst[1]
if z == 2:
    veg2Answer = veg1Lst[2]
if z == 3:
    veg2Answer = veg1Lst[3]
if z == 4:
    veg2Answer = veg1Lst[4]
if z == 5:
    veg2Answer = veg1Lst[5]
if z == 6:
    veg2Answer = veg1Lst[6]
if z == 7:
    veg2Answer = veg1Lst[7]
if z == 8:
    veg2Answer = veg1Lst[8]
if z == 9:
    veg2Answer = veg1Lst[9]
if z == 10:
    veg2Answer = veg1Lst[10]
if z == 11:
    veg2Answer = veg1Lst[11]
if z == 12:
    veg2Answer = veg1Lst[12]
if z == 13:
    veg2Answer = veg1Lst[13]
    
if veg1Answer == veg2Answer:
    veg2Answer = "Bell Pepper"

print("Vegetable 2: " + str(veg2Answer))


    

#Aromatics

a = random.randint(0,4)

aromAnswer = ""

aromLst = ["Garlic, Ginger, Scallions", "Garlic, Thai Chili, Ginger", "Galangal, Garlic, Chili, Lemongrass", "Shallots, Chinese Chives", "Garlic, Black Garlic, Ginger"]

if a == 0:
    aromAnswer = aromLst[0]
if a == 1:
    aromAnswer = aromLst[1]
if a == 2:
    aromAnswer = aromLst[2]
if a == 3:
    aromAnswer = aromLst[3]
if a == 4:
    aromAnswer = aromLst[4]
    
print("Aromatics: " + str(aromAnswer))

#Other Ingredients

b = random.randint(0,7)

othrAnswer = ""

othrLst = ["Szechuan Pickled Chili Paste", "Ssamjang", "Doenjang", "Szechuan Chili and Szechuan Pepper", "Doubanjiang", "Belacan and Tomato Paste", "Red Miso", "White Miso"]

if b == 0:
    othrAnswer = othrLst[0]
if b == 1:
    othrAnswer = othrLst[1]
if b == 2:
    othrAnswer = othrLst[2]
if b == 3:
    othrAnswer = othrLst[3]
if b == 4:
    othrAnswer = othrLst[4]
if b == 5:
    othrAnswer = othrLst[5]
if b == 6:
    othrAnswer = othrLst[6]
if b == 7:
    othrAnswer = othrLst[7]

print("Other Ingredients: " + str(othrAnswer))

#Sauce

c = random.randint(0,3)

sauceAnswer = ""

sauceLst = ["Oyster Sauce, Fish Sauce, Equal parts Dark and Light Soy Sauce", "Fish Sauce, Light Soy Sauce, White Pepper", "Broth and Light Soy Sauce", "Dark Soy Sauce, Oyster Sauce, Chili Crisp"]

if c == 0:
    sauceAnswer = sauceLst[0]
if c == 1:
    sauceAnswer = sauceLst[1]
if c == 2:
    sauceAnswer = sauceLst[2]
if c == 3:
    sauceAnswer = sauceLst[3]
    
print("Sauce: " + str(sauceAnswer))


#Recipe

print("\n" + "RECIPE:" "\n", "-Begin by marinating your protein in soy sauce and white pepper. Prepare a corn starch slurry with 3 tbsp of cool water and 1 tbsp of corn starch. \n -Fill wok with water and bring to a boil, adding a bit of salt and oil to the water. \n -Quickly blanch " + str(veg1Answer.lower()) + " and " + str(veg2Answer.lower()) + ", " + "to 'break the rawness'. Add harder and denser vegetables first, and softer vegetables last. When vegetables are tendercrisp but not fully cooked, drain them into a colander." "\n" + "-Empty and dry the wok then bring it to temperature over high heat. Add about 2 tbsp of a high-heat oil such as avocado or peanut oil, and swirl around in the wok. \n -Sear off the protein until it is almost cooked through, or cooked to your liking. Remove the protein and set aside. \n -When oil is hot, add " + str(othrAnswer.lower()) + " to oil and mix until oil is fragrant and smells of the ingredients. About 8-10 seconds. \n -Add " + str(aromAnswer.lower()) + " and stir until you can smell them in the air. \n -Add the vegetables and stir fry for about 10 seconds, then add protein and stir fry for another 10-15 seconds. \n -Add sauce along the outer part of the wok and toss the ingredients to coat. Add desired amount of corn starch slurry to thicken sauce. \n -Toss lightly and serve immediately with steamed rice." )