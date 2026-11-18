# Email Structure Guardrail

Use `$email-structure-guardrail` to draft or restructure cold or warm outreach and networking messages. Supply the sender, recipient context, actual reason for contact, supported proof, present intent, and one requested action with a duration or response window.

The skill produces four body paragraphs: Hook, Proof, Pivot, and one final question. It does not send messages. It works alongside voice, evidence, and recipient checks; missing facts remain questions or provisional placeholders.

Read [SKILL.md](SKILL.md) for execution instructions and [references/review.md](references/review.md) for semantic acceptance criteria. The script paths are relative to this folder:

```bash
python3 scripts/check_structure.py /path/to/body.txt
python3 scripts/test_structure.py
```

The linter accepts English body-only text and checks form. It cannot verify truth, recipient identity, or whether one question hides multiple requests. Other languages and ambiguous sentence boundaries require manual review. A structural pass is never complete editorial acceptance.

## Download and Install

Download this repository as a ZIP using **Code > Download ZIP**, extract it, and copy the folder into your assistant's skills directory as `email-structure-guardrail`.

The scripts need Python 3 and use only its standard library. Writing tasks also require your own voice references and the separate `content-humanizer` skill, as described in `SKILL.md`; neither dependency is included in this download.
