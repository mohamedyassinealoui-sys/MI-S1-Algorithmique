import unittest

from mi_s1_platform.execution import evaluate_function_submission, run_python_code


class ExecutionTests(unittest.TestCase):
    def test_run_python_code_success(self):
        result = run_python_code("print('ok')")
        self.assertTrue(result.ok)
        self.assertEqual(result.stdout, "ok")

    def test_run_python_code_syntax_error(self):
        result = run_python_code("if True print('x')")
        self.assertFalse(result.ok)
        self.assertIn("Erreur de syntaxe", result.explanation_fr)

    def test_function_evaluation_success(self):
        code = "def somme_n(n):\n    return sum(range(1, n+1))"
        ok, message = evaluate_function_submission(code, [("somme_n(5)", 15)])
        self.assertTrue(ok)
        self.assertIn("Tous les tests", message)

    def test_function_evaluation_failure(self):
        code = "def somme_n(n):\n    return n"
        ok, message = evaluate_function_submission(code, [("somme_n(5)", 15)])
        self.assertFalse(ok)
        self.assertIn("Tests validés", message)


if __name__ == "__main__":
    unittest.main()

