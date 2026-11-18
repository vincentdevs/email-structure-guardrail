#!/usr/bin/env python3
"""Regression tests using synthetic outreach, never real recipient data."""
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from check_structure import check

BODY = (
    "I am Morgan Lee, a CRM consultant, writing about your request for migration help.\n\n"
    "I built a deduplication workflow for a software sales team, which fits the record cleanup you described.\n\n"
    "I am now seeking another migration project where I can apply that work.\n\n"
    "Would a 15-minute conversation help us define the migration scope?"
)


class StructureTests(unittest.TestCase):
    def test_valid_body(self):
        self.assertEqual(check(BODY), [])

    def test_two_sentence_hook(self):
        self.assertEqual(check(BODY.replace('I am Morgan Lee, a CRM consultant, writing',
                                           'I am Morgan Lee, a CRM consultant. I am writing')), [])

    def test_multiline_wrapping(self):
        self.assertEqual(check(BODY.replace('CRM consultant, writing', 'CRM consultant,\nwriting')), [])

    def test_decimal_and_abbreviation(self):
        text = BODY.replace('I am Morgan Lee', 'I am Dr. Morgan Lee')
        text = text.replace('another migration project', 'another U.S. migration project worth 2.5 million')
        self.assertEqual(check(text), [])

    def test_response_window(self):
        text = BODY.rsplit('\n\n', 1)[0] + '\n\nCould you confirm permission to connect by Friday?'
        self.assertEqual(check(text), [])

    def test_spelled_duration(self):
        self.assertEqual(check(BODY.replace('15-minute', 'fifteen minute')), [])

    def test_reject_bad_forms(self):
        cases = {
            'empty': '',
            'three paragraphs': BODY.replace('\n\n', ' ', 1),
            'long hook': BODY.replace('I am Morgan', 'Hello. Another sentence. I am Morgan'),
            'two-sentence pivot': BODY.replace('I am now seeking', 'My project ended. I am now seeking'),
            'two questions': BODY.replace('I am now seeking', 'Can you help? I am now seeking'),
            'signature': BODY + '\n\nMorgan',
            'inline signature': BODY + '\nMorgan',
            'postscript': BODY + '\n\nP.S. My portfolio is attached.',
            'em dash': BODY.replace('consultant, writing', 'consultant\u2014writing'),
            'filler': BODY.replace('I am Morgan', 'I hope this finds you well. I am Morgan'),
            'filler week': BODY.replace('I am Morgan', 'I hope you are having a good week. I am Morgan'),
            'filler reach out': BODY.replace('I am Morgan', 'I wanted to reach out. I am Morgan'),
            'placeholder': BODY.replace('Morgan Lee', '[NAME]'),
            'unbounded CTA': BODY.replace('15-minute', 'brief'),
            'two-sentence CTA': BODY.replace('Would a', 'Let us talk. Would a'),
            'stage labels': 'Hook: ' + BODY,
            'bulleted proof': BODY.replace('I built', '- I built'),
        }
        for label, text in cases.items():
            with self.subTest(label=label):
                self.assertTrue(check(text))

    def test_documented_semantic_limit(self):
        # One question can contain two actions. A structural pass must never
        # be presented as semantic acceptance; the reference requires rejection.
        text = BODY.rsplit('\n\n', 1)[0] + '\n\nCould we speak for 15 minutes and could you review my CV?'
        self.assertEqual(check(text), [])

    def test_cli_exit_codes(self):
        script = Path(__file__).with_name('check_structure.py')
        with tempfile.TemporaryDirectory() as tmp:
            body = Path(tmp) / 'body.txt'
            for text, code in ((BODY, 0), (BODY + '\nMorgan', 1)):
                body.write_text(text, encoding='utf-8')
                run = subprocess.run([sys.executable, str(script), str(body)], capture_output=True, text=True)
                self.assertEqual(run.returncode, code, run.stderr)
            run = subprocess.run([sys.executable, str(script), str(Path(tmp) / 'missing')], capture_output=True)
            self.assertEqual(run.returncode, 2)


if __name__ == '__main__':
    unittest.main(verbosity=2)
