# Engineering Journal #003 — General DNS Lookup

**Ticket:** NSL-0003  
**Status:** Complete ✅

## Objective

Expand the MX-specific utility into a general DNS lookup tool that supports multiple record types without losing the behavior already built.

## What I Built

- Added support for A, AAAA, MX, and TXT queries.
- Accepted the requested record type as user input.
- Validated that the requested type is supported.
- Returned every published record for a successful query.
- Preserved MX preference values and added explicit Null MX handling.
- Distinguished non-existent domains from valid domains that lack the requested record type.

## Biggest Challenge

Generalizing the function meant recognizing that different DNS record types cannot always be handled identically. MX needed special interpretation, while A, AAAA, and TXT answers still needed a reliable shared path.

## What I Learned

Adding capability is not only about making a new input work. It also means preserving existing behavior, handling edge cases deliberately, and testing every branch after a change.

## Biggest Takeaway

I am beginning to think in terms of reusable program behavior instead of solving only the example directly in front of me.

## Outcome

The project progressed from a single-purpose MX script to a reusable DNS lookup utility ready for record-specific analysis.

