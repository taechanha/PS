int peakIndexInMountainArray(int* A, int ASize){
    int i;
    int maxIdx;
    
    for(i=1;i<ASize;++i){
        if(*A < *(A + i)){
            *A = *(A + i);
            maxIdx = i;
        }
    }

    return maxIdx;
}