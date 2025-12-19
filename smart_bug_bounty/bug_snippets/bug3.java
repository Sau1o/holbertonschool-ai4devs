import java.util.Objects;

public class AuthManager {
    
    // Intended: Validate if the provided token matches the stored secret.
    public boolean validateToken(String inputToken) {
        String secretToken = "SuperSecret123";
        
        // Bug: NullPointerException if inputToken is null.
        // Should check for null before invoking methods on it.
        if (inputToken.length() == 0) {
            return false;
        }

        // Bug: String comparison using '==' checks memory reference, not content.
        // If inputToken is a new String object with same chars, this returns false.
        if (inputToken == secretToken) {
            return true;
        }
        
        return false;
    }

    // Intended: Safe integer division helper
    public int divide(int a, int b) {
        // Bug: Integer overflow edge case.
        // If a = Integer.MIN_VALUE and b = -1, result exceeds Integer.MAX_VALUE.
        return a / b; 
    }
}
