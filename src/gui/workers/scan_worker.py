from traceback import format_exc

from PyQt6.QtCore import QObject, pyqtSignal

from ...engine.engine import ShadowPathEngine


class ScanWorker(QObject):

    finished = pyqtSignal(object)
    error = pyqtSignal(str)
    progress = pyqtSignal(str, int)

    def __init__(self):
        super().__init__()

        self.cancel_requested = False

    # =====================================================

    def stop(self):
        self.cancel_requested = True

    # =====================================================

    def run(self):

        try:

            if self.cancel_requested:
                return

            engine = ShadowPathEngine(
                server_ip="192.168.56.10",
                username="SHADOWPATH\\Administrator",
                password="Password123!",
                base_dn="DC=shadowpath,DC=local",
                progress_callback=self.progress.emit,
            )

            if self.cancel_requested:
                return

            result = engine.run()

            if self.cancel_requested:
                return

            self.finished.emit(result)

        except Exception:

            traceback = format_exc()

            print(traceback)

            self.error.emit(traceback)