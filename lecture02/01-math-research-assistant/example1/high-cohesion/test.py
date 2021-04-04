from file_repo import FileRepoABC
from file_processor import FileProcessor


class TestFileProcessor(TestCase):
    def test_run(self):
        mock_repo = mock.Mock(spec=FileRepoABC)
        mock_repo.get_files.return_value = [BytesIO(b"foo"), BytesIO(b"bar")]
        fp = FileProcessor(mock_repo, "some/path")
        results = fp.run()
        self.assertEqual(results, ["acbd18db4cc2f85cedef654fccc4a4d8",
                                   "37b51d194a7513e45b56f6524f2d51f2"])
