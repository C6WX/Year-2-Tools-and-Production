"""
Generate a realistic synthetic comic books dataset with 10,000 entries.
Mimics the Kaggle dataset schema: Title, Publisher, ReleaseYear, Format, Genre
"""
import csv
import random

random.seed(42)

# --- Realistic distributions ---
PUBLISHERS = {
    "Marvel Comics": 2200,
    "DC Comics": 2000,
    "Image Comics": 800,
    "Dark Horse Comics": 600,
    "IDW Publishing": 500,
    "Boom! Studios": 400,
    "Valiant Comics": 300,
    "Dynamite Entertainment": 250,
    "Archie Comics": 200,
    "Oni Press": 150,
    "Vertigo": 140,
    "Top Cow Productions": 120,
    "Titan Comics": 100,
    "Aftershock Comics": 90,
    "Fantagraphics Books": 80,
    "Viz Media": 70,
    "Antarctic Press": 60,
    "Avatar Press": 50,
    "AWA Studios": 40,
    "Scout Comics": 30,
    "Action Lab Entertainment": 25,
    "Abstract Studio": 22,
    "Aspen MLT": 18,
    "Zenescope Entertainment": 15,
    "Black Mask Studios": 10,
}

FORMATS = {
    "Single Issue": 5500,
    "Trade Paperback": 2000,
    "Hardcover": 1000,
    "Graphic Novel": 800,
    "Digital": 500,
    "Omnibus": 200,
}

GENRES = {
    "Superhero": 2800,
    "Science Fiction": 1200,
    "Horror": 800,
    "Fantasy": 750,
    "Crime": 600,
    "Action/Adventure": 550,
    "Drama": 500,
    "Mystery": 450,
    "Comedy": 350,
    "Thriller": 300,
    "Romance": 250,
    "War": 200,
    "Western": 100,
    "Slice of Life": 80,
    "Historical Fiction": 70,
}

# Year distribution: mostly 1990-2025, some earlier
def generate_year():
    r = random.random()
    if r < 0.02:
        return random.randint(1938, 1959)
    elif r < 0.08:
        return random.randint(1960, 1979)
    elif r < 0.20:
        return random.randint(1980, 1989)
    elif r < 0.50:
        return random.randint(1990, 2004)
    else:
        return random.randint(2005, 2025)

def weighted_choice(dist):
    items = list(dist.keys())
    weights = list(dist.values())
    return random.choices(items, weights=weights, k=1)[0]

# Title word pools
ADJECTIVES = [
    "Amazing", "Incredible", "Ultimate", "Uncanny", "Savage", "Mighty",
    "Dark", "Eternal", "Invincible", "Spectacular", "Fantastic", "Superior",
    "Deadly", "Secret", "Final", "Infinite", "Immortal", "Total", "Absolute",
    "Iron", "Shadow", "Ghost", "Cosmic", "Mystic", "Rogue", "Brave", "Fearless",
    "New", "Old", "Ancient", "Modern", "Young", "Wild", "Lone", "Silent",
    "Crimson", "Golden", "Silver", "Black", "Red", "Blue", "Green", "White",
]
NOUNS = [
    "Spider-Man", "Batman", "Wolverine", "Superman", "Deadpool", "Hulk",
    "Avengers", "X-Men", "Justice League", "Flash", "Daredevil", "Thor",
    "Punisher", "Spawn", "Hellboy", "Saga", "Sandman", "Watchmen",
    "Knight", "Warrior", "Guardian", "Hunter", "Titan", "Phoenix",
    "Dragon", "Wolf", "Hawk", "Panther", "Viper", "Falcon", "Storm",
    "Quest", "Legion", "Empire", "Realm", "Destiny", "Chronicle",
    "Wars", "Tales", "Legends", "Origins", "Archives", "Files",
    "Blade", "Shield", "Hammer", "Arrow", "Scepter", "Crown",
]
SUFFIXES = [
    "", "", "", "", "", "",  # most titles have no suffix
    ": Reborn", ": Unleashed", ": Rising", ": Awakening", ": Endgame",
    ": The Last Stand", ": Dark Days", ": New Dawn", ": Genesis",
    " Vol. 1", " Vol. 2", " Vol. 3", " #1", " #2", " #3", " #4", " #5",
    " Annual", " Special", " Premiere",
]

def generate_title():
    pattern = random.random()
    if pattern < 0.3:
        return f"The {random.choice(ADJECTIVES)} {random.choice(NOUNS)}{random.choice(SUFFIXES)}"
    elif pattern < 0.6:
        return f"{random.choice(ADJECTIVES)} {random.choice(NOUNS)}{random.choice(SUFFIXES)}"
    elif pattern < 0.8:
        return f"{random.choice(NOUNS)}{random.choice(SUFFIXES)}"
    else:
        return f"{random.choice(ADJECTIVES)} {random.choice(ADJECTIVES)} {random.choice(NOUNS)}{random.choice(SUFFIXES)}"

# Introduce intentional messiness for the cleaning exercise
def maybe_dirty_publisher(pub):
    r = random.random()
    if r < 0.03:
        return " " + pub  # leading space
    elif r < 0.06:
        return pub + " "  # trailing space
    elif r < 0.08:
        return pub.lower()  # lowercase
    elif r < 0.10:
        return pub.upper()  # uppercase
    return pub

def maybe_dirty_genre(genre):
    r = random.random()
    if r < 0.03:
        return genre.lower()
    elif r < 0.05:
        return " " + genre
    elif r < 0.07:
        return genre + " "
    return genre

def maybe_dirty_format(fmt):
    r = random.random()
    if r < 0.03:
        return fmt.lower()
    elif r < 0.05:
        return " " + fmt
    return fmt

def maybe_dirty_year(year):
    r = random.random()
    if r < 0.02:
        return ""  # missing
    elif r < 0.03:
        return "N/A"
    elif r < 0.035:
        return "Unknown"
    return str(year)

# Generate data
rows = []
seen = set()
target = 10000
duplicates_added = 0

while len(rows) < target:
    title = generate_title()
    publisher = maybe_dirty_publisher(weighted_choice(PUBLISHERS))
    year = maybe_dirty_year(generate_year())
    fmt = maybe_dirty_format(weighted_choice(FORMATS))
    genre = maybe_dirty_genre(weighted_choice(GENRES))

    row = (title, publisher, year, fmt, genre)

    # Add ~1% duplicate rows intentionally
    if len(rows) > 100 and random.random() < 0.01 and duplicates_added < 100:
        dup = random.choice(rows)
        rows.append(dup)
        duplicates_added += 1
    else:
        rows.append(row)

# Some rows get missing values
for i in random.sample(range(len(rows)), 150):
    field = random.choice([0, 1, 3, 4])  # Title, Publisher, Format, Genre
    row = list(rows[i])
    row[field] = ""
    rows[i] = tuple(row)

random.shuffle(rows)

# Write CSV
with open("comic_books.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Title", "Publisher", "ReleaseYear", "Format", "Genre"])
    for row in rows:
        writer.writerow(row)

print(f"Generated {len(rows)} rows ({duplicates_added} intentional duplicates)")
print("Saved to comic_books.csv")
