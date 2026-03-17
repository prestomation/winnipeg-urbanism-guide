# CLAUDE.md — Winnipeg Urbanism Guide

A practical reference guide for urbanists and advocates in Winnipeg, Manitoba, Canada. Built with Hugo and the hugo-book theme.

## Project Purpose

Help Winnipeg residents understand urbanism terminology, the city's planning frameworks, transit infrastructure, housing policy, and how to participate in shaping the city's future.

## Tech Stack

- **Static site generator:** Hugo 0.147.0 (extended) with the hugo-book theme
- **Deployment:** GitHub Actions → gh-pages branch
- **Search:** Pagefind (runs post-build)
- **Theme:** `themes/hugo-book` (cloned separately — read-only; override via `layouts/` or `static/`)

## Content Organization

```
content/
  _index.md           # Homepage
  quick-start/        # Government structure and planning framework
    _index.md
  glossary/           # Urban planning terminology (4 category files)
    _index.md
    housing-zoning.md
    transportation.md
    land-use.md
    funding-policy.md
  guides/             # In-depth topic guides
    _index.md
    walkability.md
    public-transit.md
    housing.md
    bike-network.md
  timeline/           # Reverse-chronological key events
    _index.md
  data/               # Public data sources directory
    _index.md
  blog/               # Analysis and commentary
    _index.md
data/
  timeline.yaml       # Timeline data (reverse-chronological, validated)
layouts/shortcodes/
  timeline.html       # Renders data/timeline.yaml
  blog-list.html      # Lists blog posts
  columns.html        # Two-column layout helper
scripts/
  validate-timeline.py      # Checks timeline.yaml is reverse-chronological
  check-external-links.py   # Validates all external URLs
```

## Critical Rules

1. **Every factual claim requires a source link.** No unsourced statements.
2. **Verify URLs before adding.** Use WebFetch to confirm the URL is valid and the content matches.
3. **Timeline must stay reverse-chronological.** The `validate-timeline.py` script checks this before build.
4. **Theme is read-only.** Override only via `layouts/` or `static/` directories.
5. **Draft content:** Use `draft: true` in front matter for work-in-progress pages.

## Essential Commands

```bash
hugo server -D                          # Local preview with drafts
python3 scripts/validate-timeline.py    # Check timeline order
python3 scripts/check-external-links.py # Validate all URLs
```

## Winnipeg Context

- **Population:** ~780,000 (city), ~880,000 CMA (2021 Census)
- **Area:** 464 km² (179 sq mi)
- **Density:** ~1,684/km² (~4,360/sq mi)
- **Walk Score:** 48 (city average)
- **Government:** Mayor + 15 councillors (ward-based, 4-year terms) under the City of Winnipeg Charter
- **Transit:** Winnipeg Transit; BLUE BRT Line (Southwest Transitway)
- **Planning docs:** OurWinnipeg 2045 + Complete Communities Direction Strategy 2.0
- **Key development:** True North Square, Portage Place redevelopment ($650M)
- **Key zoning update:** Infill Housing By-law (2025), full zoning by-law rewrite targeting 2027

## Primary Source Domains

- winnipeg.ca (City of Winnipeg)
- winnipegtransit.com / info.winnipegtransit.com
- engage.winnipeg.ca
- bikewinnipeg.ca
- freepressnews.ca / winnipegfreepress.com
- cbc.ca/news/canada/manitoba

## Secondary Sources

- yesinwpg.com (YIMBY Winnipeg)
- walkscore.com
- census.gc.ca / statcan.gc.ca
- canada.ca (federal programs)

## Content Standards

- Use Canadian English spelling (neighbourhood, colour, centre, etc.)
- Date format: "Month Day, Year" (e.g., "April 12, 2020")
- Distances in kilometres; areas in km²
- Include a "Last updated" line at the bottom of each substantive page
- Use `### Term Name` (h3) for glossary entries, with **Why it matters:** and **Learn more:** on each entry
