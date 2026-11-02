"""Progress persistence and statistics."""

from __future__ import annotations

import json
from pathlib import Path


DEFAULT_PROGRESS = {"lessons": [], "exercises": [], "challenges": [], "goals": ""}


def load_progress(progress_file: Path) -> dict:
    if not progress_file.exists():
        return DEFAULT_PROGRESS.copy()
    with progress_file.open("r", encoding="utf-8") as file:
        data = json.load(file)
    merged = DEFAULT_PROGRESS.copy()
    merged.update(data)
    return merged


def save_progress(progress_file: Path, progress: dict) -> None:
    progress_file.parent.mkdir(parents=True, exist_ok=True)
    with progress_file.open("w", encoding="utf-8") as file:
        json.dump(progress, file, ensure_ascii=False, indent=2)


def completion_rate(progress: dict, total_lessons: int, total_exercises: int, total_challenges: int) -> float:
    completed = len(progress["lessons"]) + len(progress["exercises"]) + len(progress["challenges"])
    total = total_lessons + total_exercises + total_challenges
    return 0.0 if total == 0 else (completed / total) * 100

