def create_movie(title, year, genres, rating):
    """Build and return a movie dictionary (no printing, no list changes)."""
    return {
        "title": title,
        "year": year,
        "genres": genres,
        "rating": rating,
    }


def display_movies(movies, heading):
    """Print a formatted table of movies under the given heading."""
    print(heading)
    print("-" * 51)

    if not movies:
        print("No movies in this collection.")
        return

    for movie in movies:
        title = movie["title"]
        if len(title) > 18:
            title = title[:17] + "."  # e.g. "The Shawshank Red."
        genres_text = " / ".join(movie["genres"])
        print(f"{title:<19}{movie['year']:<5}{genres_text:<31}{movie['rating']:.1f}")


def find_top_rated(movies, n):
    """Return the top n movies by rating without modifying the original list."""
    sorted_movies = sorted(movies, key=lambda m: m["rating"], reverse=True)
    return sorted_movies[:n]


def get_average_rating(movies):
    """Return the average rating rounded to 2 decimals (0.0 if empty)."""
    if len(movies) == 0:
        return 0.0

    total = 0.0
    for movie in movies:
        total += movie["rating"]

    return round(total / len(movies), 2)


# ---------------------------- Main program ----------------------------

# 1. Starter list
movies = [
    create_movie("Percy Jackson", 2010, ["Sci-Fi", "Adventure"], 7.8),
    create_movie("Percy Jackson: The Lost Crown", 2014, ["Sci-Fi", "Adventure"], 7.9),
    create_movie("Pirates of the Caribbean", 2013, ["Thriller", "Adventure"], 8.9),
    create_movie("Harry Potter", 2009, ["Adventure", "Gridy"], 8.8),
    create_movie("Jumanji", 2015, ["Sci-Fi", "Adventure", "Thriller"], 7.8),
]

# 2. Display the collection as loaded
display_movies(movies, "Your Movie Collection")

# 3. Add two new movies
print("\nAdd two new movies to the collection.")
for i in range(2):
    print(f"\nMovie {i + 1}:")
    title = input("Title: ").strip()
    year = int(input("Year: "))
    genres_input = input("Genres (separated by commas): ")
    genres = [g.strip() for g in genres_input.split(",")]
    rating = float(input("Rating: "))

    movies.append(create_movie(title, year, genres, rating))

# 4. Sort in place by year and display
movies.sort(key=lambda m: m["year"])
print()
display_movies(movies, "All Movies Sorted by Year")

# 5. Top 3 rated
top_three = find_top_rated(movies, 3)
print()
display_movies(top_three, "Top 3 Rated Movies")

# 6. Average rating
print(f"\nCollection average rating: {get_average_rating(movies):.2f}")