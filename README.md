# Winnipeg Urbanism Guide

A practical reference for urbanists and advocates in **Winnipeg, Manitoba, Canada** — covering the policies, terminology, and history behind Winnipeg's urban character.

## About

This guide helps residents and newcomers understand the planning framework, zoning rules, transit infrastructure, and community participation opportunities that shape Winnipeg's built environment. It covers:

- **Quick Start** — City government structure and how planning decisions are made
- **Glossary** — Plain-language definitions for urban planning terms
- **Guides** — In-depth coverage of walkability, transit, housing, and cycling
- **Timeline** — Key events in Winnipeg's urban development
- **Data** — Public data sources for planning and development
- **Blog** — Analysis and commentary on Winnipeg urbanism

## Technical Setup

This site is built with [Hugo](https://gohugo.io/) (extended version 0.147.0 or later) using the [hugo-book](https://github.com/alex-shpak/hugo-book) theme.

### Local Development

```bash
git clone https://github.com/prestomation/winnipeg-urbanism-guide.git
cd winnipeg-urbanism-guide

# Install the theme
git clone --depth 1 https://github.com/alex-shpak/hugo-book themes/hugo-book

# Start local server (with drafts)
hugo server -D
```

Visit `http://localhost:1313` to preview the site.

### Validation

```bash
# Validate timeline is reverse-chronological
python3 scripts/validate-timeline.py

# Check external links
python3 scripts/check-external-links.py
```

## Contributing

See [CLAUDE.md](CLAUDE.md) for content standards, conventions, and common workflow tasks.

## License

MIT
