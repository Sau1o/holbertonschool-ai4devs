#include <stdio.h>
#include <string.h>

void get_client_name() {
    char name_buffer[32];
    
    printf("Please enter your client ID name: ");
    
    // Bug: Buffer Overflow Vulnerability.
    // 'gets' reads input until a newline is found, regardless of buffer size.
    // If user enters > 32 chars, it overwrites the stack memory, potentially
    // causing a crash or allowing arbitrary code execution.
    // Intended: Use fgets() to limit input to sizeof(name_buffer).
    gets(name_buffer);
    
    printf("Processing client: %s\n", name_buffer);
}
