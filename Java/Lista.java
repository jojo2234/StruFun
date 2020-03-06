package allstructdati;


/**
 *
 * @author Alessandro Mazzeo
 */
public final class Lista {

    protected Nodo first;
    private Nodo temp;
    private Nodo prec;
    private int size;

    /**
     * <B>COMMENT:</B>After this is possible insert elements in this list.
     */
    public Lista() {
        first = null;
        size = 0;
    }

    /**
     *
     * @param dato
     * <B>COMMENT:</B>Create a list with a first element.
     */
    public Lista(Object dato) {
        this.insertHead(dato);
    }

    /**
     *
     * @param dato
     * <B>COMMENT:</B>Insert an element in the first position of the list.
     */
    public void insertHead(Object dato) {
        if (dato == null) {
            System.out.println("Object null!!!");
            return;
        }
        Nodo n = new Nodo(dato);
        n.next = first;
        first = n;
        size++;
    }

    /**
     *
     * @param dato
     * <B>COMMENT:</B>Insert an element in a latest position of the list.
     */
    public void insertTile(Object dato) {
        if (dato == null) {
            System.out.println("Object null!!!");
            return;
        }
        Nodo n = new Nodo(dato);
        temp = first;
        while (temp.next != null) {
            temp = temp.next;
        }
        temp.next = n;
        size++;
    }

    /**
     *
     * @param dato
     * @param position
     * <B>COMMENT:</B>Insert an element in a specified position.
     */
    public void insertPosition(Object dato, int position) {
        if (dato == null) {
            System.out.println("Object null!!!");
            return;
        }
        if (position <= 0) {
            this.insertHead(dato);
            return;
        }
        Nodo n = new Nodo(dato);
        if (position <= size) {
            temp = first;
            for (int i = 0; i < position; i++) {
                prec = temp;
                temp = temp.next;
            }
            prec.next = n;
            n.next = temp;
            size++;
        } else {
            System.out.println("Error the position doesn't exist!");
        }
    }

    /**
     *
     * @param position
     * <B>COMMENT:</B>Remove an element from a specified position.
     */
    public void remove(int position) {
        if (position > size || position < 0) {
            System.out.println("Error the position doesn't exist!");
            return;
        }
        temp = first;
        for (int i = 0; i < position; i++) {
            prec = temp;
            temp = temp.next;
        }
        if (position == size) {
            prec.next = null;
            size--;
        } else {
            prec.next = temp.next; //prec.next = prec.next.next;
            size--;
        }
    }

    /**
     *
     * @param dato
     * @return boolean
     * <B>COMMENT:</B>Remove all type of object equals in the list.
     */
    public boolean remove(Object dato) {
        boolean ret = false;
        if (dato == null) {
            return false;
        }
        temp = first;
        prec = null;
        while (temp != null) {
            if (temp.dato.equals(dato)) {
                if (prec == null) {
                    first = first.next;
                } else {
                    prec.next = prec.next.next;
                }
                ret = true;
                size--;
            }
            prec = temp;
            temp = temp.next;
        }
        return ret;
    }
 
    /**
     *
     * @param position
     * @return Object:The object in that position.
     */
    public Object elementAt(int position) {
        temp = first;
        for (int i = 0; i < position; i++) {
            prec = temp;
            temp = temp.next;
        }
        return temp.dato;
    }

    /**
     *
     * @return int:The size of list.
     */
    public int getSize() {
        return size;
    }

}
