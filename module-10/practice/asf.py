import movie as trustmebro
from movie import Movie as UrMom
from stdio import writeln as print



marsMan = UrMom('The Martian', 'Sci-Fi', '2015', '142 minutes')
for i in [4, 4.5, 4.5]:
	marsMan.add_rating(i)
mAvg = marsMan.get_average_rating()


erthRobotDude = UrMom('WALL-E', 'Kid-Friendly Dystopian', '2008', '97 minutes')
for i in [4.5, 5, 53624]:
	erthRobotDude.add_rating(i)
eAvg = erthRobotDude.get_average_rating()


gamerBro = UrMom('Ready Player One', 'Sci-Fi Dystopian', '2018', '140 minutes')
for i in [3, 5, 4]:
	gamerBro.add_rating(i)
gAvg = gamerBro.get_average_rating()



print(f'\n{str(marsMan)}\nAvg rating: {mAvg:.1f}')
print(f'\n{str(erthRobotDude)}\nAvg rating: {eAvg:.1f}')
print(f'\n{str(gamerBro)}\nAvg rating: {gAvg:.1f}')
