# Launch Scheduled Messages

> **tl;dr:** Launch 0612 (June 12). This estimate looks achievable if the team protects one-time scheduled messages as fixed-time `Must` scope and treats reminders, polish, and richer controls as variable scope. The main risk is delivery-state reliability across send, edit, and cancel paths.

## Estimate Summary

- **Project MMDD:** 0612 (June 12).
- **Planning mode:** Fixed launch date.
- **Fixed time, variable scope:** Hold 0612 (June 12) and cut reminders, recurring sends, bulk sends, and advanced scheduling controls before moving the date.
- **Must-have scope:** Users can schedule one-time messages from the existing composer, edit or cancel before send, and see a clear delivery state.

## Milestones

- **Milestone 1 (Must): Lock launch scope on 0429 (April 29).** Confirm the composer entry point, schedule/edit/cancel rules, delivery states, and explicit cuts.
- **Milestone 2 (Must): Scheduling path working on 0513 (May 13).** Create, edit, cancel, and send one-time scheduled messages end to end in the core flow.
- **Milestone 3 (Must): Reliability checkpoint on 0527 (May 27).** Validate time-zone handling, send execution, cancellation timing, retries, and delivery-state accuracy.
- **Milestone 4 (Should): Beta rollout on 0603 (June 3).** Release to a small cohort, monitor failed sends and confusing states, and fix launch-blocking issues only.
- **Milestone 5 (Must): Launch scheduled messages on 0612 (June 12).** Ship the must-have experience with recurring sends, bulk sends, and richer controls excluded.

## Risks and Scope Tradeoffs

- **Delivery-state bugs could erode trust.** If reliability is weak after 0527 (May 27), cut reminders and polish to focus on accurate send, edit, cancel, and failure states.
- **Scheduling controls can expand quickly.** Keep launch to one-time sends from the existing composer; defer recurring sends, bulk sends, templates, and advanced reminders.
