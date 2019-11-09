bagpack = ["food", "water", "wood", "hp+", "gun"]
da = ["DA", "Da", "da", "dA", "да", "Да", "дА", "ДА", "lf", "Lf", "LF", "lF"]
import random
#print (bagpack)
food = input ("Оставить человека без еды?: ")
if food in da:
    bagpack.pop(0)
#print (bagpack)
art = input ("Вы нашли артефакт, положить в рюкзак? ")
if art in da:
    bagpack.append("artifact")
#print (bagpack)
gyro = input ("Вы нашли гироскутер, взять его? ")
if gyro in da:
    bagpack.insert(1, "gyroscooter")
#print (bagpack)
mini = ["bottle", "scrap"]
bagpack.insert (3, mini)
#print (bagpack)
random.choice (bagpack)