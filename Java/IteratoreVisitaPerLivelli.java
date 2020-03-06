package allstructdati;

/**
 *
 * @author Alessandro Mazzeo
 */
public class IteratoreVisitaPerLivelli implements Iteratore {

    Albero daAttraversare;
    Albero cursore;
    Coda q;

    public IteratoreVisitaPerLivelli(Albero a) {
        daAttraversare = a;
        goFirst();
    }

    @Override
    public boolean inside() {
        return !q.isEmpty();
    }

    @Override
    public Object current() {
        assert inside() : "current non applicabile";
        return ((Albero) q.front()).getDato();
    }

    @Override
    public void goNext() {
        assert inside() : "goNext non applicabile";
        cursore = (Albero) q.front();
        q.denqueue();
        Albero h = cursore.getChild();
        while(!h.isEmpty()){
            q.enqueue(h);
            h = h.getBrother();
        }
    }

    @Override
    public void goFirst() {
        q = new Coda();
        if (!daAttraversare.isEmpty()) {
            q.enqueue(daAttraversare);
            Albero h = daAttraversare.getBrother();
            while (!h.isEmpty()) {
                q.enqueue(h);
                h = h.getBrother();
            }
        }
    }

}
