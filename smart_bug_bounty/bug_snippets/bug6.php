<?php

class PasswordReset {
    
    /**
     * Verifies if the reset token provided by the user matches the database hash.
     */
    public function verifyToken($user_input, $db_hash) {
        // Example hash that triggers the bug: "0e830400451993494058024219903391"
        
        // Bug: PHP Type Juggling (Magic Hash).
        // Using '==' (loose comparison) causes PHP to attempt to cast strings to numbers.
        // If both strings look like scientific notation (start with "0e" + digits),
        // they are treated as float(0) and considered equal, bypassing security.
        // Intended: Strict comparison '===' must be used to compare strings exactly.
        if ($user_input == $db_hash) {
            return true;
        }
        
        return false;
    }
}
