public class remove_element {

    public int removeElement(int[] nums, int val) {
        int tracker = 0;
        
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != val) {
                nums[tracker] = nums[i];
                tracker++;
            }
        }
        return tracker;
    }

    
    public void main(String[] args) {
        removeElement(new int[]{3,2,2,3},3);
        removeElement(new int[]{0,1,2,2,3,0,4,2},2);
    }
}
