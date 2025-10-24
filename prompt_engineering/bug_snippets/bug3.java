// Intended to print the length of each string in an array

public class Bug3 {
    public static void main(String[] args) {
        String[] words = {"apple", "banana", null, "grape"};

        for (String word : words) {
            System.out.println(word.length());
        }
    }
}
