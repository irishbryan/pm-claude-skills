# Improve Trial-to-Activation Handoff

> **tl;dr:** New self-serve users are falling out before they reach value because the handoff from signup to setup is fragmented. Tightening that path should improve activation without a full onboarding rewrite.

## The Problem

- **New users hit too many setup dead ends in the first session.** They have to piece together guidance from email, docs, and the app itself.
- **The current flow makes the first success hard to reach quickly.** Support can recover some users manually, but the product path is weak on its own.
- **The status quo keeps activation lower than it should be.** We are spending support effort where product clarity should be doing the work.

The problem appears early and repeatedly for self-serve users evaluating the product on their own.

**Why now:** The team already has activation work in flight, and this is the clearest bottleneck in the current cycle.

## The Solution

**Approach:** Ship a narrow onboarding improvement focused on the first critical setup step and clearer recovery paths when users get stuck.

1. **Guide users through the first required setup action.** Reduce ambiguity and shorten the path to first value.
2. **Add clearer recovery points when users fail.** Make the next step obvious instead of forcing users into docs or support.
3. **Instrument the drop-off points before launch.** Make sure the team can tell whether the change worked.

**Constraints:**

1. **This must fit inside the current cycle.** The team cannot absorb a full onboarding rewrite right now.
2. **The work must reuse existing auth and setup primitives.** New platform work would expand scope too much.

**Appetite:** 2-week batch.

## What Success Looks Like

1. **More trial users reach the first successful setup step.** The team can observe a better activation trend within the first week after launch.
2. **Support sees fewer onboarding rescue requests.** The volume should drop for the failure modes this pitch targets.

## Out of Scope

- **A complete redesign of onboarding.** That would exceed the appetite for this cycle.
- **Lifecycle email strategy changes.** This pitch focuses on the in-product path only.
