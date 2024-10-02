class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int x = nums1.length;
        int y = nums2.length;

        int i=0, j=0, m1=0, m2=0;
        for(int c=0; c<=(x+y)/2; c++){
            m2=m1;
            if(i!=x && j!=y){
                if(nums1[i]>nums2[j]){
                    m1=nums2[j++];
                } else {
                    m1=nums1[i++];
                }
            } else if(i<x){
                m1=nums1[i++];
            } else {
                m1=nums2[j++];
            }
        }

        if((x+y)%2==1){
            return (double) m1;
        }
        else {
            double ans = (double) m1 + (double) m2;
            return ans/2.0;
        }
    }
}