import pytest
from television import Television

class TestTelevision:
    def setup_method(self):
        self.tv1 = Television()
    

    def teardown_method(self):
        del self.tv1

    def test_init(self):
        assert "Power = False" in str(self.tv1)
        assert "Channel = 0" in str(self.tv1)
        assert "Volume = 0" in str(self.tv1)

    def test_power(self):
        assert "Power = False" in str(self.tv1)
        self.tv1.power()
        assert "Power = True" in str(self.tv1)
        self.tv1.power()
        assert "Power = False" in str(self.tv1)

    def test_mute(self):
        self.tv1.power()
        self.tv1.volume_up()
        self.tv1.volume_up()
        assert "Volume = 2" in str(self.tv1)
        self.tv1.mute()
        assert "Volume = 0" in str(self.tv1)
        self.tv1.mute()
        assert "Volume = 2" in str(self.tv1)

    def test_volume_up(self):
        self.tv1.power()
        self.tv1.volume_up()
        assert "Volume = 1" in str(self.tv1)
        self.tv1.volume_up()
        assert "Volume = 2" in str(self.tv1)
        self.tv1.volume_up()
        assert "Volume = 2" in str(self.tv1)

    def test_volume_down(self):
        self.tv1.power()
        self.tv1.volume_up()
        self.tv1.volume_up()
        assert "Volume = 2" in str(self.tv1)
        self.tv1.volume_down()
        assert "Volume = 1" in str(self.tv1)
        self.tv1.volume_down()
        assert "Volume = 0" in str(self.tv1)
        self.tv1.volume_down()
        assert "Volume = 0" in str(self.tv1)

    def test_volume_change_unmutes(self):
        self.tv1.power()
        self.tv1.mute()
        assert "Volume = 0" in str(self.tv1)
        self.tv1.volume_up()
        assert "Volume = 0" not in str(self.tv1)
        self.tv1.mute()
        self.tv1.volume_down()
        assert "Volume = 0" not in str(self.tv1)