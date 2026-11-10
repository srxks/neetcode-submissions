class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for i in strs:
            s += str(len(i)) + "#" + i
        print(s)
        return s


    def decode(self, s: str) -> List[str]:
        k = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                print(i, j)
                j+=1

            length = int(s[i:j])

            k.append(s[j+1:j+length+1])

            i = j+length+1

        return k