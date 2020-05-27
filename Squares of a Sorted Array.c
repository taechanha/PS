int compare(int* a, int* b)
{
    if(*a > *b)
        return 1;
    else if(*b > *a)
        return -1;
    else
        return 0;
}
int* sortedSquares(int* A, int ASize, int* returnSize){
    int i, j;
    int temp;
    
    for(i=0;i<ASize;++i){
        *(A + i) *= *(A + i);
    }
    
    qsort(A, ASize, sizeof(int), compare);
    
    *returnSize = ASize;
    return A;
}

