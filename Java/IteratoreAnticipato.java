package allstructdati;

/**
 *
 * @author Alessandro Mazzeo
 * <B>COMMENT:</B>Class to create an iterator with visita anticipata.
 */
public class IteratoreAnticipato implements Iteratore {

    AlberoBin a;
    AlberoBin cursore;
    Pila p;

    public IteratoreAnticipato() {
    }

    /**
     *
     * @param x
     * <B>COMMENT:</B>Used to set cursore an a to first element of x.
     */
    public IteratoreAnticipato(AlberoBin x) {
        a = cursore = x;
        p = new Pila();
    }

    /**
     *
     * @return logic:true if the iterator is empty.
     */
    @Override
    public boolean inside() {
        return cursore != AlberoBin.EMPTY;
    }

    /**
     *
     * @return object: The object at position current.
     */
    @Override
    public Object current() {
        if (a.isEmpty() == false) {
            return cursore.getDato();
        } else {
            return null;
        }
    }

    /**
     * <B>COMMENT:</B>Move cursore on next tree.
     */
    @Override
    public void goNext() {
        if (a.isEmpty() == false) {
            if (cursore.getRight().isEmpty()) {
                p.push(cursore.getRight());
            }
            if (cursore.getLeft().isEmpty()) {
                if (p.isEmpty()) {
                    cursore = AlberoBin.EMPTY;
                } else {
                    cursore = (AlberoBin) p.top();
                    p.pop();
                }
            }
        }
    }

    /**
     * <B>COMMENT:</B>Go to root of tree.
     */
    @Override
    public void goFirst() {
        cursore = a;
        p = new Pila();
    }

}
