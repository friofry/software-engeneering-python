from file_processor import FileProcessor
from unittest import TestCase, mock


class TestFileProcessor(TestCase):
    def test_run_returns_md5_of_contents(self):
        with mock.patch('file_processor.storage'):
            fp = FileProcessor('some/path')
            with mock.patch.object(fp, 'bucket') as mock_bucket:
                mock_blob = mock.Mock(name='mock_blob')

                def mock_download_to_file(bytez):
                    bytez.write(b'foobarbaz')
                mock_blob.download_to_file = mock_download_to_file
                mock_bucket.list_blobs.return_value = [mock_blob]
                # WHEN
                results = fp.run()
                # THEN
                self.assertEqual(results, ['6df23dc03f9b64cc38a0fc1483df6e21'])