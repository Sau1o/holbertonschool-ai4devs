public class Bug3Fixed {
    // Fixed Logical error: changed condition to check for 0 (even) instead of 1 (odd)
    public static boolean isEven(int num) {
        if (num % 2 == 0) {
            return true; 
        } else {
            return false;
        }
    }

    public static void main(String[] args) {
        boolean result = isEven(4);
        System.out.println(result); // Expected true
        if (result != true) throw new RuntimeException("Test failed for input 4");
    }
}
