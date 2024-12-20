public class Solution {

    // 只包含小写数字，干脆全部转成 0-25 的数字就好了
    // 根据题意，t 比 s 多 1 个字符，干脆初始值就取 t 的第 1 个字符

    public char findTheDifference(String s, String t) {
        int sLen = s.length();
        int tLen = t.length();

        char[] sCharArray = s.toCharArray();
        char[] tCharArray = t.toCharArray();


        int res = tCharArray[0] - 'a';
        for (int i = 0; i < sLen; i++) {
            res ^= (sCharArray[i] - 'a');
        }
        for (int i = 1; i < tLen; i++) {
            res ^= (tCharArray[i] - 'a');
        }
        return (char) (res + 'a');
    }
}