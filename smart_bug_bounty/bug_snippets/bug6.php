<?php

class LoginHandler {
    
    // Intended: Check if the provided hash matches the stored admin hash.
    // The stored hash starts with "0e...", which is scientific notation in loose comparison.
    public function checkAdminHash($input_hash) {
        $stored_hash = "0e123456789012345678901234567890"; // Example MD5 collision-prone format
        
        // Bug: PHP Type Juggling (Loose Comparison).
        // Using '==' allows strings looking like scientific notation (0e...) 
        // to be treated as floats (0.0). If input is also "0e..." they equate to true.
        // Should use '===' for strict comparison.
        if ($input_hash == $stored_hash) {
            return true;
        }
        
        return false;
    }
}
