#include <stdio.h>
#include <string.h>


// initial function declarations

char *reverse_array(char *message);
int array_contains(char *message, int message_length, char item);
char *strip_punct(char *message);
int is_palindrome(char *message);
int is_exact(char *message);


int main(int argc, char **argv) {
	if (argc > 1) {
		char *message = argv[1];
		
	} else {
		printf("While an empty string IS technically a palindrome, it would be nice if you gave me a proper string to test.\n");
	}



	return 0;
}


// reverses the message by iterating on the original message array
char *reverse_array(char *message) {
	int message_length;
	message_length = strlen(message);

	char flipped[message_length];

	// assembles the `flipped` array
	int i;
	for (i = 1; i < message_length + 1; i++, message++) {
		flipped[message_length - i] = *message;
	}

	char *pointer_flipped = flipped;
	return pointer_flipped;
}


// is this item in this array?
int array_contains(char *message, int message_length, char item) {
	int i;
	for (i = 0; i < message_length; i++, message++) {
		if (*message == item) {
			// as soon as the item is found in the array, this should run
			return 1;
		}
	}

	// this should only be run if the item is not found in the array
	return 0;
}



// strips out any punctuation character
char *strip_punct(char *message) {
	int message_length;
	message_length = strlen(message);

	char *message_punctless;

	char punct[11] = {',', '.', ':', ';', '\'', '"', '!', '?', '/', '\\', ' '};

	int i;
	for (i = 0; i < message_length; i++, message++) {
		if (array_contains(message, message_length, punct[i]) == 0) {
			*message_punctless == *message;
			message_punctless++;
		}
	}
}


// checks if the message is a palindrome of any kind
int is_palindrome(char *message) {
	int message_length;
	message_length = strlen(message);

	// TODO: is reversed_message_punctless == message_punctless?
}


// checks if the message is an EXACT palindrome
int is_exact(char *message) {
	int message_length;
	message_length = strlen(message);

	char *flipped = reverse_array(message);

	// TODO: is reversed_message == message?

	return 1;
}