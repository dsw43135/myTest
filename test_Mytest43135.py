import unittest
from PyQt5.QtWidgets import QApplication
from Mytest43135 import SystemInfoApp

class TestSystemInfoApp(unittest.TestCase):
    def setUp(self):
        self.app = QApplication([])
        self.window = SystemInfoApp()

    def tearDown(self):
        self.window.close()

    def test_get_ip_info(self):
        self.window.get_ip_info()

        expected_text = "Adres IP:"
        self.assertIn(expected_text, self.window.text_view.toPlainText())

    def test_get_proxy_info(self):
        self.window.get_proxy_info()

        expected_text = "Proxy Information:"
        self.assertIn(expected_text, self.window.text_view.toPlainText())

    def test_get_os_ram_info(self):
        self.window.get_os_ram_info()

        expected_text = "System operacyjny:"
        self.assertIn(expected_text, self.window.text_view.toPlainText())

    def test_get_bios_version(self):
        self.window.get_bios_version()
        expected_text = "Wersja BIOS:"
        self.assertIn(expected_text, self.window.text_view.toPlainText())

    def test_get_host_name(self):
        self.window.get_host_name()
        expected_text = "Nazwa hosta:"
        self.assertIn(expected_text, self.window.text_view.toPlainText())

if __name__ == '__main__':
    unittest.main()
