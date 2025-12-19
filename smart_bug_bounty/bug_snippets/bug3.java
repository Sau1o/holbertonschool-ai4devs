public class SecurityGate {
    
    private String masterKey = "OpenSesame123";

    /**
     * Authenticates a user based on a provided key.
     */
    public boolean unlock(String inputKey) {
        // Bug 1: NullPointerException Risk.
        // If inputKey is null, inputKey.length() throws an exception.
        // Intended: check for null first.
        if (inputKey.length() == 0) {
            return false;
        }

        // Bug 2: Reference Equality vs Content Equality.
        // In Java, '==' compares memory addresses for Objects (Strings).
        // If inputKey is a new String object with the same text, this returns false.
        // Intended: use inputKey.equals(masterKey).
        if (inputKey == masterKey) {
            return true;
        }

        return false;
    }
}
