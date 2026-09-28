# MIT Sloan Tech Summit 2027 — sponsor pipeline

A tracker for sponsorship outreach: 66 target companies, each with a fit rationale, MIT/Sloan ties,
named contacts from public sources (with a source link for each), LinkedIn searches for finding more
people, stage, owner, ask, next step, and a ready-to-edit outreach email.

## Two ways to use it

| | Shared team tracker (recommended for the team) | GitHub Pages copy |
|---|---|---|
| Where | claude.ai artifact (link in the session / your claude.ai gallery) | `sponsors/index.html` on GitHub Pages |
| Edits | Live for everyone the artifact is shared with (Contributor access or higher) | Saved in each person's browser only |
| Sharing edits | Automatic | Data → Export JSON, then commit it as `sponsors/targets.json` and rebuild |

## 2026 data and Excel export

- Tiers follow the 2026 ladder (Platinum $25k, Gold $10k, Silver $5k, Entry $2k; 2026 called the top two Petabyte and Terabyte). Data → Sponsorship tiers shows the benefits. Update `TIER_INFO` and `BENEFITS` in `src/tracker.html` when the 2027 tiers are final.
- Each company has a **2026** status (Confirmed, Received Interest, Outreach Sent, Ghosted, Declined,
  Not approached) with last year's tier, amount and notes. The list has a 2026 column you can sort and filter.
- **Data → Export Excel** saves an .xlsx with two sheets: *Companies* (every field) and *Contacts*
  (one row per person).
- The team's 2026 tracker (contacts, emails, relationship notes, amounts) lives **only in the shared
  tracker**. It is deliberately not committed here, because this repository is public.

## Files

```
sponsors/src/tracker.html   the page source (also what's published as the shared artifact)
sponsors/targets.json       the researched target list (seed data)
sponsors/build.py           wraps the source + inlines targets.json -> sponsors/index.html
sponsors/index.html         generated; don't edit by hand
```

Rebuild after editing the source or the data: `python3 sponsors/build.py`

## About the research

- Everything was gathered from public sources in Sept 2026. Company pages could not be opened directly
  (the research ran through search-result text), so **check each contact against its source link before
  writing**. Contacts marked "verify" are older or thinly sourced.
- No email addresses were guessed or invented. Add an email only once you've confirmed it.
- 7 companies (Scale AI, Databricks, Snowflake, Perplexity, Cohere, Hugging Face, Palantir) are
  flagged **Unverified**: the fit is a starting hypothesis with no named contacts yet.
- "Warm" companies took part in the 2026 Summit or a sibling MIT Sloan conference.
- MIT requires the Student Life Office (slquestions@mit.edu) to vet companies before students ask
  them for sponsorship, and sponsorships use MIT's Sponsorship Commitment Letter & Invoice template.
  The tracker has a "Vetted" checkbox per company.

Note: if this repository is public, the GitHub Pages copy (including `targets.json`) is public too.
Keep deal notes and amounts in the shared tracker, not in committed files.
