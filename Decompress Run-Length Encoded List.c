int* decompressRLElist(int* nums, int numsSize, int* returnSize){
    
    int i, j;
    int* str = malloc(sizeof(int) * 100 * (numsSize / 2));
    
    *returnSize = 0;
    
    for(i=0;i<numsSize;++i){
        if(i & 0x1 == 1){
            for(j=0;j<nums[i-1];++j){
                str[*returnSize] = nums[i];
                ++*returnSize;
            }
        } 
    }
    
    return str;
}
