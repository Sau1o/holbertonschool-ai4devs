#include <stdio.h>
#include <string.h>

void process_user_input() {
    char buffer[50];
    
    printf("Enter your username: ");
    
    // Bug: 'gets' is extremely dangerous and deprecated. 
    // It does not check buffer boundaries, leading to Buffer Overflow 
    // if input is longer than 50 characters.
    gets(buffer);
    
    printf("Welcome, %s\n", buffer);
}

int main() {
    process_user_input();
    return 0;
}
