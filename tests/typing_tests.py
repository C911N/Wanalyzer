import os
from unittest import TestCase
from pathlib import Path
from subprocess import run, PIPE
from typing import List


_TYPING_ERROR_FORMAT = 'Typing test error (mypy)\n\n\n%s'


class TypingTest(TestCase):
    """Check if all sources files are type compilant"""

    def test_run_mypy(self):
        """Typing checks with mypy"""

        file_path: str = Path(__file__).parent.absolute()
        source_path: str = os.path.join(file_path, '..', 'src')
        mypy_call: List[str] = ['mypy', source_path]
        process: CompletedProcess = run(mypy_call, stdin=PIPE, stdout=PIPE, stderr=PIPE, universal_newlines=True)
        to_print: str = process.stdout if process.stdout != '' else process.stderr
        
        # Test the output
        self.assertEqual(process.returncode, 0, _TYPING_ERROR_FORMAT % (to_print))
