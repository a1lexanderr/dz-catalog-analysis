import math

movies = [
    {
        "title": "The Dune Chronicles",
        "year": 2021,
        "genres": {"sci-fi", "drama"},
        "rating": 8.6,
        "duration_min": 155,
        "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"],
    },
    {
        "title": "Kitchen Stories",
        "year": 2019,
        "genres": {"comedy", "drama"},
        "rating": 7.1,
        "duration_min": 98,
        "actors": ["A. Novak", "M. Ferguson"],
    },
    {
        "title": "silent hours",
        "year": 2016,
        "genres": {"thriller", "drama"},
        "rating": 6.4,
        "duration_min": 112,
        "actors": ["J. Bloom", "K. Lee"],
    },
    {
        "title": "Comet Racers",
        "year": 2023,
        "genres": {"sci-fi", "action"},
        "rating": 5.9,
        "duration_min": 101,
        "actors": ["O. Isaac", "P. Diaz"],
    },
    {
        "title": "The Last Bakery",
        "year": 2014,
        "genres": {"comedy"},
        "rating": 7.8,
        "duration_min": 89,
        "actors": ["A. Novak", "T. Chalamet"],
    },
    {
        "title": "midnight in oslo",
        "year": 2020,
        "genres": {"thriller", "mystery"},
        "rating": 8.9,
        "duration_min": 124,
        "actors": ["K. Lee", "R. Ferguson"],
    },
    {
        "title": "Garden of Static",
        "year": 2022,
        "genres": {"drama"},
        "rating": 4.8,
        "duration_min": 137,
        "actors": ["P. Diaz", "J. Bloom"],
    },
    {
        "title": "The Quiet Algorithm",
        "year": 2024,
        "genres": {"sci-fi", "drama"},
        "rating": 9.2,
        "duration_min": 118,
        "actors": ["M. Ferguson", "O. Isaac"],
    },
    {
        "title": "Two Left Shoes",
        "year": 2011,
        "genres": {"comedy"},
        "rating": 6.0,
        "duration_min": 95,
        "actors": ["A. Novak", "K. Lee"],
    },
    {
        "title": "Red Harbor",
        "year": 2018,
        "genres": {"action", "thriller"},
        "rating": 7.3,
        "duration_min": 129,
        "actors": ["P. Diaz", "T. Chalamet"],
    },
]


def average_rating(movies):
    result = sum(movie["rating"] for movie in movies) / float(len(movies))
    return round(result, 1)


def catalog_age_stats(movies, current_year=2026):
    oldest = max(current_year - movie["year"] for movie in movies)
    newest = min(current_year - movie["year"] for movie in movies)
    average = math.ceil(
        sum(current_year - movie["year"] for movie in movies) / len(movies)
    )
    return oldest, newest, average


def duration_in_hours(minutes):
    hours = minutes // 60
    minutes = minutes % 60
    return f"{hours}ч {minutes}м"


def rating_tier(rating):
    if rating >= 9:
        return "шедевр"
    elif rating >= 7:
        return "хорошо"
    else:
        return "средне" if rating >= 5 else "слабо"


def decade_label(year):
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if year >= 2015:
            return "недавние"
        case _:
            return "старые"


# for movie in movies:
#     if "comedy" in movie["genres"]:
#         continue
#     print(movie["title"])

# index = 0
# while index < len(movies):
#     current_movie = movies[index]

#     if current_movie["rating"] > 9.0:
#         print(current_movie["title"])
#         break

#     index += 1
# else:
#     print("шедевров не найдено")


def count_long_movies(movies, threshold=120):
    count = 0
    for movie in movies:
        if movie["duration_min"] > threshold:
            count += 1
    return count


def normalize_title(title):
    words = title.split()
    for i, word in enumerate(words):
        words[i] = word[0].upper() + word[1:]
    return " ".join(words)


def make_slug(title):
    return title.lower().replace(" ", "-")

def format_report_line(movie):
    time = duration_in_hours(movie["duration_min"])
    sorted_genres = ", ".join(sorted(movie["genres"]))
    return (
        f'"{movie["title"]}" ({movie["year"]}) - '
        f'{movie["rating"]}/10, {time}, жанры: {sorted_genres}'
    )

def titles_sorted_by_rating(movies):
    sorted_movies = sorted(movies, key=lambda x: x["rating"], reverse=True)
    return [movie["title"] for movie in sorted_movies]


def top_n_by_rating(movies, n=3):
    result = []
    for movie in sorted(movies, key=lambda x: x["rating"], reverse=True)[:n]:
        result.append((movie["title"], movie["rating"]))
    return result


def count_by_genre(movies):
    result = {}
    for movie in movies:
        for genre in movie["genres"]:
            result[genre] = result.get(genre, 0) + 1
    return result


def actor_filmography(movies):
    result = {}
    for movie in movies:
        for actor in movie["actors"]:
            result.setdefault(actor, []).append(movie["title"])
    return result

def all_genres(movies):
    genres = set()
    for movie in movies:
        genres.update(movie["genres"])
    return genres


def common_actors(movie1, movie2):
    return set(movie1["actors"]) & set(movie2["actors"])


def genres_only_in_one(movies_a, movies_b):
    return all_genres(movies_a) - all_genres(movies_b)


def iter_high_rated(movies, min_rating=8.0):
    for movie in movies:
        if movie["rating"] >= min_rating:
            yield movie


# total_duration = sum(m["duration_min"] for m in movies if m["rating"] > 7)
# print(f"Суммарная длительность хороших фильмов: {total_duration} мин.\n")

# for movie in iter_high_rated(movies):
#     print(format_report_line(movie))


def build_report(movies):
    avg_rating = average_rating(movies)
    _, _, avg_age = catalog_age_stats(movies)

    print("ОТЧЕТ ПО КАТАЛОГУ")
    print(f"Средний рейтинг: {avg_rating}")
    print(f"Средний возраст фильмов: {avg_age} лет\n")

    print("Топ-3 фильма:")
    top_3_movies = sorted(movies, key=lambda m: m["rating"], reverse=True)[:3]
    for movie in top_3_movies:
        print(f"  {format_report_line(movie)}")
    print()

    genre_counts = count_by_genre(movies)
    sorted_genre_counts = sorted(
        genre_counts.items(), key=lambda item: item[1], reverse=True
    )

    print("Фильмов по жанрам:")
    for genre, count in sorted_genre_counts:
        print(f"  {genre} – {count}")
    print()

    unique_genres = ", ".join(sorted(all_genres(movies)))
    print(f"Все жанры каталога: {unique_genres}")


build_report(movies)
