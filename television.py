class Television:
    MIN_VOLUME = 0
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3
    MAX_VOLUME = 2

    def __init__(self) -> None:
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self) -> None:
        """
        Method to turn on and off the tv
        """
        if self.__status:
            self.__status = False
        else:
            self.__status = True

    def mute(self) -> None:
        """
        Method to mute the volume on the tv
        """
        if self.__status and self.__muted == False:
            self.__muted = True
        else:
            self.__muted = False

    def channel_up(self):
        """
        Method to increase the tv channel.
        """
        if self.__channel < Television.MAX_CHANNEL:
            self.__channel += 1
        else:
            self.__channel = Television.MIN_CHANNEL

    def channel_down(self):
        """
        Method to decrease the tv channel.
        """
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self):
        """
        Method to increase the tv volume.
        """
        if self.__status:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self):
        """
         Method to increase the tv volume.
        """
        if self.__status:
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        Method to show the tv status.
        :return: tv status.
        """
        if self.__muted:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME}'
        else:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
