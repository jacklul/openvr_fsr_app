from .openvr_mod_cfg import OpenVRModCfgSetting, OpenVRModSettings


class FsrSettings(OpenVRModSettings):
    def __init__(self):
        self.enabled = OpenVRModCfgSetting(
            key='enabled',
            name='Enabled',
            category='FSR Settings',
            desc="enable image upscaling through AMD's FSR or NVIDIA's NIS",
            value=True,
            settings=[{'value': True, 'name': 'On'}, {'value': False, 'name': 'Off'}]
        )
        self.useNIS = OpenVRModCfgSetting(
            key='useNIS',
            name="Use NVIDIA's Image Scaling",
            category='FSR Settings',
            desc="if enabled, uses NVIDIA's Image Scaling instead of the default "
                 "AMD FidelityFX SuperResolution. Both algorithms work similarly, but produce"
                 "somewhat different results. You may want to experiment switching between the"
                 "two to determine which one you like better for a particular game.",
            value=False,
            settings=[{'value': True, 'name': 'On'}, {'value': False, 'name': 'Off'}]
        )
        self.renderScale = OpenVRModCfgSetting(
            key='renderScale',
            name='Render Scale',
            category='FSR Settings',
            desc="Per-dimension render scale. If <1, will lower the game's render resolution"
                 "accordingly and afterwards upscale to the native resolution set in SteamVR. "
                 "If >1, the game will render at its native resolution, and afterwards the "
                 "image is upscaled to a higher resolution as per the given value. "
                 "If =1, effectively disables upsampling, but you'll still get the sharpening stage. "
                 "AMD presets: Ultra Quality => 0.77 Quality       => 0.67 Balanced      => 0.59 "
                 "Performance   => 0.50",
            value=0.77,
            settings=[{'settingType': 'range', 'min': 0.10, 'max': 3.0, 'step': 0.01, 'display': 'floatpercent'}]
        )
        self.sharpness = OpenVRModCfgSetting(
            key='sharpness',
            name='Sharpness',
            category='FSR Settings',
            desc="tune sharpness, values range from 0 to 1",
            value=0.9,
            settings=[{'settingType': 'range', 'min': 0.10, 'max': 3.0, 'step': 0.01, 'display': 'floatpercent'}]
        )
        self.radius = OpenVRModCfgSetting(
            key='radius',
            name='Radius',
            category='FSR Settings',
            desc="Only apply FSR/NIS to the given radius around the center of the image. "
                 "Anything outside this radius is upscaled by simple bilinear filtering,"
                 " which is cheaper and thus saves a bit of performance. Due to the design"
                 " of current HMD lenses, you can experiment with fairly small radii and may"
                 " still not see a noticeable difference."
                 " Sensible values probably lie somewhere between [0.2, 1.0]. However, note"
                 " that, since the image is not spheric, even a value of 1.0 technically still"
                 " skips some pixels in the corner of the image, so if you want to completely"
                 " disable this optimization, you can choose a value of 2."
                 " IMPORTANT: if you face issues like the view appearing offset or mismatched"
                 " between the eyes, turn this optimization off by setting the value to 2.0",
            value=0.50,
            settings=[{'settingType': 'range', 'min': 0.20, 'max': 2.00, 'step': 0.01}]
        )
        self.applyMIPBias = OpenVRModCfgSetting(
            key='applyMIPBias',
            name='Apply MIP Bias',
            category='FSR Settings',
            desc="if enabled, applies a negative LOD bias to texture MIP levels"
                 " should theoretically improve texture detail in the upscaled image"
                 " IMPORTANT: if you experience issues with rendering like disappearing"
                 " textures or strange patterns in the rendering, try turning this off"
                 " by setting the value to false.",
            value=True,
            settings=[{'value': True, 'name': 'On'}, {'value': False, 'name': 'Off'}]
        )
        self.offsetY = OpenVRModCfgSetting(
            key='offsetY',
            name='Center Offset Y',
            category='FSR Settings',
            value=0.85,
            settings=[{'settingType': 'range', 'min': 0.01, 'max': 1.99, 'step': 0.01}]
        )
        self.offsetX = OpenVRModCfgSetting(
            key='offsetX',
            name='Center Offset X',
            category='FSR Settings',
            value=0.95,
            settings=[{'settingType': 'range', 'min': 0.01, 'max': 1.99, 'step': 0.01}]
        )
        self.debugMode = OpenVRModCfgSetting(
            key='debugMode',
            name='Debug Mode',
            category='FSR Settings',
            desc="If enabled, will visualize the radius to which FSR/NIS is applied."
                 " Will also periodically log the GPU cost for applying FSR/NIS in the"
                 " current configuration.",
            value=False,
            settings=[{'value': True, 'name': 'On'}, {'value': False, 'name': 'Off'}]
        )

        # ---
        # Hotkey Settings
        # ---
        self.hotkeys = OpenVRModCfgSetting(
            key='hotkeys',
            name='Hotkeys',
            category='Hotkey Settings',
            hidden=True,
            value=dict(),
            settings=list(),
        )
        self.hotkeysEnabled = OpenVRModCfgSetting(
            key='enabled',
            parent=self.hotkeys.key,
            name='Hotkeys Enabled',
            category='Hotkey Settings',
            desc="If enabled, you can change certain settings of the mod on the fly by"
                 " pressing certain hotkeys. Good to see the visual difference. But you"
                 " may want to turn off hotkeys during regular play to prevent them from"
                 " interfering with game hotkeys.",
            value=True,
            settings=[{'value': True, 'name': 'On'}, {'value': False, 'name': 'Off'}]
        )
        self.hotkeysRequireCtrl = OpenVRModCfgSetting(
            key='requireCtrl',
            parent=self.hotkeys.key,
            name='Require Ctrl',
            category='Hotkey Settings',
            desc="if enabled, must also be holding CTRL key to use hotkeys",
            value=False,
            settings=[{'value': True, 'name': 'On'}, {'value': False, 'name': 'Off'}]
        )
        self.hotkeysRequireAlt = OpenVRModCfgSetting(
            key='requireAlt',
            parent=self.hotkeys.key,
            name='Require Alt',
            category='Hotkey Settings',
            desc="if enabled, must also be holding ALT key to use hotkeys",
            value=False,
            settings=[{'value': True, 'name': 'On'}, {'value': False, 'name': 'Off'}]
        )
        self.hotkeysRequireShift = OpenVRModCfgSetting(
            key='requireShift',
            parent=self.hotkeys.key,
            name='Require Shift',
            category='Hotkey Settings',
            desc="if enabled, must also be holding SHIFT key to use hotkeys",
            value=False,
            settings=[{'value': True, 'name': 'On'}, {'value': False, 'name': 'Off'}]
        )
        self.hotkeysToggleUseNIS = OpenVRModCfgSetting(
            key='toggleUseNIS',
            parent=self.hotkeys.key,
            name='Toggle NIS',
            category='Hotkeys',
            desc='switch between FSR and NIS',
            value=112,
            keyName='F1',
            settings=[{'settingType': 'key'}]
        )
        self.hotkeysToggleDebugMode = OpenVRModCfgSetting(
            key='toggleDebugMode',
            parent=self.hotkeys.key,
            name='Toggle Debug Mode',
            category='Hotkeys',
            desc='toggle debug mode on or off',
            value=113,
            keyName='F2',
            settings=[{'settingType': 'key'}]
        )
        self.hotkeysDecreaseSharpness = OpenVRModCfgSetting(
            key='decreaseSharpness',
            parent=self.hotkeys.key,
            name='Decrease Sharpness',
            category='Hotkeys',
            desc='decrease sharpness by 0.05',
            value=114,
            keyName='F3',
            settings=[{'settingType': 'key'}]
        )
        self.hotkeysIncreaseSharpness = OpenVRModCfgSetting(
            key='increaseSharpness',
            parent=self.hotkeys.key,
            name='Increase Sharpness',
            category='Hotkeys',
            desc='increase sharpness by 0.05',
            value=115,
            keyName='F4',
            settings=[{'settingType': 'key'}]
        )
        self.hotkeysDecreaseRadius = OpenVRModCfgSetting(
            key='decreaseRadius',
            parent=self.hotkeys.key,
            name='Decrease Radius',
            category='Hotkeys',
            desc='decrease sharpening radius by 0.05',
            value=116,
            keyName='F5',
            settings=[{'settingType': 'key'}]
        )
        self.hotkeysIncreaseRadius = OpenVRModCfgSetting(
            key='increaseRadius',
            parent=self.hotkeys.key,
            name='Increase Radius',
            category='Hotkeys',
            desc='increase sharpening radius by 0.05',
            value=117,
            keyName='F6',
            settings=[{'settingType': 'key'}]
        )
        self.hotkeysCaptureOutput = OpenVRModCfgSetting(
            key='captureOutput',
            parent=self.hotkeys.key,
            name='Capture Output',
            category='Hotkeys',
            desc='take a screenshot of the final output sent to the HMD',
            value=118,
            keyName='F7',
            settings=[{'settingType': 'key'}]
        )
        options = self.get_setting_fields()
        super(FsrSettings, self).__init__(options, 'fsr')
