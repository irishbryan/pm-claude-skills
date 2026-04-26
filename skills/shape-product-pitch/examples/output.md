# Schedule Messages for Later

> **tl;dr:** People sometimes know what they want to send before they know the right time to send it. Scheduled sending lets them compose a message now and deliver it later without relying on reminders or manual follow-up.

## The Problem

1. **Users rely on memory to send later.** They draft notes, set separate reminders, or leave messages unsent until the right moment.
2. **Manual follow-up creates avoidable misses.** Time-sensitive messages can be forgotten, sent late, or sent at inconvenient hours.
3. **The workaround is outside the message flow.** Users have to coordinate between the messaging app, calendar, and reminder tools.

**Why now:** Scheduling is a common expectation in communication tools, and it fits naturally into the existing compose flow.

## The Solution

**Approach:** Add a lightweight scheduling option to the message composer.

1. **Let users choose a send time before posting.** The scheduled message stays visible and editable until delivery.
2. **Show scheduled messages in one predictable place.** Users can review, edit, send now, or cancel before the scheduled time.
3. **Confirm delivery state clearly.** The app should make it obvious whether a message is scheduled, sent, failed, or canceled.

**Constraints:**

1. **Fit this into a small feature batch.** Keep the first version narrow enough to ship without platform-level changes.
2. **Reuse existing composer patterns.** Avoid introducing a separate scheduling surface.

## What Success Looks Like

1. **Users schedule messages without leaving the composer.** The flow should feel like a small extension of sending, not a separate planning tool.
2. **Scheduled messages are easy to manage.** Users can find and change pending messages without searching through threads.

## Risks and Open Questions

1. **Delivery failure behavior needs definition.** The team should decide how retries, offline states, and notification failures appear to users.

## Out of Scope

1. **Recurring scheduled messages are excluded.** Repetition adds complexity beyond the first version.
2. **Campaign or bulk messaging is excluded.** This pitch is for individual user-composed messages only.
