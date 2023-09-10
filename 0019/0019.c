struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode* removeNthFromEnd(struct ListNode* head, int n){
    struct ListNode* dummy = (struct ListNode*)malloc(sizeof(struct ListNode));
    struct ListNode* left = dummy;
    struct ListNode* right = dummy;
    struct ListNode* prev = left;
    int distance = 0;
    dummy->next = head;

    while(right->next){
        prev = left;
        if (distance == n - 1){
            left = left->next;
        }
        else{
           distance ++; 
        }
        right = right->next;
    }

    prev->next = prev->next->next;
    
    return dummy->next;
}