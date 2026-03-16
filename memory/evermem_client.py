import os
import uuid
import requests
from datetime import datetime, timezone
from typing import Optional
from .privacy_filter import redact

EVERMEM_BASE = os.getenv("EVERMEM_BASE_URL", "http://localhost:1995/api/v1")


class EverMemClient:
    """
    Thin wrapper around the EverMemOS Memory API.
    Uses the sender field as the project/user scoping key.
    """

    def __init__(self, base_url: str = EVERMEM_BASE):
        self.base_url = base_url.rstrip("/")
        self.memories_url = f"{self.base_url}/memories"

    def _post_message(self, content: str, sender: str, group_id: Optional[str] = None,
                      group_name: Optional[str] = None, role: str = "user") -> dict:
        """Store a single message into EverMemOS."""
        safe_content = redact(content)
        payload = {
            "message_id": str(uuid.uuid4()),
            "create_time": datetime.now(timezone.utc).isoformat(),
            "sender": sender,
            "sender_name": sender,
            "role": role,
            "content": safe_content,
        }
        if group_id:
            payload["group_id"] = group_id
            payload["group_name"] = group_name or group_id

        resp = requests.post(self.memories_url, json=payload, timeout=10)
        resp.raise_for_status()
        return resp.json()

    def store(self, content: str, project_id: str) -> dict:
        """Store an episodic memory scoped to a project."""
        return self._post_message(content, sender=project_id, group_id=project_id,
                                  group_name=f"project:{project_id}")

    def search(self, query: str, project_id: str, top_k: int = 3) -> list[str]:
        """
        Search memories for a project. Returns a list of content strings.
        Uses hybrid retrieval for best semantic match.
        """
        payload = {
            "query": query,
            "user_id": project_id,
            "retrieve_method": "hybrid",
            "memory_types": ["episodic_memory"],
            "top_k": top_k,
        }
        resp = requests.get(f"{self.memories_url}/search", json=payload, timeout=10)
        resp.raise_for_status()
        data = resp.json()

        results = []
        for group in data.get("result", {}).get("memories", []):
            for mem in group.get("episodic_memory", []):
                c = mem.get("content") or mem.get("summary", "")
                if c:
                    results.append(c)
        return results

    def health(self) -> bool:
        """Check if EverMemOS is reachable."""
        try:
            resp = requests.get(f"{self.base_url.replace('/api/v1', '')}/health", timeout=5)
            return resp.status_code == 200
        except Exception:
            return False
