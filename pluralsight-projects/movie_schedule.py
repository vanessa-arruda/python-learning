current_movie = {
 'The Grinch': '11:00 am',
 'Rudolph': '1:00 pm',
 'Frosty the Snowman': '3:00pm'
}

print("We're showing the following movies")
for key in current_movie:
 print(key)

movie = input("What movie would you like the showtime for?\n")

showtime = current_movie.get(movie)

if showtime == None:
 print("Requested movie not available")
else:
 print(movie, "is playing at", showtime)
 