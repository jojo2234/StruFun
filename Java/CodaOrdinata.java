package allstructdati;

/**
 *
 * @author Alessandro Mazzeo
 */
public class CodaOrdinata extends Coda {

    private Nodo first;

    @Override
    public void enqueue(Object ob) {
        Nodo appo = first;
        if (ob == null || !(ob instanceof Comparable)) {
            return;
        }
        if (isEmpty()) {
            Nodo n = new Nodo(ob, appo.next);
            appo = n;
        } else {
            Comparable i = (Comparable) appo.dato;
            while (appo.next != null && i.compareTo(ob) > 0) {
                appo = appo.next;
                i = (Comparable) appo.dato;
            }
            Nodo n = new Nodo(ob,null);
            appo.next = n;   
        }
    }
}
