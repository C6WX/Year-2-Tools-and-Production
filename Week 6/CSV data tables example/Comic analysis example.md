# Comic Books Dataset — Analysis Report

## 1. Dataset Overview

| Metric | Value |
|--------|-------|
| Total records (after cleaning) | 9,870 |
| Year range | 1938–2025 |
| Unique publishers | 25 |
| Unique genres | 15 |
| Unique formats | 6 |

This dataset contains information on comic books including their titles, publishers,
release years, formats, and genres.

---

## 2. Data Cleaning Summary

The following cleaning steps were applied to the raw dataset:

- Detected 463 missing values across columns:
-   - Title: 31 missing
-   - Publisher: 42 missing
-   - ReleaseYear: 313 missing
-   - Format: 28 missing
-   - Genre: 49 missing
- Removed 99 duplicate rows.
- Standardised 'Publisher': reduced unique values from 105 to 25 (strip + title case).
- Standardised 'Format': reduced unique values from 18 to 6 (strip + title case).
- Standardised 'Genre': reduced unique values from 60 to 15 (strip + title case).
- Corrected acronym-based publisher names (DC, IDW, AWA, MLT).
- Stripped whitespace from 'Title'.
- Converted ReleaseYear to numeric; 51 non-numeric values coerced to NaN.
- Dropped 31 rows with missing Title.
- 
Cleaning complete. Rows: 10,000 → 9,870 (130 removed).

---

## 3. Key Findings

- The dataset spans from **1938–2025**, with the peak release year being **2020** (258 releases).
- **Marvel Comics** is the dominant publisher with **2,605** entries, followed by **DC Comics** with **2,375** entries.
- **Single Issue** is the most common format, accounting for 5,398 entries (54.7% of the dataset).
- **Superhero** is the dominant genre with 3,120 entries.
- The comic book industry shows strong growth from the 1990s onward, with the 2000s and 2010s representing the bulk of releases.

---

## 4. Graph Analysis

### 4.1 Releases by Year

![Releases by Year](graphs/01_releases_by_year.png)

This line chart shows the number of comic book releases per year. The area under the
curve is shaded for visual emphasis.

**Notable patterns:**
- There is a clear upward trend in releases starting in the late 1980s and accelerating
  through the 1990s and 2000s.
- The peak year is **2020**, with **258** releases.
- Earlier decades (pre-1970s) show relatively few entries, which may reflect both lower
  production volumes and gaps in the dataset.

---

### 4.2 Top 10 Publishers

![Top Publishers](graphs/02_top_publishers.png)

This horizontal bar chart shows the ten most prolific publishers in the dataset.

**Notable patterns:**
- **Marvel Comics** and **DC Comics** dominate the market, together
  accounting for 4,980 entries
  (50.5% of the dataset).
- A significant drop-off occurs after the top 2, with **Image Comics** at
  1,004 entries—roughly a third of either market leader.
- The long tail of smaller publishers is typical of the industry.

---

### 4.3 Format Distribution

![Format Distribution](graphs/03_format_distribution.png)

This bar chart shows how comic books are distributed across different formats.

**Notable patterns:**
- **Single Issue** dominates with 5,398 entries, which is
  expected as it is the traditional publishing unit for comics.
- **Trade Paperback** is the second most common format at 1,951
  entries, reflecting the popularity of collected editions.
- Digital format represents a smaller share, suggesting the dataset may skew toward
  physical publications or pre-digital era entries.

---

### 4.4 Genre Distribution

![Genre Distribution](graphs/04_genre_distribution.png)

This horizontal bar chart shows the top genres by number of entries.

**Notable patterns:**
- **Superhero** is by far the most common genre, followed by
  **Science Fiction** and **Horror**.
- The dominance of Superhero reflects the historical core market of the
  comic book industry.
- Genres like Romance and War represent niche
  categories with smaller but dedicated audiences.

---

### 4.5 Publisher × Genre Breakdown

![Publisher by Genre](graphs/05_publisher_by_genre.png)

This grouped bar chart shows how the top 5 publishers distribute their output across
the top 6 genres.

**Notable patterns:**
- The major publishers (Marvel and DC) are heavily weighted toward Superhero comics.
- Independent publishers like Image Comics show more genre diversity, with stronger
  representation in Science Fiction, Horror, and other non-superhero genres.
- This visualization highlights the strategic focus of each publisher.

---

### 4.6 Format Over Time

![Format Over Time](graphs/06_format_over_time.png)

This stacked area chart shows how the distribution of comic book formats has evolved
over time.

**Notable patterns:**
- Single Issues have historically dominated but the share of Trade Paperbacks and
  Graphic Novels has grown steadily since the 1990s.
- Hardcover editions show a moderate increase in recent decades, reflecting the
  growing collector and prestige market.
- Digital formats appear primarily in the most recent years.

---

### 4.7 Releases by Decade

![Decade Breakdown](graphs/07_decade_breakdown.png)

This bar chart aggregates releases by decade for a high-level view of the industry's
growth trajectory.

**Notable patterns:**
- Each successive decade from the 1980s onward shows substantially more releases than
  the previous one.
- The 2000s and 2010s represent the largest share of data, aligning with the industry's
  expansion and the rise of independent publishers.
- Earlier decades have fewer entries, partly due to the dataset's coverage.

---

### 4.8 Top Publisher Trends Over Time

![Publisher Trends](graphs/08_publisher_trends.png)

This line chart tracks the annual output of the top 5 publishers across the full
time range of the dataset.

**Notable patterns:**
- Marvel and DC show the most consistent and highest output, often moving in tandem
  with broader industry trends.
- Image Comics shows growth mainly from the early 1990s (when it was founded) onward.
- Smaller publishers show more volatile year-to-year output, reflecting their
  smaller catalogs and project-based publishing schedules.

---

## 5. Summary of Key Insights

1. **Market concentration**: The comic book industry is highly concentrated, with
   Marvel and DC commanding approximately 50% of all entries.

2. **Growth trajectory**: The industry has seen significant growth since the 1990s,
   with output levels in the 2000s and 2010s dwarfing earlier decades.

3. **Genre dominance**: Superhero comics remain the dominant genre, though independent
   publishers are diversifying the market with stronger presences in horror, sci-fi,
   and drama.

4. **Format evolution**: While single issues remain the primary format, the market has
   diversified with growing shares for trade paperbacks, graphic novels, and hardcovers.

5. **Limitations**: This dataset may not capture all published comics (particularly
   international titles and very small press releases). Year coverage before the 1980s
   is sparse, which limits historical analysis. Some missing values were present in the
   raw data and handled through exclusion in relevant analyses.

---

*Report generated by `analyze_comics.py`*
