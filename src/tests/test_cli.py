from aaxconvert.cli import main
from click.testing import CliRunner
import unittest


class TestCli(unittest.TestCase):
    def test_convert_activation_bytes_raises(self):
        runner = CliRunner()
        result = runner.invoke(main, ["convert", "README.md", None])
        assert result.exit_code != 0


if __name__ == "__main__":
    unittest.main(verbosity=2)
