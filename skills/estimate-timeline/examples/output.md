# Launch Scheduled Messages

**tl;dr:** Launch 0612 (June 12) with one-time scheduled messages as fixed scope. Cut reminders and richer controls before moving the date; delivery-state reliability is the main risk.

## 1. Estimate Summary

1. **The project shorthand is 0612 (June 12).**

2. **The team is planning backward from a fixed launch date.**

3. **The launch date stays fixed while scope remains variable.** Hold 0612 (June 12) and cut reminders, recurring sends, bulk sends, and advanced scheduling controls before moving the date.

4. **The must-have scope covers one-time scheduled messages in the existing composer.** Users can edit or cancel before send and see a clear delivery state.

## 2. Milestones

1. **Milestone 1 locks launch scope on 0429 (April 29).** Confirm the composer entry point, schedule/edit/cancel rules, delivery states, and explicit cuts.

2. **Milestone 2 delivers a working scheduling path on 0513 (May 13).** Create, edit, cancel, and send one-time scheduled messages end to end in the core flow.

3. **Milestone 3 validates reliability on 0527 (May 27).** Check time-zone handling, send execution, cancellation timing, retries, and delivery-state accuracy.

4. **Milestone 4 begins beta rollout on 0603 (June 3).** Release to a small cohort, monitor failed sends and confusing states, and fix launch-blocking issues only.

5. **Milestone 5 launches scheduled messages on 0612 (June 12).** Ship the must-have experience with recurring sends, bulk sends, and richer controls excluded.

## 3. Risks and Scope Tradeoffs

1. **Delivery-state bugs could erode trust.** If reliability is weak after 0527 (May 27), cut reminders and polish to focus on accurate send, edit, cancel, and failure states.

2. **Scheduling controls can expand quickly.** Keep launch to one-time sends from the existing composer; defer recurring sends, bulk sends, templates, and advanced reminders.
