
class RemoveDuplicates {
    public int removeDuplicates(int[] nums) {
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

    public void main(String[] args) {
        System.out.println(removeDuplicates(new int[]{0,0,1,1,1,2,2,3,3,4}));
        System.out.println("hi");
    }
}