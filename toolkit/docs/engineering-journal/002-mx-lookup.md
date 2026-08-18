# Engineering Journal #002 — MX Lookup

**Ticket:** NSL-0002  
**Status:** Complete ✅

## Objective

Build the toolkit's first working DNS feature: retrieve and display a domain's mail exchange records.

## What I Built

- Used `dnspython` to query MX records for a domain.
- Iterated through the returned DNS answers.
- Displayed mail-server hostnames together with their preference values.
- Added handling for non-existent domains and domains without published MX records.
- Investigated structured MX objects rather than treating every DNS answer as plain text.

## Biggest Challenge

The returned MX records looked printable, but they were structured objects with useful attributes such as `preference` and `exchange`. Understanding that distinction changed how I approached the data.

## What I Learned

External libraries often return richer objects than their printed output suggests. Inspecting an object's type and attributes is more dependable than assuming it behaves like a string.

## Biggest Takeaway

When unfamiliar data reaches my program, I should first learn what it is and what it exposes before deciding how to process it.

## Outcome

The toolkit can retrieve meaningful MX data and respond cleanly to common DNS failure conditions.

