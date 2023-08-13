#include "lists.h"
/**
*check_cycle-checks if a list is a cycle
*@list:pointer to linked list
*Return:1 if cycle is detected and 0 if not
*/
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	while (fast && slow && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
		{
			return (1);
		}
	}
	return (0);
}
