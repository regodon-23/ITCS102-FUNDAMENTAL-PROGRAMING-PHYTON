print("Welcome to the Manga Recommender! ")
print("Answer a few questions to find your next read.")
genre = input("What genre do you like? (action, romance): ")
length = input("How long should the manga be? (short, medium, long): ")
decade = input("Which decade? (2010s, 2020s): ")

if genre == "action":
	if length == "short" and decade == "2010s":
	 print("Recommendation: Vampire night")
	elif length == "short" and decade == "2020s":
	 print("Recommendation: Beyond the clouds ")
	elif length == "medium" and decade == "2010s":
	 print("Recommendation: Naruto")
	elif length == "medium" and decade == "2020s":
	 print("Recommendation: Chainsaw man")
	elif length == "long" and decade == "2010s":
	 print("Recommendation: Hakuoki")
	elif length == "long" and decade == "2020s":
	 print("Recommendation: Bleach")
	else:
	 print("Sorry, no action manga matches your selection.")

elif genre == "romance":
	if length == "short" and decade == "2010s":
	 print("Recommendation: The breaker")
	elif length == "short" and decade == "2020s":
	 print("Recommendation: Season of blossom")
	elif length == "medium" and decade == "2010s":
	 print("Recommendation: House of the sun")
	elif length == "medium" and decade == "2020s":
	 print("Recommendation: Villains are destinied to die")
	elif length == "long" and decade == "2010s":
	 print("Recommendation: Noragami")
	elif length == "long" and decade == "2020s":
	 print("Recommendation: Ohh la la")
	else:
	 print("Sorry, no romance manga matches your selection.")

else:
	print("Invalid genre. Please choose from 'action', or 'romance'.")




