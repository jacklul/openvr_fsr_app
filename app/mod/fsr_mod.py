from pathlib import Path

from app.app_settings import AppSettings
from app.cfg.fsr_cfg import FsrSettings
from app.globals import OPEN_VR_DLL
from .base_mod import BaseMod, BaseModType


class FsrMod(BaseMod):
    TYPE = BaseModType.fsr
    VAR_NAMES = {
        'installed': 'fsrInstalled',
        'version': 'fsrVersion',
        'settings': 'settings',
    }

    def __init__(self, manifest: dict):
        self.settings = FsrSettings()
        self.settings.from_js_dict(manifest.get(self.VAR_NAMES['settings']))
        fsr_mod_dll = Path(AppSettings.openvr_fsr_dir) / OPEN_VR_DLL

        super(FsrMod, self).__init__(manifest, self.settings, fsr_mod_dll)
