class Solution:
    def uniqueMorseRepresentations(self, words):
        morse = [
            ".-", "-...", "-.-.", "-..", ".", "..-.", "--.",
            "....", "..", ".---", "-.-", ".-..", "--", "-.",
            "---", ".--.", "--.-", ".-.", "...", "-", "..-",
            "...-", ".--", "-..-", "-.--", "--.."
        ]

        transformations = set()

        for word in words:
            code = ""

            for char in word:
                index = ord(char) - ord('a')
                code += morse[index]

            transformations.add(code)

        return len(transformations)
