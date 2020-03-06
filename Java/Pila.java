package allstructdati;

/**
 *
 * @author Alessandro Mazzeo
 */
public class Pila {

    protected Nodo first;
    private Nodo n;
    private int size;
/**
 * <B>COMMENT:</B>Set size to 0.
 */
    public Pila() {
        size = 0;
    }
/**
 * 
 * @return boolean:TRUE if the stack is empty.
 */
    public boolean isEmpty() {
        return n == null;
    }

    /**
     * 
     * @param obj
     * <B>COMMENT:</B>Insert an object in the stack.
     */
    
    public void push(Object obj) {
        if (obj == null) {
            return;
        }
        n = new Nodo(obj);
        n.next = first;
        first = n;
        size++;
    }

    /**
     *<B>COMMENT:</B>Remove the first objetct to the stack.
     */
    public void pop() {
        size--;
        n = n.next;
    }

    /**
     * 
     * @return Object:The last object entered in the stack.
     */
    public Object top() {
        return n.dato;
    }
    /**
     * 
     * @return int:The size of stack. 
     */
    public int getSize() {
        return size;
    }
}
