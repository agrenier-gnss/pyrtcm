import os
import sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
sys.path.append(os.path.join(ROOT, "src"))

from pyrtcm import RTCMReader, ERR_RAISE

rtcm_file = "./ssr_binary_SSRC00CNE025306A.rtcm3"

with open(rtcm_file, 'rb') as stream:
    rtr = RTCMReader(stream, quitonerror=ERR_RAISE, labelmsm=1)
    for raw_data, parsed_data in rtr:
        print(parsed_data)
        print(" ")

