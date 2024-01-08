#include"lists.h"
#include<stdlib.h>
#include<stdio.h>

/**
 * *add_nodeint-addsanewnodeatthebeginningofalistint_tlist
 * *@head:headoflistint_t
 * *@n:inttoaddinlistint_tlist
 * *Return:addressofthenewelement,orNULLifitfailed
 * */
listint_t*add_nodeint(listint_t**head,constintn)
{
		listint_t*new;

			new=malloc(sizeof(listint_t));
				if(new==NULL)
							return(NULL);
					new->n=n;
						new->next=*head;
							*head=new;
								return(new);
}
/**
 * *is_palindrome-identifyifasynglelinkedlistispalindrome
 * *@head:headoflistint_t
 * *Return:1ifitispalindromeelse0
 * */
intis_palindrome(listint_t**head)
{
		listint_t*head2=*head;
			listint_t*aux=NULL,*aux2=NULL;

				if(*head==NULL||head2->next==NULL)
							return(1);
					while(head2!=NULL)
							{
										add_nodeint(&aux,head2->n);
												head2=head2->next;
													}
						aux2=aux;
							while(*head!=NULL)
									{
												if((*head)->n!=aux2->n)
															{
																			free_listint(aux);
																						return(0);
																								}
														*head=(*head)->next;
																aux2=aux2->next;
																	}
								free_listint(aux);
									return(1);
}

