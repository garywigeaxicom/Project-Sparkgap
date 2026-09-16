from __future__ import annotations

import re


PROMPT_INJECTION_PATTERNS = (
    r"ignore (all|any|the) (previous|prior|system) instructions",
    r"reveal (the )?(system prompt|hidden prompt|credentials|secrets)",
    r"disclose (the )?(retrieved documents|private documents|secrets)",
)
HIGH_IMPACT_PATTERN = re.compile(
    r"(decide|determine|deny|approve|reject).{0,80}(employment|housing|education|healthcare|legal|essential services|physical safety)",
    re.IGNORECASE,
)


def classify_input(text: str) -> str | None:
    normalized = " ".join(text.lower().split())
    if any(re.search(pattern, normalized) for pattern in PROMPT_INJECTION_PATTERNS):
        return "prompt_injection"
    if HIGH_IMPACT_PATTERN.search(normalized):
        return "high_impact_decision"
    return None


def refusal(reason: str) -> str:
    if reason == "prompt_injection":
        return "I cannot reveal hidden instructions, credentials, or private retrieved content."
    return "I cannot make an autonomous high-impact decision. A qualified human reviewer must assess this case."
