#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

listint_t *create_node(int n);

/**
 * insert_node - inserts a node sorted in a linked list of ints
 * @head: double pointer to head of LL, needed for modification in edge
 * cases
 * @number: data for new node
 *
 *print_listint - prints all elements of a listint_t list
 *
 * Return: number of nodes
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *cur_node = NULL, *new_node = NULL;

	if (!head)
		return (NULL);
	else if (!(*head))
	{
		new_node = create_node(number);
		*head = new_node;
		return (new_node);
	}
	cur_node = *head;
	while (cur_node)
	{
		/* need to insert at head */
		if (cur_node->n >= number)
		{
			new_node = create_node(number);
			new_node->next = cur_node;
			*head = new_node;
			return (new_node);
		}
		else if (cur_node->n <= number)
		{
			if (!cur_node->next || cur_node->next->n >= number)
			{
				new_node = create_node(number);
				new_node->next = cur_node->next;
				cur_node->next = new_node;
				return (cur_node->next);
			}
		}
		cur_node = cur_node->next;
	}
	return (NULL); /* failed */
}


/**
 * create_node - creates a new node for the LL
 * @n: integer to be included in new node
 *
 * Return: address of the new element or NULL if it fails
 */
listint_t *create_node(int n)
{
	listint_t *ret = NULL;

	ret = malloc(sizeof(listint_t));
	if (!ret)
		return (NULL);
	ret->next = NULL;
	ret->n = n;
	return (ret);
}
