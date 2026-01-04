import java.util.ArrayList;
import java.util.List;

public class ListNode<T> {

    T val;
    ListNode<T> next;

    ListNode(){}
    ListNode(T val){
        this.val = val;
    }
    ListNode(T val, ListNode<T> next){
        this.val = val;
        this.next = next;
    }

    public static <T> ListNode<T> from_list(List<T> list){
        ListNode<T> head = new ListNode<T>();
        ListNode<T> curr = head;
        for (T item : list) {
            curr.next = new ListNode<>(item);
            curr = curr.next;
        }
        return head.next;
    }

    public static <T> List<T> to_list(ListNode<T> head){
        ListNode<T> curr = head;
        List<T> list = new ArrayList<>();
        while(curr != null){
            list.add(curr.val);
            curr = curr.next;
        }
        return list;
    }
}
