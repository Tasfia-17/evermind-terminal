import re

# Patterns that indicate sensitive data — redact before sending to EverMemOS
_PATTERNS = [
    r'(?i)(password|passwd|secret|token|api[_-]?key|auth)[^\s]*\s*[=:]\s*\S+',
    r'(?i)(aws_secret|aws_access)[^\s]*\s*[=:]\s*\S+',
    r'[A-Za-z0-9+/]{40,}={0,2}',   # long base64-like strings (keys/tokens)
    r'(?<!\d)\d{16,}(?!\d)',         # long numeric strings (card numbers etc.)
]

_COMPILED = [re.compile(p) for p in _PATTERNS]


def redact(text: str) -> str:
    """Redact sensitive values from text before storing in EverMemOS."""
    for pattern in _COMPILED:
        text = pattern.sub('[REDACTED]', text)
    return text
