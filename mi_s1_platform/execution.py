"""Execution and automatic correction utilities."""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass


@dataclass
class ExecutionResult:
    ok: bool
    stdout: str
    stderr: str
    explanation_fr: str


def explain_error(stderr: str) -> str:
    if "SyntaxError" in stderr:
        return "Erreur de syntaxe : vérifiez la structure des lignes (parenthèses, :, indentation)."
    if "NameError" in stderr:
        return "Nom inconnu : une variable ou une fonction est utilisée avant sa définition."
    if "TypeError" in stderr:
        return "Erreur de type : vérifiez les types des valeurs utilisées."
    if "ZeroDivisionError" in stderr:
        return "Division par zéro : ajoutez un test avant la division."
    return "Erreur d'exécution : relisez la logique de l'algorithme et les entrées."


def run_python_code(code: str, timeout_seconds: int = 3) -> ExecutionResult:
    process = subprocess.run(
        [sys.executable, "-c", code],
        capture_output=True,
        text=True,
        timeout=timeout_seconds,
        check=False,
    )
    ok = process.returncode == 0
    stderr = process.stderr.strip()
    return ExecutionResult(
        ok=ok,
        stdout=process.stdout.strip(),
        stderr=stderr,
        explanation_fr="" if ok else explain_error(stderr),
    )


def evaluate_function_submission(user_code: str, tests: list[tuple[str, object]]) -> tuple[bool, str]:
    harness = "import json\nresults = []\n" + user_code.strip() + "\n"
    for expr, expected in tests:
        harness += f"\nresults.append(({expr}) == {expected!r})"
    harness += "\nprint(json.dumps(results))"

    result = run_python_code(harness)
    if not result.ok:
        return False, f"{result.stderr}\n{result.explanation_fr}".strip()

    try:
        checks = json.loads(result.stdout.splitlines()[-1])
    except (json.JSONDecodeError, IndexError):
        return False, "La correction automatique n'a pas pu analyser la sortie."

    if all(checks):
        return True, "Tous les tests sont validés."
    return False, f"Tests validés: {sum(checks)}/{len(checks)}."
