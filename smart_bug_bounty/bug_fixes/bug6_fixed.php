<?php
/*
 * FIX APPLIED:
 * Used strict comparison (===) to prevent Magic Hash vulnerability.
 */
class TokenVerifier {
    public function verify($user_input, $db_hash) {
        // Fix: Strict comparison checks type and content
        if ($user_input === $db_hash) {
            return true;
        }
        return false;
    }
}
