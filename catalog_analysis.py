import math

movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155, "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},
    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
]

def average_rating(movies):
    total_rating = 0
    for movie in movies:
        total_rating += movie["rating"]
    return round(total_rating / len(movies), 1)

def catalog_age_stats(movies, current_year=2026):
    ages = [current_year - movie["year"] for movie in movies]
    oldest_age = max(ages)
    newest_age = min(ages)
    average_age = math.ceil(sum(ages) / len(ages))
    return (oldest_age, newest_age, average_age)

def duration_in_hours(minutes):
    hours = minutes // 60
    minutes %= 60
    return f"{hours}ч {minutes}м"

def rating_tier(rating):
    if rating >= 7:
        text_rating = "шедевр" if rating >= 9 else "хорошо"
    else:
        text_rating = "средне" if rating >= 5 else "слабо"
    return text_rating

def decade_label(year):
    match year:
        case _ if year > 2020:
            text_year = "новые"
        case _ if 2015 <= year <= 2020:
            text_year = "недавние"
        case _ if year < 2015:
            text_year = "старые"
    return text_year

def print_non_comedy_titles(movies):
    for movie in movies:
        if "comedy" in movie["genres"]:
            continue
        print(movie["title"])

def find_first_masterpiece(movies):    
    i = 0
    while i < len(movies):
        if movies[i]["rating"] >= 9.0:
            return movies[i]["title"]
            break
        i += 1
    else:
        return "Шедевров не найдено"

def count_long_movies(movies, threshold=120):
    i = 0
    for movie in movies:
        if movie["duration_min"] > threshold:
            i += 1
    return i

def normalize_title(title):
    words_list = title.split()
    new_words_list = []
    for word in words_list:
        new_word = word[:1].upper() + word[1:]
        new_words_list.append(new_word)
    return " ".join(new_words_list)

def make_slug(title):
    words_list = title.split()
    new_words_list = []
    for word in words_list:
        new_word = word.lower()
        new_words_list.append(new_word)
    return "-".join(new_words_list)

def format_report_line(movie):
    film_string = f'"{movie["title"]}" ({movie["year"]}) - {movie["rating"]}/10, {duration_in_hours(movie["duration_min"])}, жанры: {", ".join(list(movie["genres"]))}'
    return film_string


