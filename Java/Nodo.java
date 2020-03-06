package allstructdati;

/**
 *
 * @author Alessandro Mazzeo
 */
public class Nodo {

    protected Object dato;
    protected Nodo next;

    protected Nodo() {
    }

    /**
     * 
     * @param ob 
     * <B>COMMENT:</B>Object to insert in Nodo.
     */
    protected Nodo(Object ob) {
        dato = ob;
        next = null;
    }

    /**
     * 
     * @param ob
     * @param n 
     * <B>COMMENT:</B>Object to insert in Nodo with next position.
     */
    protected Nodo(Object ob, Nodo n) {
        dato = ob;
        next = n;
    }

}
