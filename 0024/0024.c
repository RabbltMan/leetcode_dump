#include <stdio.h>

struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode* swapPairs(struct ListNode* head){
    struct ListNode* dummy = (struct ListNode* )malloc(sizeof(struct ListNode));
    dummy->next = head;
    struct ListNode* currentNode = dummy->next;
    struct ListNode* prevNode = dummy;
    struct ListNode* postNode = currentNode && currentNode->next ? currentNode->next : NULL;

    while(postNode){
        prevNode->next = postNode;
        currentNode->next = postNode->next;
        postNode->next = currentNode;
        prevNode = prevNode->next->next;
        currentNode = prevNode->next;
        postNode = currentNode && currentNode->next ? currentNode->next : NULL;
    }

    return dummy->next;
}
