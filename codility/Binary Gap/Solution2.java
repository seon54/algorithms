public class Solution2 {

    // with recursion
    public int solution(int N) {

        return binaryGap(N, 0, 0, 0);
    }

    public int binaryGap(int n, int counter, int max, int index) {

        if (n == 0) {
            return max;
        }

        if (n % 2 == 0 && index == 0) {
            index = 0;
        } else if (n % 2 == 0) {
            counter++;
        } else {
            max = Math.max(counter, max);
            index++;
            counter = 0;

        }

        n = n / 2;

        return binaryGap(n, counter, max, index);
    }
}
