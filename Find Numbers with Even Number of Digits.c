int findNumbers(int* nums, int numsSize){
    int i;
    int count = 0;
    int numCount = 0;

    for(i=0;i<numsSize;++i){
        while(*(nums+i) != 0){
            *(nums+i) /= 10;
            count++;
        }
        if(count % 2 == 0){
            numCount++;
        }
        count = 0;
    }
    
    return numCount;
}

