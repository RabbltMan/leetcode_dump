// Definition for singly-linked list.
struct ListNode {
     int val;
     struct ListNode *next;
};


struct ListNode* reverseBetween(struct ListNode* head, int left, int right){
    struct ListNode* dummy = malloc(sizeof(struct ListNode));
    struct ListNode* leftEdge = dummy;

    dummy->next = head;
    leftEdge->next = head;

    for(int i = 0; i < left-1; i++){
        leftEdge = leftEdge->next;
    }

    struct ListNode* prevNode = malloc(sizeof(struct ListNode));
    struct ListNode* currentNode = leftEdge->next;

    for (int i = 0; i < right - left + 1; i++){
        struct ListNode* nextNode = currentNode->next;
        currentNode->next = prevNode;
        prevNode = currentNode;
        currentNode = nextNode;
    }

    leftEdge->next->next = currentNode;
    leftEdge->next = prevNode;

    return dummy->next;
}