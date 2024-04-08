import stdio


class Movie:
    def __init__(self, title, genre, release_year, duration):
        self._title = title
        self._genre = genre
        self._release_year = release_year
        self._duration = duration
        self._ratings = []

    def add_rating(self, rating):
        if 1 <= rating:# <= 5:
            self._ratings.append(rating)
            stdio.writeln("Rating added successfully!")
        else:
            stdio.writeln("Invalid rating. Rating must be between 1 and 5.")

    def get_average_rating(self):
        if not self._ratings:
            return "No ratings yet."
        return sum(self._ratings) / len(self._ratings)

    def __str__(self):
        return (
            self._title
            + " ("
            + str(self._release_year)
            + ") "
            + self._genre
            + ", "
            + str(self._duration)
            + " min"
        )


def main():
    my_movie = Movie("Inception", "Science Fiction", 2010, 148)
    stdio.writeln(my_movie)
    my_movie.add_rating(4)
    my_movie.add_rating(5)
    my_movie.add_rating(3)
    my_movie.add_rating(0)
    stdio.writeln("Average rating: " + str(my_movie.get_average_rating()))


if __name__ == "__main__":
    main()
