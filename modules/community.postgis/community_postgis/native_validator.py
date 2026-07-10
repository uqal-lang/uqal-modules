from __future__ import annotations

_BLOCKED = [
    "DROP ", "TRUNCATE ", "DELETE ", "INSERT ", "UPDATE ",
    "ALTER ", "CREATE ", "GRANT ", "REVOKE ", "EXEC ",
]


def security_check(query: str) -> list[str]:
    upper = query.upper()
    return [
        f"Blocked pattern '{p.strip()}' found in query"
        for p in _BLOCKED
        if p in upper
    ]
