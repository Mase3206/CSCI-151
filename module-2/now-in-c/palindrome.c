#include <stdio.h>
#include <string.h>
#include <stdlib.h>


// initial function declarations

char *reverse_array(char *message);
int array_contains(char *message, int message_length, char item);
char *strip_punct(char *message);
int is_palindrome(char *message);
int is_exact(char *message);


int main(int argc, char **argv) {
	// uncomment the following line when debugging
	// char *message = "tacocat";
	// argc = 2;

	if (argc > 1) {
		// comment 2 lines down when debugging
		// message passed in via cli by the user
		char *message = argv[1];

		if (is_exact(message) == 1) {
			printf("This is a palindrome.\n");
		} else {
			if (is_palindrome(message) == 1) {
				printf("This is an inexact palindrome.\n");
			} else {
				printf("Sorry, this is not a palindrome.\n");
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

	char *flipped = malloc((message_length + 1) * sizeof(char));

	// assembles the `flipped` array
	int i;
	for (i = 1; i < message_length + 1; i++, message++) {
		flipped[message_length - i] = *message;
	}

    flipped[message_length] = '\0'; // Don't forget to null-terminate the string
	return flipped;
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

	char message_array[message_length];
	strcpy(message_array, message);

	char message_punctless[message_length];
	int count_not_punct = 0;

	char punct[11] = {',', '.', ':', ';', '\'', '"', '!', '?', '/', '\\', ' '};

	int i, j;
	// iterate thru message
	for (i = 0; i < message_length; i++) {
		int is_punct = 0;

		// check each punctuation
		for (j = 0; j < 11; j++) {
			if (message_array[i] == punct[j]) {
				is_punct = 1;
				break;
			}
		}

		if (!is_punct) {
			message_punctless[count_not_punct] = message_array[i];
			count_not_punct++;
		}
	}

	// add the string terminator to mark the end of string, regardless of array size, then return
	message_punctless[count_not_punct] = "\0"[0];
	char *pointer_message_punctless = message_punctless;
	return pointer_message_punctless;
}


// checks if the message is a palindrome of any kind
int is_palindrome(char *message) {
	printf("%s\n", message);
	char *message_punctless = strip_punct(message);
	printf("%s\n", message_punctless);

	int exact = is_exact(message_punctless);
	return exact;
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

	free(reversed_message);
	return 1;
}