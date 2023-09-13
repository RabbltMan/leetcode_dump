int searchInsert(int* nums, int numsSize, int target){
    int l = 0;
    int r = numsSize - 1;

    while (l < r) {
        if (target <= nums[l]) {
            return l;
        }
        if (target > nums[r]) {
            return r+1;
        }

        int m = (l + r) / 2;
        if (target >= nums[l] && target <= nums[m]) {
            r = m;
        }
        else {
            l = m + 1;
        }
    }

    return target <= nums[l] ? l : l+1;
}
