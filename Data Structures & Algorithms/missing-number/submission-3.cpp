#include <numeric>

class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int n = nums.size();
        int sum = std::reduce(nums.begin(), nums.end());
        
        return n*(n+1)/2 - sum;
    }
};


/*
n = len(nums)
target = n * (n + 1) // 2 # Sum of the range [0;n]
        
return target - sum(nums)
*/