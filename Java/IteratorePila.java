package allstructdati;

/**
 *
 * @author Alessandro Mazzeo
 */
public class IteratorePila implements Iteratore {

    Pila c;
    Nodo cursore;

    public IteratorePila(Pila c) {
        this.c = c;
        this.goFirst();
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
