#include <stdio.h>
#include <string.h>


// initial function declarations

char * reverse_array(char *message);
int is_exact(char message[]);


int main(int argc, char **argv) {
	

	return 0;
}


char * reverse_array(char *message) {
	int message_length;
	message_length = strlen(message);

	char flipped[message_length];
	// flipped[0] = *message;

	int i;
	for (i = 1; i < message_length + 1; i++, message++) {
		flipped[message_length - i] = *message;
	}

	char *pointer_flipped = flipped;
	return pointer_flipped;
}


int is_exact(char *message) {


	return 1;
}