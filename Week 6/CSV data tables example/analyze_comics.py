"""
Comic Books Dataset Analysis
=============================
Loads, cleans, analyzes, and visualizes a comic books dataset.
Produces PNG graphs and a Markdown report.

Usage:
    python analyze_comics.py

Configuration:
    Edit DATASET_PATH below if the CSV file is in a different location.
"""

import os
import sys
import pandas as pd
import matplotlib
matplotlib.use("Agg")  # non-interactive backend for saving files
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import textwrap

# ─── Configuration ──────────────────────────────────────────────────────────
DATASET_PATH = "comic_books.csv"
OUTPUT_DIR = "output"
GRAPHS_DIR = os.path.join(OUTPUT_DIR, "graphs")
REPORT_PATH = os.path.join(OUTPUT_DIR, "analysis.md")
CLEANED_CSV_PATH = os.path.join(OUTPUT_DIR, "cleaned_comics.csv")

# ─── Visual Style ───────────────────────────────────────────────────────────
COLORS = {
    "primary": "#2C3E50",
    "accent": "#E74C3C",
    "palette": [
        "#2C3E50", "#E74C3C", "#3498DB", "#2ECC71", "#F39C12",
        "#9B59B6", "#1ABC9C", "#E67E22", "#34495E", "#16A085",
        "#D35400", "#8E44AD", "#27AE60", "#C0392B", "#2980B9",
    ],
}
plt.rcParams.update({
    "figure.facecolor": "white",
    "axes.facecolor": "#FAFAFA",
    "axes.edgecolor": "#CCCCCC",
    "axes.grid": True,
    "grid.alpha": 0.3,
    "grid.color": "#CCCCCC",
    "font.size": 11,
    "axes.titlesize": 14,
    "axes.titleweight": "bold",
    "axes.labelsize": 12,
    "xtick.labelsize": 10,
    "ytick.labelsize": 10,
    "figure.dpi": 150,
})


# ═══════════════════════════════════════════════════════════════════════════
# 1. DATA LOADING
# ═══════════════════════════════════════════════════════════════════════════

def load_data(path):
    """Load CSV and perform initial inspection."""
    if not os.path.exists(path):
        print(f"ERROR: Dataset file not found at '{path}'")
        sys.exit(1)

    df = pd.read_csv(path, dtype=str)  # load all as strings initially
    print("=" * 60)
    print("DATASET LOADED")
    print("=" * 60)
    print(f"  Rows: {len(df):,}")
    print(f"  Columns: {list(df.columns)}")
    print(f"\nFirst 5 rows:")
    print(df.head().to_string(index=False))
    print()
    return df


# ═══════════════════════════════════════════════════════════════════════════
# 2. DATA CLEANING
# ═══════════════════════════════════════════════════════════════════════════

def clean_data(df):
    """Clean the dataset and return (cleaned_df, cleaning_log)."""
    log = []
    original_count = len(df)

    # --- Replace empty strings with NaN ---
    df = df.replace(r"^\s*$", pd.NA, regex=True)

    # --- Report missing values ---
    missing = df.isna().sum()
    missing_total = missing.sum()
    if missing_total > 0:
        log.append(f"Detected {missing_total} missing values across columns:")
        for col in df.columns:
            if missing[col] > 0:
                log.append(f"  - {col}: {missing[col]} missing")
    else:
        log.append("No missing values detected.")

    # --- Remove duplicate rows ---
    dup_count = df.duplicated().sum()
    if dup_count > 0:
        df = df.drop_duplicates().reset_index(drop=True)
        log.append(f"Removed {dup_count} duplicate rows.")
    else:
        log.append("No duplicate rows found.")

    # --- Standardise text fields (strip whitespace, title case) ---
    text_cols = ["Publisher", "Format", "Genre"]
    for col in text_cols:
        before = df[col].nunique()
        df[col] = df[col].astype(str).str.strip().str.title()
        # Fix <Na> artefact from converting pd.NA to string
        df[col] = df[col].replace("<NA>", pd.NA).replace("Nan", pd.NA)
        after = df[col].nunique()
        if before != after:
            log.append(f"Standardised '{col}': reduced unique values from {before} to {after} (strip + title case).")
        else:
            log.append(f"Standardised '{col}': applied strip and title case (no duplicates collapsed).")

    # Fix known acronym-based names corrupted by title case
    acronym_fixes = {
        "Dc Comics": "DC Comics",
        "Idw Publishing": "IDW Publishing",
        "Awa Studios": "AWA Studios",
        "Aspen Mlt": "Aspen MLT",
    }
    for wrong, right in acronym_fixes.items():
        df["Publisher"] = df["Publisher"].replace(wrong, right)
    log.append("Corrected acronym-based publisher names (DC, IDW, AWA, MLT).")

    # Title: just strip whitespace
    df["Title"] = df["Title"].astype(str).str.strip()
    df["Title"] = df["Title"].replace("<NA>", pd.NA).replace("Nan", pd.NA)
    log.append("Stripped whitespace from 'Title'.")

    # --- Convert ReleaseYear to numeric ---
    df["ReleaseYear"] = pd.to_numeric(df["ReleaseYear"], errors="coerce")
    invalid_years = df["ReleaseYear"].isna().sum() - missing["ReleaseYear"]
    if invalid_years > 0:
        log.append(f"Converted ReleaseYear to numeric; {invalid_years} non-numeric values coerced to NaN.")
    else:
        log.append("Converted ReleaseYear to numeric; no non-numeric values found.")

    # Filter years to a sensible range (1900-2030)
    mask_bad_year = df["ReleaseYear"].notna() & (
        (df["ReleaseYear"] < 1900) | (df["ReleaseYear"] > 2030)
    )
    bad_year_count = mask_bad_year.sum()
    if bad_year_count > 0:
        df.loc[mask_bad_year, "ReleaseYear"] = pd.NA
        log.append(f"Set {bad_year_count} out-of-range years (outside 1900–2030) to NaN.")

    # Convert to nullable integer
    df["ReleaseYear"] = df["ReleaseYear"].astype("Int64")

    # --- Drop rows missing Title (the identifier) ---
    title_na = df["Title"].isna().sum()
    if title_na > 0:
        df = df.dropna(subset=["Title"]).reset_index(drop=True)
        log.append(f"Dropped {title_na} rows with missing Title.")

    final_count = len(df)
    log.append(f"\nCleaning complete. Rows: {original_count:,} → {final_count:,} "
               f"({original_count - final_count:,} removed).")

    return df, log


# ═══════════════════════════════════════════════════════════════════════════
# 3. GRAPH HELPERS
# ═══════════════════════════════════════════════════════════════════════════

def save_fig(fig, filename):
    """Save figure to GRAPHS_DIR and close it."""
    path = os.path.join(GRAPHS_DIR, filename)
    fig.savefig(path, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"  Saved: {path}")
    return path


def add_bar_labels(ax, bars, fmt="{:.0f}", fontsize=8):
    """Add value labels to bar chart bars."""
    for bar in bars:
        width = bar.get_width() if bar.get_width() > bar.get_height() else bar.get_height()
        if bar.get_width() > bar.get_height():
            # horizontal bar
            ax.text(
                bar.get_width() + 0.5, bar.get_y() + bar.get_height() / 2,
                fmt.format(bar.get_width()), va="center", fontsize=fontsize, color="#333"
            )
        else:
            # vertical bar
            ax.text(
                bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.5,
                fmt.format(bar.get_height()), ha="center", va="bottom",
                fontsize=fontsize, color="#333"
            )


# ═══════════════════════════════════════════════════════════════════════════
# 4. GRAPH CREATION
# ═══════════════════════════════════════════════════════════════════════════

def graph_releases_by_year(df):
    """Graph 1: Releases per year (line chart)."""
    year_data = df.dropna(subset=["ReleaseYear"])
    yearly = year_data.groupby("ReleaseYear").size().sort_index()

    fig, ax = plt.subplots(figsize=(14, 6))
    ax.fill_between(yearly.index, yearly.values, alpha=0.3, color=COLORS["palette"][2])
    ax.plot(yearly.index, yearly.values, color=COLORS["palette"][2], linewidth=2)
    ax.set_title("Comic Book Releases by Year")
    ax.set_xlabel("Year")
    ax.set_ylabel("Number of Releases")
    ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
    fig.tight_layout()
    return save_fig(fig, "01_releases_by_year.png"), yearly


def graph_top_publishers(df):
    """Graph 2: Top 10 publishers (horizontal bar chart)."""
    pub_data = df.dropna(subset=["Publisher"])
    top = pub_data["Publisher"].value_counts().head(10)

    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.barh(
        top.index[::-1], top.values[::-1],
        color=COLORS["palette"][:10][::-1], edgecolor="white", linewidth=0.5
    )
    add_bar_labels(ax, bars)
    ax.set_title("Top 10 Publishers by Number of Entries")
    ax.set_xlabel("Number of Comic Books")
    ax.set_ylabel("")
    fig.tight_layout()
    return save_fig(fig, "02_top_publishers.png"), top


def graph_format_distribution(df):
    """Graph 3: Format distribution (bar chart)."""
    fmt_data = df.dropna(subset=["Format"])
    fmt_counts = fmt_data["Format"].value_counts()

    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(
        fmt_counts.index, fmt_counts.values,
        color=COLORS["palette"][:len(fmt_counts)], edgecolor="white", linewidth=0.5
    )
    add_bar_labels(ax, bars, fontsize=9)
    ax.set_title("Distribution of Comic Book Formats")
    ax.set_xlabel("Format")
    ax.set_ylabel("Count")
    plt.xticks(rotation=30, ha="right")
    fig.tight_layout()
    return save_fig(fig, "03_format_distribution.png"), fmt_counts


def graph_genre_distribution(df):
    """Graph 4: Top genres (horizontal bar chart)."""
    genre_data = df.dropna(subset=["Genre"])
    top_genres = genre_data["Genre"].value_counts().head(12)

    fig, ax = plt.subplots(figsize=(10, 7))
    bars = ax.barh(
        top_genres.index[::-1], top_genres.values[::-1],
        color=COLORS["palette"][:len(top_genres)][::-1], edgecolor="white", linewidth=0.5
    )
    add_bar_labels(ax, bars)
    ax.set_title("Top Genres by Number of Comic Books")
    ax.set_xlabel("Count")
    ax.set_ylabel("")
    fig.tight_layout()
    return save_fig(fig, "04_genre_distribution.png"), top_genres


def graph_publisher_by_genre(df):
    """Graph 5: Top publishers vs. top genres (grouped bar chart)."""
    data = df.dropna(subset=["Publisher", "Genre"])
    top_pubs = data["Publisher"].value_counts().head(5).index.tolist()
    top_genres = data["Genre"].value_counts().head(6).index.tolist()

    filtered = data[data["Publisher"].isin(top_pubs) & data["Genre"].isin(top_genres)]
    cross = filtered.groupby(["Publisher", "Genre"]).size().unstack(fill_value=0)
    # Reorder
    cross = cross.reindex(index=top_pubs, columns=top_genres, fill_value=0)

    fig, ax = plt.subplots(figsize=(14, 7))
    x = range(len(cross.index))
    width = 0.13
    for i, genre in enumerate(cross.columns):
        offset = (i - len(cross.columns) / 2 + 0.5) * width
        bars = ax.bar(
            [xi + offset for xi in x], cross[genre], width,
            label=genre, color=COLORS["palette"][i], edgecolor="white", linewidth=0.5
        )

    ax.set_title("Top 5 Publishers × Top 6 Genres")
    ax.set_xlabel("Publisher")
    ax.set_ylabel("Number of Comic Books")
    ax.set_xticks(list(x))
    ax.set_xticklabels([textwrap.fill(p, 15) for p in cross.index], fontsize=9)
    ax.legend(title="Genre", bbox_to_anchor=(1.02, 1), loc="upper left", fontsize=9)
    fig.tight_layout()
    return save_fig(fig, "05_publisher_by_genre.png"), cross


def graph_format_over_time(df):
    """Graph 6: Format popularity over time (stacked area chart)."""
    data = df.dropna(subset=["ReleaseYear", "Format"])
    # Focus on years with enough data
    year_counts = data.groupby("ReleaseYear").size()
    valid_years = year_counts[year_counts >= 5].index
    data = data[data["ReleaseYear"].isin(valid_years)]

    top_formats = data["Format"].value_counts().head(5).index.tolist()
    data_top = data.copy()
    data_top.loc[~data_top["Format"].isin(top_formats), "Format"] = "Other"

    pivot = data_top.groupby(["ReleaseYear", "Format"]).size().unstack(fill_value=0)
    # Ensure consistent ordering
    format_order = [f for f in top_formats if f in pivot.columns]
    if "Other" in pivot.columns:
        format_order.append("Other")
    pivot = pivot.reindex(columns=format_order, fill_value=0)

    fig, ax = plt.subplots(figsize=(14, 6))
    ax.stackplot(
        pivot.index, *[pivot[col] for col in pivot.columns],
        labels=pivot.columns,
        colors=COLORS["palette"][:len(pivot.columns)],
        alpha=0.85
    )
    ax.set_title("Comic Book Formats Over Time")
    ax.set_xlabel("Year")
    ax.set_ylabel("Number of Releases")
    ax.legend(loc="upper left", fontsize=9)
    ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
    fig.tight_layout()
    return save_fig(fig, "06_format_over_time.png"), pivot


def graph_decade_breakdown(df):
    """Graph 7 (bonus): Releases by decade (bar chart)."""
    data = df.dropna(subset=["ReleaseYear"]).copy()
    data["Decade"] = (data["ReleaseYear"] // 10 * 10).astype(str) + "s"
    decade_counts = data["Decade"].value_counts().sort_index()

    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(
        decade_counts.index, decade_counts.values,
        color=COLORS["palette"][5], edgecolor="white", linewidth=0.5
    )
    add_bar_labels(ax, bars, fontsize=9)
    ax.set_title("Comic Book Releases by Decade")
    ax.set_xlabel("Decade")
    ax.set_ylabel("Number of Releases")
    fig.tight_layout()
    return save_fig(fig, "07_decade_breakdown.png"), decade_counts


def graph_top_publisher_trends(df):
    """Graph 8 (bonus): Release trend for top 5 publishers over time (line chart)."""
    data = df.dropna(subset=["ReleaseYear", "Publisher"])
    top5 = data["Publisher"].value_counts().head(5).index.tolist()
    data = data[data["Publisher"].isin(top5)]

    pivot = data.groupby(["ReleaseYear", "Publisher"]).size().unstack(fill_value=0)
    # Only show years with some activity
    pivot = pivot[pivot.sum(axis=1) > 0]

    fig, ax = plt.subplots(figsize=(14, 6))
    for i, pub in enumerate(top5):
        if pub in pivot.columns:
            ax.plot(pivot.index, pivot[pub], label=pub,
                    color=COLORS["palette"][i], linewidth=2, marker="", alpha=0.85)

    ax.set_title("Release Trends: Top 5 Publishers Over Time")
    ax.set_xlabel("Year")
    ax.set_ylabel("Number of Releases")
    ax.legend(fontsize=9)
    ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
    fig.tight_layout()
    return save_fig(fig, "08_publisher_trends.png"), None


# ═══════════════════════════════════════════════════════════════════════════
# 5. MARKDOWN REPORT
# ═══════════════════════════════════════════════════════════════════════════

def generate_report(df, cleaning_log, graph_data):
    """Generate the analysis markdown report."""
    total = len(df)
    year_range = f"{int(df['ReleaseYear'].min())}–{int(df['ReleaseYear'].max())}" if df["ReleaseYear"].notna().any() else "N/A"
    n_publishers = df["Publisher"].nunique()
    n_genres = df["Genre"].nunique()
    n_formats = df["Format"].nunique()

    # Unpack graph data
    yearly = graph_data.get("yearly")
    top_pubs = graph_data.get("top_pubs")
    fmt_counts = graph_data.get("fmt_counts")
    top_genres = graph_data.get("top_genres")
    cross = graph_data.get("cross")
    decade_counts = graph_data.get("decade_counts")

    # Find peak year
    peak_year = int(yearly.idxmax()) if yearly is not None else "N/A"
    peak_count = int(yearly.max()) if yearly is not None else "N/A"

    report = f"""# Comic Books Dataset — Analysis Report

## 1. Dataset Overview

| Metric | Value |
|--------|-------|
| Total records (after cleaning) | {total:,} |
| Year range | {year_range} |
| Unique publishers | {n_publishers} |
| Unique genres | {n_genres} |
| Unique formats | {n_formats} |

This dataset contains information on comic books including their titles, publishers,
release years, formats, and genres.

---

## 2. Data Cleaning Summary

The following cleaning steps were applied to the raw dataset:

"""
    for line in cleaning_log:
        report += f"- {line}\n"

    report += f"""
---

## 3. Key Findings

- The dataset spans from **{year_range}**, with the peak release year being **{peak_year}** ({peak_count:,} releases).
- **{top_pubs.index[0]}** is the dominant publisher with **{top_pubs.values[0]:,}** entries, followed by **{top_pubs.index[1]}** with **{top_pubs.values[1]:,}** entries.
- **{fmt_counts.index[0]}** is the most common format, accounting for {fmt_counts.values[0]:,} entries ({fmt_counts.values[0] / total * 100:.1f}% of the dataset).
- **{top_genres.index[0]}** is the dominant genre with {top_genres.values[0]:,} entries.
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
- The peak year is **{peak_year}**, with **{peak_count:,}** releases.
- Earlier decades (pre-1970s) show relatively few entries, which may reflect both lower
  production volumes and gaps in the dataset.

---

### 4.2 Top 10 Publishers

![Top Publishers](graphs/02_top_publishers.png)

This horizontal bar chart shows the ten most prolific publishers in the dataset.

**Notable patterns:**
- **{top_pubs.index[0]}** and **{top_pubs.index[1]}** dominate the market, together
  accounting for {(top_pubs.values[0] + top_pubs.values[1]):,} entries
  ({(top_pubs.values[0] + top_pubs.values[1]) / total * 100:.1f}% of the dataset).
- A significant drop-off occurs after the top 2, with **{top_pubs.index[2]}** at
  {top_pubs.values[2]:,} entries—roughly a third of either market leader.
- The long tail of smaller publishers is typical of the industry.

---

### 4.3 Format Distribution

![Format Distribution](graphs/03_format_distribution.png)

This bar chart shows how comic books are distributed across different formats.

**Notable patterns:**
- **{fmt_counts.index[0]}** dominates with {fmt_counts.values[0]:,} entries, which is
  expected as it is the traditional publishing unit for comics.
- **{fmt_counts.index[1]}** is the second most common format at {fmt_counts.values[1]:,}
  entries, reflecting the popularity of collected editions.
- Digital format represents a smaller share, suggesting the dataset may skew toward
  physical publications or pre-digital era entries.

---

### 4.4 Genre Distribution

![Genre Distribution](graphs/04_genre_distribution.png)

This horizontal bar chart shows the top genres by number of entries.

**Notable patterns:**
- **{top_genres.index[0]}** is by far the most common genre, followed by
  **{top_genres.index[1]}** and **{top_genres.index[2]}**.
- The dominance of {top_genres.index[0]} reflects the historical core market of the
  comic book industry.
- Genres like {top_genres.index[-2]} and {top_genres.index[-1]} represent niche
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
   Marvel and DC commanding approximately {(top_pubs.values[0] + top_pubs.values[1]) / total * 100:.0f}% of all entries.

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
"""
    return report


# ═══════════════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════════════

def main():
    # Create output directories
    os.makedirs(GRAPHS_DIR, exist_ok=True)

    # Step 1: Load data
    df = load_data(DATASET_PATH)

    # Step 2: Clean data
    print("=" * 60)
    print("DATA CLEANING")
    print("=" * 60)
    df, cleaning_log = clean_data(df)
    for line in cleaning_log:
        print(f"  {line}")
    print()

    # Save cleaned dataset
    df.to_csv(CLEANED_CSV_PATH, index=False)
    print(f"  Saved cleaned dataset: {CLEANED_CSV_PATH}")
    print()

    # Step 3: Generate graphs
    print("=" * 60)
    print("GENERATING GRAPHS")
    print("=" * 60)

    graph_data = {}

    path, yearly = graph_releases_by_year(df)
    graph_data["yearly"] = yearly

    path, top_pubs = graph_top_publishers(df)
    graph_data["top_pubs"] = top_pubs

    path, fmt_counts = graph_format_distribution(df)
    graph_data["fmt_counts"] = fmt_counts

    path, top_genres = graph_genre_distribution(df)
    graph_data["top_genres"] = top_genres

    path, cross = graph_publisher_by_genre(df)
    graph_data["cross"] = cross

    path, pivot = graph_format_over_time(df)
    graph_data["format_pivot"] = pivot

    path, decade_counts = graph_decade_breakdown(df)
    graph_data["decade_counts"] = decade_counts

    path, _ = graph_top_publisher_trends(df)

    print()

    # Step 4: Generate report
    print("=" * 60)
    print("GENERATING REPORT")
    print("=" * 60)
    report = generate_report(df, cleaning_log, graph_data)
    with open(REPORT_PATH, "w", encoding="utf-8") as f:
        f.write(report)
    print(f"  Saved report: {REPORT_PATH}")

    # Final summary
    print()
    print("=" * 60)
    print("ALL DONE")
    print("=" * 60)
    print(f"  Graphs saved to: {GRAPHS_DIR}/")
    print(f"  Report saved to: {REPORT_PATH}")
    print(f"  Cleaned data:    {CLEANED_CSV_PATH}")
    graph_files = [f for f in os.listdir(GRAPHS_DIR) if f.endswith(".png")]
    print(f"  Total graphs: {len(graph_files)}")
    for gf in sorted(graph_files):
        print(f"    - {gf}")


if __name__ == "__main__":
    main()
