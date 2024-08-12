class MusicPlayer:
    """
    Facade class that provides a simple interface to the complex subsystem.
    """
    def __init__(self):
        self.mp3_player = None
        self.flac_player = None

    def play_mp3(self):
        if self.mp3_player is None:
            self.mp3_player = MP3Player()
        self.mp3_player.load("music.mp3")
        self.mp3_player.set_volume(22)
        self.mp3_player.play()

    def play_flac(self):
        if self.flac_player is None:
            self.flac_player = FlacPlayer()
        self.flac_player.load("music.flac")
        self.flac_player.set_volume(44)
        self.flac_player.play()


class MP3Player:
    def load(self, file_path: str):
        print(f'Loading MP3 from {file_path}...')
        return self

    def set_volume(self, volume: int):
        print(f'Setting volume to {volume}...')
        return self

    def play(self):
        print('Playing MP3...')
        return self


class FlacPlayer:
    def load(self, file_path: str):
        print(f'Loading FLAC from {file_path}...')
        return self

    def set_volume(self, volume: int):
        print(f'Setting volume to {volume}...')
        return self

    def play(self):
        print('Playing FLAC...')
        return self


if __name__ == '__main__':
    player = MusicPlayer()
    player.play_mp3()
    player.play_flac()
