# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Cover Letter Crafter is a Streamlit application that generates personalized cover letters and optimizes CV profiles using the Groq LLM API. It supports bilingual output (English/French).

## Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
```

## Environment Setup

Requires `GROQ_API_KEY` - can be set via:
- Environment variable
- Streamlit secrets (`st.secrets['GROQ_API_KEY']`)

## Architecture

```
app.py                  # Main Streamlit entry point, UI logic, Groq API calls
llm_utils.py            # Prompt templates for cover letters, profiles, job analysis, translation
config/
  settings.py           # Path constants (BASE_DIR, BACKGROUND image path)
  styles.py             # Streamlit UI styling (glass morphism CSS), page config, header component
static/                 # Background images for UI
my_resume.txt           # User's resume content (loaded at runtime)
```

**Data Flow:**
1. User pastes job description in the UI
2. `app.py` combines job description with resume from `my_resume.txt`
3. Prompt templates from `llm_utils.py` structure the LLM request
4. Groq API (`meta-llama/llama-4-scout-17b-16e-instruct`) generates output
5. Results stored in `st.session_state` and displayed in UI

**Key Session State Variables:**
- `cover_letter` / `cover_letter_fr` - Generated cover letters
- `modified_resume` / `modified_resume_fr` - Optimized CV profiles
- `job_analysis` - Extracted job information
- `show_french` / `show_french_profile` - Language toggle flags

## Key Features

- **Cover Letter Generation**: Uses `cover_letter_prompt()` - generates professional cover letters matching job requirements
- **CV Profile Optimization**: Uses `profile_modifier_prompt()` - adapts profile summary to job description while preserving quantified achievements
- **Job Analysis**: Uses `job_analysis_prompt()` - extracts company name, position, requirements, skills, mission
- **French Translation**: On-demand translation of generated content via `translate_to_french()`

## Prompt Engineering

Prompts in `llm_utils.py` follow a structured format:
- Explicit template with placeholders
- Numbered guidelines for content generation
- Constraints on length, tone, and formatting
- Clear instruction to return "ONLY the [content], no additional commentary"
