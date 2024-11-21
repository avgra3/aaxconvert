import unittest
from aaxconvert.conversion import _path_to_ffmpeg, _get_name, run_ffmpeg


class TestConversion(unittest.TestCase):
    def test_path_to_ffmpeg(self):
        path = _path_to_ffmpeg()
        expected_path = "/usr/bin/ffmpeg"
        self.assertEqual(path, expected_path)

    def test_path_to_ffmpeg_raises(self):
        pass

    def test_get_name(self):
        # File exists -- only passes when ran from project root directory
        expected = ("README", ".md")
        tested = _get_name("README.md")
        self.assertTupleEqual(tested, expected)

    def test_get_name_raises(self):
        # File does not exist
        invalid_file = "DOESNOTEXIST"
        with self.assertRaises(SystemExit):
            _get_name(invalid_file)

    def test_run_ffmpeg_raises(self):
        file_path = "README.md"
        with self.assertRaises(Exception):
            run_ffmpeg(filepath=file_path, activation_bytes="TEST")


if __name__ == "__main__":
    unittest.main(verbosity=2)
