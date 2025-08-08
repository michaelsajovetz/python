class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3


    def __init__(self):
        self.__status = False
        self.__muted = False
        self.__volume = self.MIN_VOLUME
        self.__channel = self.MIN_CHANNEL


    def power(self):
        '''
        Changes the power status of the TV from on to off or vice versa
        '''
        self.__status = not self.__status


    def mute(self):
        '''
        Changes the muted status of the TV from muted to not muted or vice versa
        '''
        if self.__status:
            self.__muted = not self.__muted


    def channel_up(self):
        '''
        Increases the selected channel by one. If channel is at maximum, set to minimum
        '''
        if self.__status:
            new_channel = self.__channel + 1
            if new_channel > self.MAX_CHANNEL:
                new_channel = self.MIN_CHANNEL
            self.__channel = new_channel


    def channel_down(self):
        '''
        Decreases the selected channel by one. If channel is at minimum, set to maximum
        '''
        if self.__status:
            new_channel = self.__channel - 1
            if new_channel < self.MIN_CHANNEL:
                new_channel = self.MAX_CHANNEL
            self.__channel = new_channel


    def volume_up(self):
        '''
        If the TV is on and if the volume is below the maximum, un-mutes the TV (if muted) and increases the volume by one
        '''
        if self.__status:
            if self.__muted:
                self.__muted = False
            new_volume = self.__volume + 1
            if new_volume > self.MAX_VOLUME:
                new_volume = self.MAX_VOLUME
            self.__volume = new_volume


    def volume_down(self):
        '''
        If the TV is on and if the volume is above the minimum, un-mutes the TV (if muted) and decreases the volume by one
        '''
        if self.__status:
            if self.__muted:
                self.__muted = False
            new_volume = self.__volume - 1
            if new_volume < self.MIN_VOLUME:
                new_volume = self.MIN_VOLUME
            self.__volume = new_volume


    def __str__(self) -> str:
         '''
         Custom string method for the Television class
         :return: a string with the TV's current status, channel, and volume
         '''
         if self.__muted:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.MIN_VOLUME}'
         else:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'