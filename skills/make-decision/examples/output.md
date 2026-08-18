# Decide Whether To Build Scheduled Sending Now

Decision: Should the team build scheduled message sending in the next feature batch or defer it?

## 1. Decision To Make

Use this worksheet to decide whether scheduled sending should enter the next feature batch or wait until the core messaging flow is more mature.

## 2. Background

Users sometimes want to write a message now and send it later, but the current product requires them to remember and come back manually. The feature is useful and easy to understand, but it adds delivery-state complexity that could distract from current reliability work.

## 3. Options

| Criteria | Option 1: Build scheduled sending now | Option 2: Defer scheduled sending |
|:-|:-|:-|
| Customer value | :green_circle: High. Gives users a clear new ability inside the existing message flow. | :red_circle: Low. Leaves the current reminder-based workaround in place. |
| Delivery risk | :red_circle: High. Failure, edit, and cancellation states introduce significant delivery uncertainty. | :green_circle: Low. Adds no new delivery path and keeps the team focused on known reliability work. |
| Scope expansion risk | :yellow_circle: Medium. The first version can stay narrow, but recurring and bulk sending are likely follow-on pressures. | :green_circle: Low. Deferring removes the immediate risk of scope expanding during the batch. |

## 4. Recommendation

Build scheduled sending now as a narrow first version. It has clear customer value and can stay contained if the team limits scope to one-time scheduled messages. The main risk is delivery-state complexity; this recommendation should change if the team cannot define failure, edit, and cancellation behavior before build starts.
