---
name: email-structure-guardrail
description: Structure cold or warm outreach emails and networking messages into Hook, Proof, Pivot, and one final time-boxed CTA. Use when drafting outreach to prospects, recruiters, or partners, restructuring a messy outreach draft, or checking its information order. This is a structure guard, used alongside the sender's voice and factual evidence, rather than a campaign or sending tool.
---

# Email Structure Guardrail

Make the recipient understand who is writing, why the contact is relevant, what supports the approach, and what one response is requested. Use the four stages below for new outreach and outreach rewrites. This structure is a preference; do not claim that it guarantees higher reply rates.

## Before Drafting

1. Identify the actual sender, recipient, language, trigger, supported proof, current intent, and requested next step. Use supplied context and authorized sources before asking for missing decisions. Never manufacture a referral, achievement, metric, market need, availability, or deadline. Use a concrete deliverable when no metric is available. For missing material facts, ask a focused question or use clearly marked placeholders in an explicitly provisional draft.
2. Run the recipient check before drafting or creating any external draft: compare names in the text with To, Cc, Bcc, the company domain, thread, and known contact record. On a mismatch, show the name, address, and inconsistency, ask one confirmation question, and stop before drafting. Never guess a replacement address. For generic addresses, state outside the copy that the name could not be checked; disclose plausible initials or short forms accepted. If no address was supplied, do not invent one or claim it was verified. A text-only draft may use the supplied recipient context, but verify the address before any external draft or send.
3. Load the applicable speaker and language rules from the current tone repository, then the actual `content-humanizer` skill. Use the sender's own current voice references, language rules, examples, and known writing preferences. If they maintain a tone repository, verify its freshness without overwriting local changes. This download does not bundle a personal tone repository or the separate `content-humanizer` skill. If a required voice or humanizer cannot be accessed, report the missing dependency and request its location or permission for a fallback.
4. Preserve the current explicit brief. This skill's strict outreach format overrides general defaults allowing courtesies or a signature after the CTA. Do not apply it to ordinary replies, logistics, cover letters, or application fields unless specifically asked. If a newer explicit request changes the format, follow it and identify the exception outside the copy rather than claiming strict conformance.

## Write Four Body Paragraphs in This Order

1. **Hook (identity + relevance): one or two sentences.** State who the sender is and the concrete trigger or warm relevance. Start directly; omit generic conversational filler, invented familiarity, and rhetorical opening questions. Use a supplied greeting on its own line only when requested, outside the four body paragraphs.
2. **Proof (capability + market fit): one paragraph.** Group supported track record, relevant metrics and technical deliverables, connecting them to the recipient's actual context. Include only evidence that supports this approach. Dense means concentrated evidence, not a long resume dump, jargon, bullets, or an unreadable sentence. Preserve qualifications and causation accurately.
3. **Pivot (status + intent): exactly one sentence.** Connect that evidence to what the sender seeks now. Do not repeat the introduction, invent a career transition, or hide an additional request here.
4. **Single CTA (low-friction close): exactly one question in one sentence.** Ask for one proportionate action with a bounded duration or response window. Use supplied logistics; otherwise ask for them or put `[DURATION]` or `[TIMEFRAME]` in a provisional draft. A proposed duration is a request, never a claim that a meeting is booked. Do not invent the sender's availability or impose artificial urgency. Never turn a simple networking request into an unasked meeting. Multiple purposes for one conversation are acceptable; independently answerable actions such as booking a call and reviewing a CV are two asks, even with one question mark.

End the email body on that question mark. Add no sign-off, signature, postscript, attachment explanation, profile-sharing permission, or new fact after it. If a sending surface appends a mandatory footer or signature, flag that limitation outside the copy; never claim the rendered message ends on the question without checking it.

## Review and Validate

Apply the actual content-humanizer pass while preserving facts, the four stages, and the single ask. Remove filler such as “I hope this finds you well”, “I hope you are having a good week”, and “I wanted to reach out”. Never use an em dash. Keep the tone thoughtful, specific, and natural, like a senior operator explaining a relevant reason to talk.

Read [review.md](references/review.md) for the semantic review and test scenarios before finalizing. For English body-only drafts, run the bundled structural linter when a local shell is available:

```bash
python3 scripts/check_structure.py /path/to/body.txt
python3 scripts/test_structure.py
```

Resolve linter errors, then manually verify stage meaning, evidence, recipient fit, and that there is only one requested action. Run the selected voice's required language checker too. The linter checks observable form, not truth, recipient identity, persuasion, or semantic CTA count. Its sentence parsing is an English heuristic; review abbreviations and other languages manually. Never silently translate to satisfy it. Without a shell, perform the same review manually and do not claim a script ran.

Return one ready-to-use draft by default, without stage labels, analysis, or a process log. Put a requested subject and any necessary qualification before the copy, clearly outside the four-paragraph body. Do not append commentary after the final question. This skill drafts text only; it does not authorize creating drafts in an app or sending messages.
