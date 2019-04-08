import java.util.Scanner;
import java.util.Stack;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int num = scanner.nextInt();

        for (int i = 0; i < num; i++) {
            String str = scanner.next();
            Stack stack = new Stack<>();
            String result = "YES";

            for (int j = 0; j < str.length(); j++) {

                if (str.charAt(j) == '(') {
                    stack.push(str.charAt(j));
                }

                if (str.charAt(j) == ')') {

                    if (!stack.isEmpty()) {
                        stack.pop();
                    } else {
                        result = "NO";
                    }
                }

            }

            if (!stack.isEmpty()) {
                result = "NO";
            }

            System.out.println(result);
        }
    }
}