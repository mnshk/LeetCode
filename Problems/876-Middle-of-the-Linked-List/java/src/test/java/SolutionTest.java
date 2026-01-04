import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;
import java.util.List;

public class SolutionTest {
    @Test
    public void testMiddleNode(){
        Solution1<Integer> solution1 = new Solution1<>();
        Solution2<Integer> solution2 = new Solution2<>();

        List<Integer> input = List.of(1,2,3,4,5);

        ListNode<Integer> head = ListNode.from_list(input);
        ListNode<Integer> result = solution1.middleNode(head);
        Assertions.assertEquals(List.of(3,4,5),ListNode.to_list(result));

        head = ListNode.from_list(input);
        result = solution2.middleNode(head);
        Assertions.assertEquals(List.of(3,4,5),ListNode.to_list(result));
    }
}
