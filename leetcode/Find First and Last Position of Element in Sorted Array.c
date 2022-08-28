int* searchRange(int* nums, int numsSize, int target, int* returnSize){
    int* out = (int*)malloc(sizeof(unsigned int) * 2);
    int* p1 = &nums[0];
    int* p2 = &nums[numsSize-1];
    int count = 0;
    *returnSize = 2;
    
    if(numsSize == 0){
        out[0] = -1;
        out[1] = -1;
        return out;
    }
    else if(numsSize == 1)
        if(*p1 != target){
            out[0] = -1;
            out[1] = -1;
            return out;
        }
    
    while(*p1 != target){
        p1++;
        count++;
        if(count == numsSize){
            out[0] = -1;
            out[1] = -1;
            return out;
        }
    }
    out[0] = count;
    count = numsSize-1;
    
    while(*p2 != target){
        p2--;
        count--;
        }

    out[1] = count;
    
    return out;
}
