# Fix broken password reset flow for SSO users

> **tl;dr:** SSO users who try to reset their password hit a dead end because the reset flow does not detect their auth method. This needs a clear error state and redirect.

## The Problem

1. **SSO users land on a password reset page that does not apply to them.** They enter their email, wait for a reset link that never arrives, and then contact Support.
2. **Support is handling these tickets weekly.** The fix is straightforward but nobody has picked it up because the issue was never clearly filed.

## What Done Looks Like

1. **SSO users see a clear message explaining they sign in through their identity provider.** The message appears after they enter their email, before they expect a reset link.
2. **The message includes a link or redirect to their SSO login page.** Users can recover on their own without contacting Support.
3. **Support ticket volume for this issue drops to near zero.** Measurable within one week of launch.

## Suggested Approach

1. **Check the user's auth method after email entry on the reset page.** If the account is SSO-only, show the redirect message instead of sending a reset link.
2. **Reuse the existing SSO detection logic from the login flow.** No new auth infrastructure needed.

## Out of Scope

1. **Reworking the full password reset flow.** Only the SSO edge case matters here.
2. **Changes to the SSO login page itself.** That is a separate concern.
