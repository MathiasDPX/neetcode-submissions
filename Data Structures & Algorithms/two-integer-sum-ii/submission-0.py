class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ptrL = 0
        ptrR = len(numbers) - 1

        ptrSum = numbers[ptrL] + numbers[ptrR]
        while ptrSum != target:
            if ptrSum > target:
                ptrR -= 1
            else:
                ptrL += 1

            ptrSum = numbers[ptrL] + numbers[ptrR]

        return [ptrL + 1, ptrR + 1]