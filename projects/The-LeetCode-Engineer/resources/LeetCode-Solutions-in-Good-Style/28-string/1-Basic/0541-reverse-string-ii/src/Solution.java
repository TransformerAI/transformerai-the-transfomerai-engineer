public class Solution {

    public String reverseStr(String s, int k) {
        int len = s.length();
        char[] charArr = s.toCharArray();
        int begin = 0;
        int step = 2 * k;
        while (begin < len) {
            int end = begin + k - 1;
            reverseCharArr(charArr, begin, Math.min(end, len - 1));
            begin += step;
        }
        return String.valueOf(charArr);
    }

    /**
     * 反转一个字符数组的指定部分
     * @param arr
     * @param left
     * @param right
     */
    private void reverseCharArr(char[] arr, int left, int right) {
        while (left < right) {
            swap(arr, left, right);
            left++;
            right--;
        }
    }

    private void swap(char[] arr, int index1, int index2) {
        char temp = arr[index1];
        arr[index1] = arr[index2];
        arr[index2] = temp;
    }
}