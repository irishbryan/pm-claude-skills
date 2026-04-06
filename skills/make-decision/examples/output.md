# Decide Whether To Defer Billing Migration

Decision: Should we move the billing migration into this cycle or defer it until next cycle?

## 1. Decision To Make

Decide whether the team should spend this cycle on the billing migration now or defer it so the current activation work can ship cleanly.

## 2. Background

The migration has real long-term value, but the vendor contract and risk review are not settled yet. At the same time, the team already has a narrow activation opportunity that is better understood and closer to launch.

## 3. Options

| Criteria | Option 1: Do it now | Option 2: Defer one cycle |
|:-|:-|:-|
| Delivery confidence | :red_circle: Low. Contract and dependency timing are still unclear. | :green_circle: High. Keeps the current cycle focused and reduces execution risk. |
| User impact this cycle | :yellow_circle: Medium. Some platform cleanup value but little immediate customer impact. | :green_circle: High. Keeps the team on the activation fix with faster customer payoff. |
| Strategic cleanup | :green_circle: High. Removes a known long-term drag. | :yellow_circle: Medium. The cleanup still matters but slips by a cycle. |

## 4. Recommendation

Defer the billing migration by one cycle. It wins on delivery confidence and near-term user impact, which matter more than cleanup value right now. The main downside is carrying the migration risk longer, so the team should use the next cycle to reduce the dependency uncertainty before revisiting the decision.
