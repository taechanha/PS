int* smallerNumbersThanCurrent(int* nums, int numsSize, int* returnSize){
    *returnSize = numsSize;
    int count;
    int* out = (int*)malloc(sizeof(int) * numsSize);
    int i, j;
    
    for(i=0;i<numsSize;++i){
        count = 0;
        for(j=0;j<numsSize;++j){
            if(*(nums+i) > *(nums+j)){
                count++;
            }
        }
        *(out + i) = count;
    } 
        
    return out;
}

