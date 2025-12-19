/**
 * FIX APPLIED:
 * 1. Added null check BEFORE accessing length.
 * 2. Used .equals() for content comparison instead of ==.
 */
public class SecurityGate {
    private String masterKey = "OpenSesame123";

    public boolean unlock(String inputKey) {
        // Fix 1: Safety check for null
        if (inputKey == null || inputKey.length() == 0) {
            return false;
        }

        // Fix 2: Correct string comparison
        if (masterKey.equals(inputKey)) {
            return true;
        }

        return false;
    }
}
