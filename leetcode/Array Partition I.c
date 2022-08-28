int min(int a, int b)
{
    if(a>b){
        return b;
    }
    else
        return a;
}
int compare(int* a, int* b)
{
    if(*a > *b)
        return 1;
    else if(*a < *b)
        return -1;
    else
        return 0;
}
int arrayPairSum(int* nums, int numsSize){
    int i, j;
    int sum = 0;
    
    qsort(nums, numsSize, sizeof(int), compare);
    
    for(i=0;i<numsSize;i+=2){
        sum += min(*(nums + i), *(nums + i + 1) );
    }
    
    return sum;
}

