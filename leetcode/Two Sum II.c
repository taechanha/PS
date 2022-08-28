int* twoSum(int* numbers, int numbersSize, 
            int target, int* returnSize){
    int i,j;
    int* out = malloc(sizeof(int)*2);
    *returnSize = 2;
    
    if(target > 0)
        for(i=0;i<numbersSize;++i){
            if(numbers[numbersSize-1-i] < target){
               break;
         }
        }
    numbersSize = numbersSize-i;
    
    printf("%d|", numbersSize);
    for(i=0;i<numbersSize-1;++i)
        for(j=i+1;j<numbersSize;++j){
            if((numbers[i] + numbers[j]) == target){
                printf("%d %d",i,j);
                goto label;
                }
        }
    label:
    out[0] = i+1;
    out[1] = j+1;
    return out;
}

