# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

**Local Development:**
```bash
python app.py  # Runs Flask development server on port 5000
```

**Production (Heroku):**
```bash
gunicorn app:app  # Production WSGI server (configured in Procfile)
```

**Deployment:**
```bash
git push heroku main  # Deploy to Heroku
```

## Architecture

This is a Flask-based single-page website for Burnt Leaf Cigars, a cigar lounge in Baltimore/Randallstown, MD.

### Key Components

1. **app.py** - Main Flask application with single route serving index.html
2. **templates/index.html** - Single page with four sections (Home, About, Events, Contact) and embedded Instagram feed
3. **static/styles.css** - Responsive design with video backgrounds, gold (#ffd700) accent color, Playfair Display font
4. **static/videos/** - Background and promotional videos (video-heavy design)
5. **igdowloader.py** - Utility script using yt-dlp for downloading Instagram content

### Technology Stack
- **Backend:** Flask 3.1.0 (Python 3.9.16)
- **Frontend:** Vanilla HTML/CSS/JavaScript with smooth scroll navigation
- **Deployment:** Heroku with Gunicorn
- **No testing framework** - Simple marketing site without tests

### Important Notes
- Video-heavy design may impact load times
- Instagram feed uses direct iframe embed (could break if service changes)
- No configuration management - values are hardcoded
- Single page design limits SEO opportunities
- Missing .gitignore file (should exclude .DS_Store files)