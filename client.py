import bge
import socket
import struct
from mathutils import Vector
from collections import OrderedDict

if not hasattr(bge, "__component__"):
    pass

class Component(bge.types.KX_PythonComponent):

    args = OrderedDict([
    ])

    def start(self, args):
        self.udp_ip = 'localhost'
        self.udp_port = 4444
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def update(self):
        ba = bytearray(struct.pack("d", self.object.localPosition[0]))
        print(ba)
        #Only send up key strokes for now, instead of position.
        self.sock.sendto(ba, (self.udp_ip, self.udp_port))
        #catch events in a listen check instead of freezing here.
        data, server = self.sock.recvfrom(1204)
        newPos = struct.unpack("d", data)
        print(newPos[0])
        #applyMovement instead of directly manipulating position.
        self.object.localPosition = Vector((newPos[0], self.object.localPosition[1], self.object.localPosition[2]))