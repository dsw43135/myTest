import sys
import socket
import platform
import psutil
import wmi
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QPushButton

class SystemInfoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("System Information")
        self.setGeometry(100, 100, 800, 600)

        self.text_view = QTextEdit(self)
        self.text_view.setReadOnly(True)

        self.button_panel = QVBoxLayout()
        self.create_button("1. IP Information", self.get_ip_info)
        self.create_button("2. Proxy Information", self.get_proxy_info)
        self.create_button("3. OS and RAM Information", self.get_os_ram_info)
        self.create_button("4. BIOS Version", self.get_bios_version)
        self.create_button("5. Host Name", self.get_host_name)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.text_view)
        main_layout.addLayout(self.button_panel)
        self.setLayout(main_layout)

    def create_button(self, text, callback):
        button = QPushButton(text, self)
        button.clicked.connect(callback)
        self.button_panel.addWidget(button)

    def get_ip_info(self):
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        is_static = "Static" if socket.gethostbyname_ex(hostname)[2] else "Dynamic"
        is_ethernet = "Ethernet" if "Ethernet" in str(psutil.net_if_stats()) else "Wi-Fi"
        self.text_view.clear()
        self.text_view.append(f"Hostname: {hostname}")
        self.text_view.append(f"IP Address: {ip_address}")
        self.text_view.append(f"IP Type: {is_static}")
        self.text_view.append(f"Connection Type: {is_ethernet}")

    def get_proxy_info(self):
        self.text_view.clear()
        self.text_view.append("Proxy Information: No Proxy")

    def get_os_ram_info(self):
        os_info = platform.uname()
        ram_info = psutil.virtual_memory()
        self.text_view.clear()
        self.text_view.append(f"Operating System: {os_info.system} {os_info.release}")
        self.text_view.append(f"RAM Total: {ram_info.total / (1024 ** 3):.2f} GB")
        self.text_view.append(f"RAM Available: {ram_info.available / (1024 ** 3):.2f} GB")

    def get_bios_version(self):
        c = wmi.WMI()
        bios_info = c.Win32_BIOS()[0]
        self.text_view.clear()
        self.text_view.append(f"BIOS Version: {bios_info.Version}")

    def get_host_name(self):
        host_name = socket.gethostname()
        self.text_view.clear()
        self.text_view.append(f"Host Name: {host_name}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SystemInfoApp()
    window.show()
    sys.exit(app.exec_())
