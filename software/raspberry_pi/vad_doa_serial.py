
import sys
import webrtcvad
import numpy as np
from mic_array_serial import MicArray
from pixel_ring import pixel_ring
import serial
import time


RATE = 16000
CHANNELS = 4
VAD_FRAMES = 10     # ms
DOA_FRAMES = 100    # ms


def main():
    vad = webrtcvad.Vad(3)

    speech_count = 0
    chunks = []
    doa_chunks = int(DOA_FRAMES / VAD_FRAMES)

    try:
        with MicArray(RATE, CHANNELS, RATE * VAD_FRAMES / 1000)  as mic:
            for chunk in mic.read_chunks():
                # Use single channel audio to detect voice activity
                if vad.is_speech(chunk[0::CHANNELS].tobytes(), RATE):
                    speech_count += 1
                #     sys.stdout.write('1')
                # else:
                #     sys.stdout.write('0')

                sys.stdout.flush()

                chunks.append(chunk)
                if len(chunks) == doa_chunks:
                    if speech_count > (doa_chunks * 0.3):    #original factor: 0.5
                        frames = np.concatenate(chunks)
                        direction = mic.get_direction(frames)
                        pixel_ring.set_direction(direction)
                        print('\n{}'.format(int(direction)))
                        data_ser.write(bytearray(str(int(direction)),'ascii'))

                    speech_count = 0
                    chunks = []

    except KeyboardInterrupt:
        pass
        
    pixel_ring.off()


if __name__ == '__main__':
    data_ser = serial.Serial("/dev/ttyGS0", 115200, timeout = 300)
    data_ser.flushInput()

    #main()    

    if data_ser.isOpen():
        print("serial open success!")
        main()
    else: 
        print("serial open failed!")
    

