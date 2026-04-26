# Decide Whether To Build Scheduled Sending Now

Decision: Should the team build scheduled message sending in the next feature batch or defer it?

## 1. Decision To Make

Use this worksheet to decide whether scheduled sending should enter the next feature batch or wait until the core messaging flow is more mature.

## 2. Background

Users sometimes want to write a message now and send it later, but the current product requires them to remember and come back manually. The feature is useful and easy to understand, but it adds delivery-state complexity that could distract from current reliability work.

## 3. Options

| Criteria | Option 1: Build scheduled sending now | Option 2: Defer scheduled sending |
|:-|:-|:-|
| Customer value | :green_circle: High. Gives users a clear new ability inside the existing message flow. | :yellow_circle: Medium. Avoids complexity, but leaves the current reminder-based workaround in place. |
| Delivery confidence | :yellow_circle: Medium. The basic composer flow is straightforward, but failure states need definition. | :green_circle: High. Keeps the team focused on known messaging reliability work. |
| Scope control | :yellow_circle: Medium. The first version can stay narrow if recurring and bulk sending are excluded. | :green_circle: High. Deferring removes the risk of scope expanding during the batch. |

## 4. Recommendation

Build scheduled sending now as a narrow first version. It has clear customer value and can stay contained if the team limits scope to one-time scheduled messages. The main risk is delivery-state complexity; this recommendation should change if the team cannot define failure, edit, and cancellation behavior before build starts.
