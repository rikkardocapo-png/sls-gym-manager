# SLS Gym Manager

A desktop booking and membership system for a school gym, built as my
**IB Diploma Computer Science Internal Assessment** (2024–2025).

> **Status: archived.** The hosted database it used has been shut down, so the
> apps no longer connect. The code is kept here as a record of the project.

## What it does

The system is two Tkinter apps sharing one MySQL database.

**Client app (students and teachers)** — `client/`
- Account sign-up and login
- Weekly booking grid: each period holds up to 20 people, colour-coded by how
  full it is, with some periods reserved for teachers
- Medical certificate upload, with expiry tracking and warnings
- Induction-day status, plus pre-filled emails to gym staff for support or
  induction requests

**Admin app (gym staff)** — `admin/`
- Live timetable of all bookings, with each period's attendance list
- User directory: approve or delete medical certificates, mark inductions
  complete and grant teacher status
- Download uploaded certificates (stored as BLOBs)

## Tech

- Python 3, Tkinter / ttk
- MySQL (`mysql-connector-python`), first local, then hosted
- PyInstaller `.spec` files and `.icns` icons for standalone macOS builds
- Final version: database credentials Fernet-encrypted in a bundled `.env`
  (`cryptography`, `python-dotenv`), generated with `tools/maker.py`

## Repository layout

| Path | Contents |
|------|----------|
| `client/` | Student / teacher app (entry point `Student_Main.py`) |
| `admin/` | Staff app (entry point `V2.py`) |
| `tools/maker.py` | Generates the encryption key and encrypted `.env` |
| `experiments/` | Scratch scripts: connection tests, date validation, UI tests |

## History

The commit history rebuilds the project from my dated version folders,
one commit per version. The commits keep each version's original date.

| Tag | Date | Milestone |
|-----|------|-----------|
| — | Jun 2024 | Server-side prototype |
| — | Aug 2024 | First student client |
| `v0.1` | Aug 2024 | Booking grid, certificate and induction status |
| `v0.2` | Sep 2024 | Admin app and hosted database |
| `v0.3` | Oct 2024 | Final IA build, packaged as macOS apps |
| `v1.1` | Oct 2024 | Split into ADMINAPP / CLIENTAPP |
| `v1.1-smoothbeta` | Jan 2025 | UI polish, new remote database |
| `v1.2` | Jan 2025 | Online server version |
| `v1.3` | Mar 2025 | Packaged release with encrypted credentials |

Database passwords and keys that were hard-coded in early versions have been
replaced with `REDACTED` throughout the history.

## Running it

Running it needs a MySQL database with the expected schema (`Users`,
`Timetable`, `Certificates`), which is not included. Install the dependencies:

```bash
pip install mysql-connector-python cryptography python-dotenv
```

For the client, create `client/.env` from `client/.env.example` using
`tools/maker.py`, then run `python Student_Main.py` from `client/`.
