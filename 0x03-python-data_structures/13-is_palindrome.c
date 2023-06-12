#include <stdlib.h>
#include "lists.h"
/**
* reverse_list - Reverses a linked list
* @head: Pointer to the head of the list
* Return: Pointer to the new head of the reversed list
*/
listint_t *reverse_list(listint_t *head)
{
listint_t *prev = NULL;
listint_t *current = head;
listint_t *next = NULL;
while (current != NULL)
{
next = current->next;
current->next = prev;
prev = current;
current = next;
}
return (prev);
}
/**
* get_middle - Finds the middle node of a linked list
* @head: Pointer to the head of the list
* Return: Pointer to the middle node
*/
listint_t *get_middle(listint_t *head)
{
listint_t *slow_ptr = head;
listint_t *fast_ptr = head;
while (fast_ptr != NULL && fast_ptr->next != NULL)
{
fast_ptr = fast_ptr->next->next;
slow_ptr = slow_ptr->next;
}
return (slow_ptr);
}
/**
* compare_lists - Compares two linked lists
* @list1: Pointer to the first list
* @list2: Pointer to the second list
* Return: 1 if the lists are equal, 0 otherwise
*/
int compare_lists(listint_t *list1, listint_t *list2)
{
while (list1 != NULL && list2 != NULL)
{
if (list1->n != list2->n)
return (0);
list1 = list1->next;
list2 = list2->next;
}
return (list1 == NULL && list2 == NULL);
}
/**
* is_palindrome - Checks if a singly linked list is a palindrome
* @head: Pointer to the head of the list
* Return: 1 if the list is a palindrome, 0 otherwise
*/
int is_palindrome(listint_t **head)
{
if (*head == NULL || (*head)->next == NULL)
return (1);
listint_t *middle = get_middle(*head);
listint_t *second_half = reverse_list(middle->next);
listint_t *temp = second_half;
int is_palindrome = 1;
while (*head != NULL && temp != NULL)
{
if ((*head)->n != temp->n)
{
is_palindrome = 0;
break;
}
*head = (*head)->next;
temp = temp->next;
}
second_half = reverse_list(second_half);
middle->next = second_half;
return (is_palindrome);
}
