/*
 * FIX APPLIED:
 * Replaced unsafe gets() with fgets() to prevent buffer overflow.
 */
#include <stdio.h>
#include <string.h>

void get_client_name() {
    char name_buffer[32];
    
    printf("Enter name: ");
    
    // Fix: Limit input to buffer size - 1 (for null terminator)
    if (fgets(name_buffer, sizeof(name_buffer), stdin) != NULL) {
        // Optional: Remove trailing newline if present
        name_buffer[strcspn(name_buffer, "\n")] = 0;
        printf("Processing: %s\n", name_buffer);
    }
}
