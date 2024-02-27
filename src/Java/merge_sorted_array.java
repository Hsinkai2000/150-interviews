
class Solution {
    public static void merge(int[] nums1, int m, int[] nums2, int n) {
        int counter1 = m-1;
        int counter2 = n-1;
        int tracker = m+n-1;
        
        while (counter2>=0){
            if(counter1 >= 0 && nums1[counter1] > nums2[counter2]){
                nums1[tracker] = nums1[counter1];
                counter1--;
            }
            else{
                nums1[tracker] = nums2[counter2];
                counter2--;    
            }
            tracker--;
        }
    }
    
    // public static void main(String[] args) {
    //     merge(new int[]{1,2,3,0,0,0},3,new int[]{2,5,6},3);
    //     merge(new int[]{1},1,new int[]{},0);
    //     merge(new int[]{4,5,6,0,0,0},3,new int[]{1,2,3},3);
    // }

    public static int removeDuplicates(int[] nums) {
        int index=0;

        for (int i = 0; i < nums.length-1; i++) {
            if (nums[i] < nums[i+1]) {
                nums[index] = nums[i];
                index++;
            }
            if(i+1 == nums.length && nums[i] < nums[i+1]){
                index++;
            }
        }

        return index;
    }

    public static void main(String[] args) {
        System.out.println(removeDuplicates(new int[]{0,0,1,1,1,2,2,3,3,4}));
        System.out.println("hi");
    }
}