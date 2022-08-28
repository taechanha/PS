void moveZeroes(int* nums, int numsSize){
    signed int idx = -1; // flag
    int i;
    int temp;
    
    for(i=0;i<numsSize;++i){
        if(idx = -1 && nums[i] == 0){
            idx = i;
            continue;
        }
        if(nums[i] == 0)
            continue;
        
        temp = nums[i];
        nums[i] = nums[idx];
        nums[idx] = nums[i];
        
        idx = i;
    }
    
}