#Programmer: Stephanie Byrne
#Date: 8/06/2020
#File: SelfGameDraft.py

#PLOT: Essentially it is a 12 Question (maybe 10) survey that produces a journal like entry in text doc.
# Futeure developement: Advice for the next day as well

#Ask phil how I can get 3 numbers (from dates) as input in a string and separate them as 3 1ntegars
b_day = int(input("What is the day of birth? "))
b_month = input("What is your month of birth? ")
t_day = int(input("What day of the month is it? "))
t_month = input("What month is it? ")
d_week = input("What day of the week is it? ")
#temp = int(input("What is the temperature today? (just the number in celsius) "))
#fav_sea = input("What is your favorite season? ")
#work = input("Did you work today? ")
#people = int(input("How many people did you interact with today? "))
message = ""

#For the Activity and Clothing section, ASK PHIL what the best way to display options for input?
# Should I give the answer a numerical value?
if b_month == "december":
    if b_day < 17:
        star = "when ya like people, over there"
    else:
        star = "when you just want to break free"
elif b_month == "january":
    if b_day < 18:
        star = "when you have weird questions but need answers"
    else:
        star = "when you want to get to the point"
elif b_month == "february":
    if b_day < 15:
        star = "when you know how it can all go wrong"
    else:
        star = "when you spend to long analysing"
elif b_month == "march":
    if b_day < 11:
        star = "when you don't get what the fuss is about"
    else:
        star = "when you just want to day dream and have fun"
elif b_month == "april":
    if b_day < 18:
       star = "when all you want to do is help"
    else:
        star = "when you know it's time to lead"
elif b_month == "may":
    if b_day < 13:
        star = "when your passion becomes obsession"
    else:
        star = "when you don't want things to change"
elif b_month == "june":
    if b_day < 19:
        star = "when you have it all going for you but who notices"
    else:
        star = "when ya ready to go but where to go"
elif b_month == "july":
    if b_day < 21:
        star = "when you jump at all opportunities that come your way"
    else:
        star = "when you are conscious of those around you"
elif b_month == "august":
    if b_day < 9:
        star = "when you feel the pain of those around you"
    else:
        star = "when you give so much more than you take"
elif b_month == "september":
    if b_day < 15:
        star = "when you have people that lookup to you"
    else:
        star = "when you seem to be the only one working their hardest"
elif b_month == "october":
    if b_day < 30:
        star = "when patience and kindness don't ever seem to be enough"
    else:
        star = "when your stuck in the middle"
elif b_month == "november":
    if b_day < 22:
       star = "when you see the light and have to explain it to everyone"
    else:
        star = "Seductive Scorpio"

if t_month == "december":
    if t_day < 17:
        message += "Time to build on your visions. You never know who may notice!"
    else:
        message += "You are optimistic now. Adventures will satisfy your philosophical questions!"
elif t_month == "january":
    if t_day < 18:
        message += "You are being a little too honest and a little too rebellious. Use that energy for good!"
    else:
        message += "You are seeing whats real, that focus can leave you uptight."
elif t_month == "february":
    if t_day < 15:
        message += "You might be a little sensitive and quite dry with your reactions of late."
    else:
        message += "You might need to distance yourself and look a little deeper."
elif t_month == "march":
    if t_day < 11:
        message += "Might be best to go with the flow"
    else:
        message += "Your imagination is running wild. All the Romance and life's pleasures."
elif t_month == "april":
    if t_day < 18:
       message += "You are happy to help and think fondly of others today!"
    else:
        message += "You are confident and direct which can be intimidating."
elif t_month == "may":
    if t_day < 13:
        message += "You can get frustrated with distractions now, stay motivated!"
    else:
        message += "You kinda have it all going for you, stability and practical."
elif t_month == "june":
    if t_day < 19:
        message += "You have the right idea, let it grow, don't hold onto old ideas."
    else:
        message += "You stay on top of any situation, eventually!"
elif t_month == "july":
    if t_day < 21:
        message += "You are ready to go but make better choices, for your sake."
    else:
        message += "You have a deep understanding of those around you."
elif t_month == "august":
    if t_day < 9:
        message += "You stay loyal and people rely on your intuition."
    else:
        message += "Generosity and honest makes you a great leader."
elif t_month == "september":
    if t_day < 15:
        message += "People will notice you, how could they not."
    else:
        message += "You have worked hard and are becoming quite reliable."
elif t_month == "october":
    if t_day < 30:
        message += "Your patience will bring out something beautifully creative in you."
    else:
        message += "You are stuck in the middle of it. It's your answer they want!"
elif t_month == "november":
    if t_day < 22:
       message += "You know what is fair and how to stay positive. People like that."
    else:
        message += "You are feeling brave. Honest and loyal. Aim High!"

print("It's one of those days ", star, ", on a", d_week, "of all days!", message)
#ADD and change the horoscope01.py file (exclude the chinese horoscope section) for message
#Change the horoscope file to also adapt for Todays date too add on message
#day of the week is 7 options with an stereotype feeling associated with that day "Monday bad, Saturday Good" message
#Temp = has 3 if, cold, warm, hot, with associated feelings in message
#ASK PHIL = Fav Season would be good to associated with the days temp???