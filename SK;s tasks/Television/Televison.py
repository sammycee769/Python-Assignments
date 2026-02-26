class Television:
    MIN_VOLUME =0
    MAX_VOLUME  = 100
    LAST_CHANNEL = 100
    FIRST_CHANNEL = 1

    def __init__(self):
        self.__is_on = False
        self.__volume = 0
        self.__channel = 1

    def turn_on(self):
        self.__is_on = True

    def turn_off(self):
        self.__is_on = False

    def check_tv_power_status(self):
        return self.__is_on

    def  __check_power_status(self):
        if not self.__is_on:
            raise ValueError("TV is Off")

    def increase_volume(self):
        self.__check_power_status()
        if self.__volume < self.MAX_VOLUME :
            self.__volume = self.__volume + 1

    def decrease_volume(self):
        self.__check_power_status()
        if self.__volume > self.MIN_VOLUME:
            self.__volume = self.__volume - 1

    def __channel_validator(self,channel:int):
        if channel < self.FIRST_CHANNEL or channel > self.LAST_CHANNEL:
            raise ValueError("Invalid channel number")

    def set_channel(self, channel:int):
        self.__check_power_status()
        self.__channel_validator(channel)
        self.__channel = channel

    def next_channel(self):
        self.__check_power_status()
        if self.__channel < self.LAST_CHANNEL:
            self.__channel = self.__channel + 1
        else:
            self.__channel = self.FIRST_CHANNEL

    def previous_channel(self):
        self.__check_power_status()
        if self.__channel > self.FIRST_CHANNEL:
            self.__channel = self.__channel - 1
        else:
            self.__channel = self.LAST_CHANNEL

    def get_volume(self):
        return self.__volume

    def get_channel(self):
        return self.__channel

    def is_on(self):
        return self.__is_on

