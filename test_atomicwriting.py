import unittest
from atomicwriting import atomicwriting


class TestAtomicwriting(unittest.TestCase):
    def test_writing_0(self):
        content = "Yingtong Miao\nTammy"
        res = atomicwriting("writingfile.txt", content)
        self.assertEqual(res, content)

    def test_writing_1(self):
        content = "Yingtong Miao\nTammy"
        res = atomicwriting(r"C:\Users\Lenovo\Desktop\test.txt", content)
        self.assertEqual(res, content)

    def test_writing_2(self):
        content = "Yingtong Miao\nTammy"
        res = atomicwriting("C:\\Users\\Lenovo\\Desktop\\test.txt", content)
        self.assertEqual(res, content)
        
    def test_notstring_0(self):
        res = atomicwriting(11, 6)
        self.assertEqual(res, "File name is not string.")

    def test_notstring_1(self):
        res = atomicwriting("writingfile.txt", 6)
        self.assertEqual(res, "Writing contents are not string.")
        
    def test_null_0(self):
        res = atomicwriting("", "")
        self.assertEqual(res, "File name is empty.")

    def test_null_1(self):
        res = atomicwriting("writingfile.txt", "")
        self.assertEqual(res, "Writing contents are empty.")
        
#     File path is incorrect. Current path does not have "file" folder.
#     def test_filename_0(self):
#         res = atomicwriting("file\writingfile.txt", "Yingtong Miao\nTammy")
#         self.assertEqual(res, "File name or file path error")

#     "a"  is a folder.
#     def test_filename_1(self):
#         res = atomicwriting(r"C:\Users\Lenovo\Desktop\a", "Yingtong Miao\nTammy")
#         self.assertEqual(res, "File name or file path error")

