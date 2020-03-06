package allstructdati;

/**
 *
 * @author Alessandro Mazzeo
 */
public class Coda {

    private Nodo n;
    private Nodo coda;
    private int size;

    public Coda() {
        size = 0;
    }
    /**
     * 
     * @return logic:True if the tail is empty.
     */
    public boolean isEmpty() {
        return (size <= 0);
    }
    /**
     * 
     * @param ob 
     * <B>COMMENT:</B>Push an element in tail.
     */
    public void enqueue(Object ob) {
        if (isEmpty()) {
            coda = new Nodo(ob, null);
            n = coda;
        } else {
            coda.next = new Nodo(ob, null);
            coda = coda.next;
        }
        size++;
    }
    /**
     * 
     * <B>COMMENT:</B>Remove an element from tail.
     */
    public void denqueue() {
        if (isEmpty()) {
            System.out.println("Errore!!!");
        }
        n = n.next;
        size--;
    }
    /**
     * 
     * @return Object:dato
     */
    public Object front() {
        if(isEmpty()){
            System.out.println("Errore!!!");
        }
        return n.dato;
    }
}
