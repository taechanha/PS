double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size){
    int* new = (int*)malloc(sizeof(int) * (nums1Size+nums2Size));
    int i = 0;
    int count1 = 0;
    int count2 = 0;
    
    if(nums1Size+nums2Size == 1){
        if(nums1Size == 1)
            return *nums1;
        else
            return *nums2;
    }
    else if(nums1Size == 0){
        if((nums2Size & 0x1) == 0)
            return (double)(nums2[nums2Size/2-1]+nums2[nums2Size/2])/2;
        else
            return (double)nums2[nums2Size/2];
    }
    else if(nums2Size == 0){
        if((nums1Size & 0x1) == 0)
            return (double)(nums1[nums1Size/2-1]+nums1[nums1Size/2])/2;
        else
            return (double)nums1[nums1Size/2];
    }
        
    
   while(i != (nums1Size+nums2Size))
   {
       
       if((nums1[count1 == nums1Size ? count1-1:count1] > nums2[count2 == nums2Size ? count2-1:count2] 
           && (count2) != nums2Size)
          || (count1) == nums1Size)
       {
           *(new+i) = *(nums2+count2);
           count2++;
       }
       else{
           *(new+i) = *(nums1+count1);
           count1++;
           
       }
       i++;
   }   
    
    if(((nums1Size+nums2Size) & 0x1) == 0){
        return (double)(new[(nums1Size+nums2Size)/2 - 1] + new[(nums1Size+nums2Size)/2]) / 2;
    }
    else
        return (double)new[(nums1Size+nums2Size)/2];
}


