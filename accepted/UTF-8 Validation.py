# coding=utf-8
class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        masks = [0x00, 0x80, 0xE0, 0xF0, 0xF8]
        bits = [0x0, 0x0, 0xC0, 0xE0, 0xF0]
        while data:
            for idx in range(4,-1,-1):
                if masks[idx] & data[0] == bits[idx]:
                    break # idx表示有idx个byte
            if idx == 0 or idx > len(data):
                return False
            for i in range(1, idx):
                if data[i] & 0xC0 != 0x80:
                    return False
            data = data[idx:]
        return True
