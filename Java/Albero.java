package allstructdati;

/**
 *
 * @author Alessandro Mazzeo
 */
public class Albero implements Attraversabile {

    protected Object dato;
    protected Albero child;
    protected Albero brother;
    protected static final Albero EMPTY = new Albero(null, null);

    public Albero() {
    }

    public Albero(Object dato, Albero child) {
        this.dato = dato;
        this.child = child;
        this.brother = EMPTY;
    }

    public Albero(Object dato, Albero child, Albero brother) {
        if (dato != null) {
            this.dato = dato;
            this.child = child;
            this.brother = brother;
        }
    }

    public Object getDato() {
        return dato;
    }

    public Albero getChild() {
        return child;
    }

    public Albero getBrother() {
        return brother;
    }

    public void setDato(Object dato) {
        if (dato != null) {
            this.dato = dato;
        }
    }

    public void setChild(Albero child) {
        this.child = child;
    }

    public void setBrother(Albero brother) {
        this.brother = brother;
    }

    public boolean isEmpty() {
        return this == Albero.EMPTY;
    }

    public void visitaAnticipata(Albero a) {
        if (!a.isEmpty()) {
            System.out.println(a.getDato());
            visitaAnticipata(a.getChild());
            visitaAnticipata(a.getBrother());
        }
    }

    public void visitaPosticipata(Albero a) {
        if (!a.isEmpty()) {
            visitaPosticipata(a.getChild());
            visitaPosticipata(a.getBrother());
            System.out.println(a.getDato());
        }
    }

    public void visitaLivelli(Albero a) {
        if (!a.isEmpty()) {
            Coda c = new Coda();
            c.enqueue(a.getDato());
            c.enqueue(a.getChild());
            c.enqueue(a.getBrother());
        }
    }

    @Override
    public String toString() {
        String resoult;
        if (isEmpty()) {
            resoult = "EMPTY";
        } else {
            resoult = "Albero:" + getDato();
            if (!child.isEmpty()) {
                resoult += "(" + getChild() + ")";
            }
            Albero h = brother;
            if (!h.isEmpty()) {
                resoult += "," + h;
            }
        }
        return resoult;
    }

    @Override
    public Iteratore newIterator() {
        return new IteratoreAlbero(this);
    }

    public Iteratore breadthFirstIterator() {
        return new IteratoreVisitaPerLivelli(this);
    }
}
