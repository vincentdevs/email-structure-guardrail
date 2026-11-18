#!/usr/bin/env python3
"""Lint English body-only outreach structure. Semantic review remains mandatory."""
import argparse
import re
import sys
from pathlib import Path

FILLER = re.compile(
    r"\b(?:i hope (?:this finds you well|you(?: are|'re|’re) (?:having a good week|well))"
    r"|i wanted to reach out)\b", re.I
)
TIMEBOX = re.compile(
    r"\b(?:\d+|one|two|five|ten|fifteen|twenty|thirty)\s*[- ]?"
    r"(?:minute|hour|day|week)s?\b|\b(?:by|before)\s+"
    r"(?:monday|tuesday|wednesday|thursday|friday|saturday|sunday|tomorrow|noon|\d{4}-\d{2}-\d{2})\b"
    r"|\b(?:this|next)\s+(?:week|month)\b", re.I
)
PLACEHOLDER = re.compile(r"\[[^\]\n]+\]")


def sentences(text):
    # Protect decimals, domains, common abbreviations, and initials. This is not NLP.
    text = re.sub(r"(?<=\d)\.(?=\d)", "<dot>", text)
    text = re.sub(r"\b(?:Mr|Mrs|Ms|Dr|Prof|Inc|Ltd)\.",
                  lambda m: m[0].replace('.', '<dot>'), text)
    text = re.sub(r"\b(?:e\.g\.|i\.e\.|[A-Z]\.(?=\s+[A-Z]))",
                  lambda m: m[0].replace('.', '<dot>'), text)
    text = re.sub(r"\b(?:[A-Z]\.){2,}", lambda m: m[0].replace(".", "<dot>"), text)
    text = re.sub(r"(?<=\w)\.(?=\w)", "<dot>", text)
    return [s for s in re.split(r"[.!?]+(?:[\"'”’])?(?:\s+|$)", text.strip()) if s.strip()]


def check(text):
    errors = []
    text = text.strip()
    if '\u2014' in text:
        errors.append('Em dash is forbidden.')
    if FILLER.search(text):
        errors.append('Remove conversational filler.')
    if PLACEHOLDER.search(text):
        errors.append('Unresolved placeholder: draft is provisional.')
    if text.count('?') != 1 or not text.endswith('?'):
        errors.append('Body must end on its only question mark, with nothing after it.')
    parts = [p.strip() for p in re.split(r'\n\s*\n', text) if p.strip()]
    if len(parts) != 4:
        errors.append(f'Expected four body paragraphs; found {len(parts)}.')
        return errors
    if not 1 <= len(sentences(parts[0])) <= 2:
        errors.append('Hook must contain one or two sentences.')
    if len(sentences(parts[2])) != 1:
        errors.append('Pivot must contain exactly one sentence.')
    if len(sentences(parts[3])) != 1 or parts[3].count('?') != 1:
        errors.append('CTA must be exactly one question in one sentence.')
    if not TIMEBOX.search(parts[3]):
        errors.append('CTA needs a recognizable duration or response window.')
    if any(re.search(r'^\s*(?:[-*]|\d+[.)])\s', p, re.M) for p in parts):
        errors.append('Use body paragraphs rather than lists.')
    if any(re.match(r'^(?:hook|proof|pivot|cta|single cta)\s*:', p, re.I) for p in parts):
        errors.append('Remove stage labels from the email body.')
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('body', type=Path, help='UTF-8 English body only, no subject or greeting')
    args = parser.parse_args()
    try:
        errors = check(args.body.read_text(encoding='utf-8'))
    except (OSError, UnicodeError) as exc:
        parser.exit(2, f'Cannot read body: {exc}\n')
    for error in errors:
        print(f'FAIL: {error}')
    if not errors:
        print('PASS: structural checks only. Review facts, stage meaning, recipient, and single action manually.')
    return bool(errors)


if __name__ == '__main__':
    sys.exit(main())
