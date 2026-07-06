from traceback import format_exc

from PyQt6.QtCore import QObject, pyqtSignal

from ...engine.engine import ShadowPathEngine


class ScanWorker(QObject):

    finished = pyqtSignal(object)
    error = pyqtSignal(str)
    progress = pyqtSignal(str, int)

    def run(self):

        try:

            engine = ShadowPathEngine(
                server_ip="192.168.56.10",
                username="SHADOWPATH\\Administrator",
                password="Password123!",
                base_dn="DC=shadowpath,DC=local",
                progress_callback=self.progress.emit,
            )

            result = engine.run()

            self.finished.emit(result)

        except Exception:

            traceback = format_exc()

            print(traceback)

            self.error.emit(traceback)