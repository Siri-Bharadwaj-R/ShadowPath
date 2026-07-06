"""
ShadowPath Engine

Backend API for the GUI.
"""

from .models import EngineResult


class ShadowPathEngine:
    """
    Entry point for the ShadowPath analysis engine.
    """

    def __init__(self):
        pass

    def run(self) -> EngineResult:
        """
        Execute a complete ShadowPath analysis.

        Implementation will be added during the engine refactor.
        """
        raise NotImplementedError("ShadowPath engine not implemented yet.")