#include <stdio.h>
#include <string.h>


// initial function declarations

char *reverse_array(char *message);
int array_contains(char *message, int message_length, char item);
char *strip_punct(char *message);
int is_palindrome(char *message);
int is_exact(char *message);


int main(int argc, char **argv) {
	// debug options
	char *message = "tacoc.at";
	argc = 2;

	if (argc > 1) {
		// char *message = argv[1];

		// type[0]: is this an exact palindrome?
		// type[1]: is this a palindrome at all?
		// int type[2];
		// type[0] = is_exact(message);

		if (is_exact(message) == 1) {
			printf("This is a palindrome.\n");
		} else {
			if (is_palindrome(message) == 1) {
				printf("This is an inexact palindrome.");
			} else {
				printf("Sorry, this is not a palindrome.");
			}
		}
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
	message_length = strlen(message) + 10;

	// char *iter_message;
	// iter_message = message;

	char message_array[message_length];
	snprintf(message_array, "%s\0", (message_length), message);


	char message_punctless[message_length];
	int count_not_punct = 0;

	char punct[11] = {',', '.', ':', ';', '\'', '"', '!', '?', '/', '\\', ' '};

	int i;
	for (i = 0; i < message_length; i++) {
		int contains_this_punct = array_contains(message, message_length, punct[i]);

		if (contains_this_punct == 0) {
			char char_to_save = message_array[i];
			message_punctless[count_not_punct] == char_to_save;
			count_not_punct++;
		}
	}

	// add the string terminator to mark the end of string, regardless of array size, then return
	message_punctless[count_not_punct] = "\0";
	char *pointer_message_punctless = message_punctless;
	return pointer_message_punctless;
}


// checks if the message is a palindrome of any kind
int is_palindrome(char *message) {
	char *message_punctless = strip_punct(message);
	char *reversed_message_punctless = reverse_array(message_punctless);

	int message_punctless_length;
	message_punctless_length = strlen(message_punctless);

	int i;
	for (i = 0; i < message_punctless_length; i++, message_punctless++, reversed_message_punctless++) {
		if (*message != *reversed_message_punctless) {
			return 0;
		}
	}

	return 1;
}


// checks if the message is an EXACT palindrome
int is_exact(char *message) {
	int message_length;
	message_length = strlen(message);

	char *reversed_message = reverse_array(message);

	int i;
	for (i = 0; i < message_length; i++, message++, reversed_message++) {
		if (*message != *reversed_message) {
			return 0;
		}
	}

	return 1;
}