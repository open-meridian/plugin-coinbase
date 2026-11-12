"""What this version declares beside its role (W8.1, W4.1; contracts v18 and v19).

**Its catalogue** (spec/the-lake, "The catalogue"; the plan's Q5 and Q21),
declared from code and read the same way at registration and by `meridian
plugin upload`:

- `daily`: each product's close and bar for a UTC day, its day ending at
  00:00 UTC (`day_time_zone` `Etc/UTC`, `day_end_minute` 0, as the plan
  rules for a venue with no official close), pulled for what the lake
  wants and pushed for a standing want; kept.
- `live`: the last trade's price and the best bid and offer as prices, at
  most once a second per subject and kind, pulled for the latest or kept
  current for a standing want; and from contract v19 the best bid and offer
  with their sizes as a quote, kept current from the venue's stream while a
  standing want stands.
- `trades` (contract v19): every trade, from the venue's stream for the
  subjects under a standing want, or from its REST history for a range
  wanted; declared apart from the live prices, so an admin licenses and
  keeps them apart (the plan's Q40).

**Its terms and pricing** (contract 30, ruling 1032): no dataset declares a
licence. Each describes Coinbase's Market Data Terms in plain words
(`TERMS`): an organisation may use and display the data within itself, and
needs Coinbase's written consent to redistribute it, display it outside, or
build applications for other end users (README, "Coinbase's terms"; not
legal advice). The deployment admin sets the deployment's licence on the
Data sources page, which is the one enforced.

**How a gap is recovered** (W10.14): `daily` and `trades` are `backfill` --
Coinbase serves candles and trades back in time, and a want of a range is
answered from them; `live` is `stream_only` -- a ticker or a book as it
stood is not served again. No dataset names a sessions calendar: Coinbase
trades around the clock.

`venue_id` is empty: the venue master's ID for Coinbase Exchange is minted by
the platform, not known to the code a catalogue is declared from, so each row
names the venue by the ID it resolves at run time (the SDK's
`meridian.roles.data.pairs.Feed`), and the
catalogue names none (README, "The venue").

**Its storage**: one kind of raw record, Coinbase's responses as received,
kept a month by default (`KIND`, kept by the SDK's
`meridian.edge.RawStore`); the SDK declares the kind's two window settings.
**Its settings**: sample data, a developer's (synthetic.py). No secret:
Coinbase's public market data needs no key.
"""

import meridian
from meridian import DatasetDeclaration

VENDOR = "Coinbase"
SAMPLE_DATA = "sample_data"

#: Its one kind of raw record, Coinbase's responses as received: a month of
#: them by default, enough to re-convert a row a person questions. An admin
#: sets the window in Settings.
KIND = "responses"
LABEL = "Raw responses"
WINDOW_DAYS = 30

#: Its settings, in the data role's order (spec/plugin-pages-follow-their-role):
#: no environment and no credential -- Coinbase's public market data has one
#: environment and needs no key -- so only sample data, a developer's.
SETTINGS = [
    meridian.sample_data(
        description=(
            "Answer from built-in made-up Coinbase responses, or a developer's recorded ones, "
            "instead of calling Coinbase. Development deployments only."
        )
    ),
]

#: Coinbase's published terms, in plain words (ruling 1032): the same for each
#: dataset, all from Coinbase Exchange's public market data.
TERMS = (
    "Coinbase Exchange's public market data (REST and WebSocket feed): free, no key or account. "
    "Coinbase's Market Data Terms let an organisation use and display it within itself. "
    "Without Coinbase's written consent they forbid redistributing it or displaying it "
    "outside the organisation, and building applications for other end users with it."
)

CATALOGUE = [
    DatasetDeclaration(
        key="daily",
        vendor=VENDOR,
        data_types=["meridian.v1.Price", "meridian.v1.Bar"],
        modes=["pull", "push"],
        cadence=86_400,
        history=0,
        terms_and_pricing=TERMS,
        gap_recovery="backfill",
        day_time_zone="Etc/UTC",
        day_end_minute=0,
    ),
    DatasetDeclaration(
        key="live",
        vendor=VENDOR,
        data_types=["meridian.v1.Price", "meridian.v1.Quote"],
        modes=["pull", "stream"],
        cadence=1,
        history=0,
        terms_and_pricing=TERMS,
        gap_recovery="stream_only",
        day_time_zone="Etc/UTC",
        day_end_minute=0,
    ),
    DatasetDeclaration(
        key="trades",
        vendor=VENDOR,
        data_types=["meridian.v1.Trade"],
        modes=["pull", "stream"],
        cadence=1,
        history=0,
        terms_and_pricing=TERMS,
        gap_recovery="backfill",
        day_time_zone="Etc/UTC",
        day_end_minute=0,
    ),
]
