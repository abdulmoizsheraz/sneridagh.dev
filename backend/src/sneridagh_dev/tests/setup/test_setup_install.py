from sneridagh_dev import PACKAGE_NAME


class TestSetupInstall:
    def test_addon_installed(self, installer):
        """Test if sneridagh_dev is installed."""
        assert installer.is_product_installed(PACKAGE_NAME) is True

    def test_browserlayer(self, browser_layers):
        """Test that ISneridaghDevLayer is registered."""
        from sneridagh_dev.interfaces import ISneridaghDevLayer

        assert ISneridaghDevLayer in browser_layers

    def test_latest_version(self, profile_last_version):
        """Test latest version of default profile."""
        assert profile_last_version(f"{PACKAGE_NAME}:default") == "20231031001"
