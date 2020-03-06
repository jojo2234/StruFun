package allstructdati;

public class IteratoreLista implements Iteratore {

    Lista c;
    Nodo cursore;

    public IteratoreLista(Lista aThis) {
        c = aThis;
        goFirst();
    }

    @Override
    public boolean inside() {
        return (cursore != null);
    }

    @Override
    public Object current() {
        if (!inside()) {
            throw new RuntimeException("Elemento disponibile");
        }
        return cursore.dato;
    }

    @Override
    public void goNext() {
        if (!inside()) {
            throw new RuntimeException("Elemento disponibile");
        }
        cursore = cursore.next;
    }

    @Override
    public void goFirst() {
        cursore = c.first;
    }

}
