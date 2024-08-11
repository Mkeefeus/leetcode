// Definition for singly-linked list.
class ListNode {
    val: number;
    next: ListNode | null;
    constructor(val?: number, next?: ListNode | null) {
        this.val = val === undefined ? 0 : val;
        this.next = next === undefined ? null : next;
    }
}

function generateListNodes(l1: ListNode | null, l2: ListNode | null, carry: number = 0): ListNode {
    let x = l1 !== null ? l1.val : 0;
    let y = l2 !== null ? l2.val : 0;
    let sum = carry + x + y;
    carry = Math.floor(sum / 10);
    const next1 = l1?.next || null;
    const next2 = l2?.next || null;
    const nextNode = next1 || next2 || carry ? generateListNodes(next1, next2, carry) : null;
    return new ListNode(sum % 10, nextNode);
}

function addTwoNumbers(l1: ListNode | null, l2: ListNode | null): ListNode | null {
    if (!l1 || !l2) return null;
    return generateListNodes(l1, l2);
}
