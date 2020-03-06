package allstructdati;

/**
 *
 * @author Alessandro Mazzeo
 */
public class AlberoBin implements Attraversabile {

    private Object dato;
    private AlberoBin right;
    private AlberoBin left;
    private String str;
    protected static final AlberoBin EMPTY = new AlberoBin(null, null, null);

    public AlberoBin() {
    }

    /**
     *
     * @param dato
     * @param right
     * @param left
     */
    public AlberoBin(Object dato, AlberoBin right, AlberoBin left) {
        if (dato != null) {
            this.dato = dato;
            this.right = right;
            this.left = left;
        }
    }

    /**
     *
     * @return AlberoBin:right.
     */
    public AlberoBin getRight() {
        return right;
    }

    /**
     *
     * @return AlberoBin:left.
     */
    public AlberoBin getLeft() {
        return left;
    }

    /**
     *
     * @return Object:dato.
     */
    public Object getDato() {
        return dato;
    }

    /**
     *
     * @param dato
     */
    public void setDato(Object dato) {
        this.dato = dato;
    }

    /**
     *
     * @param right
     */
    public void setRight(AlberoBin right) {
        this.right = right;
    }

    /**
     *
     * @param left
     */
    public void setLeft(AlberoBin left) {
        this.left = left;
    }

    /**
     *
     * @return true:If the tree is empty.
     */
    public boolean isEmpty() {
        return (this == EMPTY);
    }

    /**
     *
     * @param a
     * @param livello
     * @return ricorsive
     * <B>COMMENT:</B>Used to position in a specified livel right, set dato at
     * new level.
     */
    public Object visitaRight(AlberoBin a, int livello) {
        if (a != null) {
            if (livello == 0) {
                dato = a.getDato();
            } else {
                return visitaRight(a.getRight(), --livello);
            }
        }
        return null;
    }

    /**
     *
     * @param a
     * @param livello
     * @return ricorsive
     * <B>COMMENT:</B>Used to position in a specified livel left, set dato at
     * new level.
     */
    public Object visitaLeft(AlberoBin a, int livello) {
        if (a != null) {
            if (livello == 0) {
                dato = a.getDato();
            } else {
                return visitaLeft(a.getLeft(), --livello);
            }
        }
        return null;
    }

    /**
     *
     * @param a
     * <B>COMMENT:</B>Used to print element with visita anticipata.
     */
    public void visitaAnticipata(AlberoBin a) {
        if (a != null) {
            str += a.getDato();
            System.out.println(a.getDato());
            visitaAnticipata(a.getLeft());
            visitaAnticipata(a.getRight());
        }
    }

    /**
     *
     * @param a
     * <B>COMMENT:</B>Used to print element with visita simmetrica.
     */
    public void visitaSimmetrica(AlberoBin a) {
        if (a != null) {
            visitaSimmetrica(a.getLeft());
            str += a.getDato();
            System.out.println(a.getDato());
            visitaSimmetrica(a.getRight());
        }
    }

    /**
     *
     * @param a
     * <B>COMMENT:</B>Used to print element with visita posticipata.
     */
    public void visitaPosticipata(AlberoBin a) {
        if (a != null) {
            visitaPosticipata(a.getLeft());
            visitaPosticipata(a.getRight());
            str += a.getDato();
            System.out.println(a.getDato());
        }
    }

    /**
     *
     * @param a
     * @return logic:True if the tree are equals.
     */
    public boolean equals(AlberoBin a) {
        if (a != null) {
            this.visitaAnticipata(a);
            String temp = str;
            this.visitaAnticipata(this);
            return temp.equals(str);
        } else {
            return this == null;
        }
    }

    /**
     * 
     * @param a
     * @return AlberoBin:The tree with right and left inverted. 
     */
    public AlberoBin mirror(AlberoBin a) {
        return null;
    }

    @Override
    public Iteratore newIterator() {
        return new IteratoreAnticipato();
    }

}
