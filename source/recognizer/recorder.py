import pyaudio
import wave

from PyQt5 import QtCore

class Recorder(QtCore.QObject):
    def __init__(self, channels=1, rate=44100, frames_per_buff=1024):
        self.channels = channels
        self.rate = rate
        self.frames_per_buff = frames_per_buff

    def open(self, fname, mode='wb'):
        return RecordingFile(fname, mode, self.channels, self.rate, self.frames_per_buff)

class RecordingFile(QtCore.QObject):
    def __init__(self, fname, mode, channels, rate, frames_per_buff):
        self.fname = fname
        self.mode = mode
        self.channels = channels
        self.rate = rate
        self.frames_per_buff = frames_per_buff
        self.pa = pyaudio.PyAudio()
        self.wavefile = self._prepare_file(self.fname, self.mode)
        self.stream = None

    def __exit__(self, exception, value, traceback):
        self.close()

    def close(self):
        self.stream.close()
        self.pa.terminate()
        self.wavefile.close()

    def _prepare_file(self, fname, mode='wb'):
        wavefile = wave.open(fname, mode)
        wavefile.setnchannels(self.channels)
        wavefile.setsampwidth(self.pa.get_sample_size(pyaudio.paInt16))
        wavefile.setframerate(self.rate)
        return wavefile

    def get_callback(self):
        def callback(in_data, frame_count, time_info, status):
            self.wavefile.writeframes(in_data)
            return in_data, pyaudio.paContinue
        return callback

    def start_rec(self):
        self.stream = self.pa.open(format=pyaudio.paInt16,
                                    channels=self.channels,
                                    rate=self.rate,
                                    input=True,
                                    frames_per_buffer=self.frames_per_buff,
                                    stream_callback=self.get_callback())
        self.stream.start_stream()
        return self

    def stop_rec(self):
        self.stream.stop_stream()
        return self